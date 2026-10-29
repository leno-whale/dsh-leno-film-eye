/**
 * 对齐表：把「时间 / 帧 / 音量 / 切点」放到同一行上。
 *
 * 为什么要这张表：单独看画面会漏掉声音的变化，单独看声音不知道画面在干什么。
 * 三条线对齐之后，「声音在这里掉下去」和「画面在这里转场」才能被看见是同一件事。
 *
 * 手法：音量不走「每个窗口调一次 ffmpeg」，而是一次解码成 8kHz 单声道 PCM、
 * 在内存里按窗口算 RMS。三小时的片子按 600 秒切块解码，避免一次读几百 MB。
 */
import fs from 'node:fs';
import path from 'node:path';

import { run, runRaw, resolveBin, ts } from './ff.js';
import { shots } from './film.js';

const RATE = 8000; // 8kHz 足够算音量
const CHUNK_SEC = 600; // 每次解码 10 分钟

/** 解码一段 → 每 window 秒一个 dB 值（0 点是满刻度，静音约 -90）。 */
function audioLevels(file, { from, to, window }) {
  const ffmpeg = resolveBin('ffmpeg');
  const out = [];
  const startSec = from ? Number(from) : 0;
  const endSec = to ? Number(to) : null;
  let cursor = startSec;

  for (;;) {
    const len = endSec ? Math.min(CHUNK_SEC, endSec - cursor) : CHUNK_SEC;
    if (len <= 0) break;
    const args = ['-hide_banner', '-loglevel', 'error'];
    if (cursor > 0) args.push('-ss', String(cursor));
    args.push('-i', file, '-t', String(len), '-vn', '-ac', '1', '-ar', String(RATE), '-f', 's16le', '-');
    const r = runRaw(ffmpeg, args, { timeout: 300000 });
    if (r.code !== 0 || !r.stdout || !r.stdout.length) break;

    const buf = r.stdout;
    const samples = Math.floor(buf.length / 2);
    const perWindow = Math.floor(window * RATE);
    for (let i = 0; i < samples; i += perWindow) {
      const n = Math.min(perWindow, samples - i);
      let sum = 0;
      for (let k = 0; k < n; k += 1) {
        const v = buf.readInt16LE((i + k) * 2) / 32768;
        sum += v * v;
      }
      const rms = Math.sqrt(sum / n);
      // 满刻度正弦的 RMS 是 -3.01 dB；这里用 20log10(rms)，静音钳到 -90
      out.push({
        t: Math.round(cursor + (i / RATE) * 10) / 10,
        db: rms > 0 ? Math.max(-90, Math.round(20 * Math.log10(rms) * 10) / 10) : -90,
      });
    }
    cursor += len;
    if (!endSec && len < CHUNK_SEC) break; // 读到底了
  }
  return out;
}

/**
 * 生成对齐表。
 * @returns {Promise<{ok, rows, frames, cuts, maxDrop, silentTail, outDir?}>}
 */
export async function align(file, opts = {}) {
  if (!fs.existsSync(file)) return { ok: false, error: `文件不存在：${file}` };
  const interval = Math.max(1, Number(opts.interval) || 4);
  const from = opts.from ? Number(opts.from) : null;
  const to = opts.to ? Number(opts.to) : null;
  const outDir = opts.outDir || '';

  const ffmpeg = resolveBin('ffmpeg');
  if (!ffmpeg) return { ok: false, error: '找不到 ffmpeg' };

  // 1) 音量
  const levels = audioLevels(file, { from, to, window: interval });
  if (!levels.length) return { ok: false, error: '音量解码失败（可能是没有音轨）' };

  // 2) 切点
  let cuts = [];
  try {
    const s = await shots(file, { threshold: opts.threshold ?? 0.3 });
    cuts = (s.cuts || []).map((c) => Math.round(c * 10) / 10);
  } catch {
    cuts = [];
  }

  // 3) 抽帧（可选：给了 outDir 才落盘，避免默认往工作区写图）
  let frames = [];
  if (outDir) {
    const dir = path.join(outDir, 'frames');
    fs.mkdirSync(dir, { recursive: true });
    const args = ['-hide_banner', '-loglevel', 'error', '-y'];
    if (from) args.push('-ss', String(from));
    if (to) args.push('-to', String(to));
    args.push('-i', file, '-vf', `fps=1/${interval},scale=480:-1`, '-q:v', '3', path.join(dir, 'f_%04d.jpg'));
    const r = run(ffmpeg, args, { timeout: 300000 });
    if (r.code === 0) {
      frames = fs.readdirSync(dir).filter((f) => f.endsWith('.jpg')).sort()
        .map((f) => path.join(dir, f));
    }
  }

  // 4) 合成行：每行一个时间点
  const rows = levels.map((lv, i) => {
    // 这一行距离最近的切点有多远（最近的切点在这一格内 ⇒ 记 cut）
    const inThis = cuts.find((c) => c >= lv.t && c < lv.t + interval);
    const prev = [...levels].slice(0, i).reverse().find((p) => p.db < -60);
    return {
      t: lv.t,
      db: lv.db,
      frame: frames[i] ? path.basename(frames[i]) : '',
      cut: inThis !== undefined ? Math.round(inThis * 10) / 10 : null,
      afterSilence: Boolean(prev),
    };
  });

  // 5) 两个要点：最大跌落、尾巴是否静音
  let maxDrop = { drop: 0, at: null, from: null, to: null };
  for (let i = 1; i < levels.length; i += 1) {
    const d = levels[i].db - levels[i - 1].db;
    if (d < maxDrop.drop) maxDrop = { drop: Math.round(d * 10) / 10, at: levels[i].t, from: levels[i - 1].db, to: levels[i].db };
  }
  const tail = levels.slice(-2);
  const silentTail = tail.length === 2 && tail[1].db < -50;

  const text = [
    `对齐表：${path.basename(file)}`,
    `时长 ${ts(levels[levels.length - 1].t)}｜窗口 ${interval} 秒｜${rows.length} 行｜切点 ${cuts.length} 个`,
    `最大跌落 ${maxDrop.at === null ? '无' : `${ts(maxDrop.at)} ${maxDrop.from} → ${maxDrop.to} dB（${maxDrop.drop} dB）`}`,
    `尾巴${silentTail ? `静音（最后 ${tail[1].db} dB）` : `不静音（最后 ${tail[1].db} dB）`}`,
    frames.length ? `帧 ${frames.length} 张` : '帧：未落盘（没给 outDir）',
    '',
    '时间     音量dB  切点   帧',
    ...rows.map((r) => `${ts(r.t).padEnd(9)} ${String(r.db).padStart(6)}  ${r.cut !== null ? '●' : ' '}    ${r.frame}`),
  ].join('\n');

  if (outDir) {
    fs.mkdirSync(outDir, { recursive: true });
    fs.writeFileSync(path.join(outDir, 'align.tsv'), [
      ['t', 'db', 'cut', 'frame'].join('\t'),
      ...rows.map((r) => [r.t, r.db, r.cut ?? '', r.frame].join('\t')),
    ].join('\n') + '\n', 'utf8');
  }

  return { ok: true, rows, frames, cuts, maxDrop, silentTail, text, outDir };
}
