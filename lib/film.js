import fs from 'node:fs';
import path from 'node:path';
import { run, probeDuration, ts } from './ff.js';

/** 每张拼图几秒（默认 8 秒 × 9 格 ≈ 72 秒一页）。 */
export const DEFAULT_INTERVAL = 8;
export const GRID = 3;

/**
 * 连续画面：固定间隔抽帧、九张拼一页。
 * 与「场景切换抽帧」的区别：后者只拍剪辑点，前者拍时间轴——能看出东西在动。
 */
export function sheets(file, { from = 0, to = null, interval = DEFAULT_INTERVAL, max = 3, outDir } = {}) {
  const dur = probeDuration(file);
  if (!dur) return { ok: false, error: 'ffprobe 读不到时长（文件不存在或不是媒体）' };
  const start = Math.max(0, Number(from) || 0);
  const end = to == null ? dur : Math.min(dur, Number(to));
  if (!(end > start)) return { ok: false, error: `区间为空：from=${start} to=${end}` };

  const dir = outDir || path.join(process.cwd(), '.film-eye-sheets');
  fs.mkdirSync(dir, { recursive: true });

  const args = ['-hide_banner', '-loglevel', 'error', '-y'];
  if (start > 0) args.push('-ss', ts(start));
  args.push('-i', file, '-t', ts(end - start));
  const scale = 480;
  args.push('-vf', `fps=1/${Math.max(1, interval)},scale=${scale}:-1,tile=${GRID}x${GRID}`, '-frames:v', String(Math.max(1, max)));
  const pattern = path.join(dir, 'sheet_%03d.jpg');
  args.push(pattern);

  const r = run('ffmpeg', args);
  if (r.code !== 0) return { ok: false, error: `ffmpeg 失败：${r.stderr.split('\n').filter(Boolean).slice(-2).join(' / ')}` };

  const files = fs
    .readdirSync(dir)
    .filter((f) => /^sheet_\d+\.jpg$/.test(f))
    .sort()
    .map((f) => path.join(dir, f));

  const covered = Math.min(end - start, max * GRID * GRID * Math.max(1, interval));
  return {
    ok: true,
    files,
    count: files.length,
    interval,
    grid: GRID,
    coveredSec: Math.round(covered),
    totalSec: Math.round(end - start),
    note: files.length === 0 ? '没出图：区间太短或 ffmpeg 不支持 tile' : '',
  };
}

/** 声音：哪几段是静的、整体多响。文字转不出「他停了两秒」。 */
export function audioProfile(file, { from = 0, to = null, noiseDb = -40, minSilence = 0.5 } = {}) {
  const dur = probeDuration(file);
  if (!dur) return { ok: false, error: '读不到时长' };

  const args = ['-hide_banner', '-loglevel', 'info'];
  if (from > 0) args.push('-ss', ts(from));
  args.push('-i', file);
  if (to != null) args.push('-t', ts(Math.max(0, to - from)));
  args.push('-af', `silencedetect=noise=${noiseDb}dB:d=${minSilence}`, '-f', 'null', '-');

  const r = run('ffmpeg', args);
  const log = `${r.stderr}`;
  const silences = [];
  let cur = null;
  for (const line of log.split(/\r?\n/)) {
    const s = /silence_start:\s*(-?[\d.]+)/.exec(line);
    if (s) {
      cur = { start: Number(s[1]) };
      continue;
    }
    const e = /silence_end:\s*(-?[\d.]+)\s*\|\s*silence_duration:\s*([\d.]+)/.exec(line);
    if (e && cur) {
      silences.push({ start: cur.start, end: Number(e[1]), seconds: Number(e[2]) });
      cur = null;
    }
  }
  if (cur) silences.push({ start: cur.start, end: null, seconds: null });

  // 整体响度（单独跑一次，silencedetect 不给这个）
  const v = run('ffmpeg', ['-hide_banner', '-nostats', '-i', file, '-af', 'volumedetect', '-f', 'null', '-']);
  const mean = /mean_volume:\s*(-?[\d.]+) dB/.exec(v.stderr);
  const max = /max_volume:\s*(-?[\d.]+) dB/.exec(v.stderr);

  const audible = [];
  let cursor = from;
  for (const s of silences) {
    if (s.start > cursor) audible.push({ start: cursor, end: Math.min(s.start, to ?? dur) });
    cursor = s.end ?? to ?? dur;
  }
  if (cursor < (to ?? dur)) audible.push({ start: cursor, end: to ?? dur });

  return {
    ok: true,
    duration: Math.round(dur),
    meanDb: mean ? Number(mean[1]) : null,
    maxDb: max ? Number(max[1]) : null,
    silences: silences.map((s) => ({ ...s, start: round1(s.start), end: s.end == null ? null : round1(s.end) })),
    audible: audible.map((a) => ({ start: round1(a.start), end: round1(a.end) })),
  };
}

/** 镜头：剪辑点、每段多长、每分钟切几次。节奏是能算的，不用猜。 */
export function shots(file, { threshold = 0.3, from = 0, to = null } = {}) {
  const dur = probeDuration(file);
  if (!dur) return { ok: false, error: '读不到时长' };

  const args = ['-hide_banner', '-loglevel', 'info'];
  if (from > 0) args.push('-ss', ts(from));
  args.push('-i', file, '-an', '-vf', `select='gt(scene,${threshold})',metadata=print:file=-`, '-f', 'null', '-');

  const r = run('ffmpeg', args);
  const text = `${r.stdout}\n${r.stderr}`;
  const cuts = [];
  for (const line of text.split(/\r?\n/)) {
    const m = /pts_time:([\d.]+)/.exec(line);
    if (m) cuts.push(Number(m[1]));
  }
  const uniq = [...new Set(cuts)].sort((a, b) => a - b);
  const end = to ?? dur;
  const bounds = [from, ...uniq.filter((t) => t > from && t < end), end];
  const lens = [];
  for (let i = 1; i < bounds.length; i += 1) lens.push(round1(bounds[i] - bounds[i - 1]));
  const avg = lens.length ? lens.reduce((a, b) => a + b, 0) / lens.length : 0;
  return {
    ok: true,
    duration: round1(end - from),
    cuts: uniq.filter((t) => t > from && t < end).map(round1),
    shotCount: lens.length,
    avgShotSec: round1(avg),
    longestShotSec: lens.length ? Math.max(...lens) : null,
    cutsPerMinute: lens.length > 1 ? round1((lens.length - 1) / ((end - from) / 60)) : 0,
  };
}

const round1 = (x) => Math.round(Number(x) * 10) / 10;
