import { spawnSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';

/**
 * 找 ffmpeg / ffprobe。顺序：
 *   1. 环境变量 FILM_EYE_FFMPEG / FILM_EYE_FFPROBE（整条路径）
 *   2. 本机已有副本（bili-whale 装过一份，直接用，不重复下载 100MB）
 *   3. PATH
 * 找不到就报错说清楚，不要静默用错的版本。
 */
const HOME = process.env.USERPROFILE || process.env.HOME || '';

const DIRS = [
  path.join(HOME, '.dsh', 'bili-whale', 'bin'),
  path.join(HOME, '.dsh', 'bili-whale', 'tools', 'bin'),
  path.join(HOME, '.dsh', 'tools'),
  path.join(HOME, '.dsh', 'film-eye', 'bin'),
];

const cache = new Map();

export function resolveBin(base) {
  if (cache.has(base)) return cache.get(base);
  const envKey = base === 'ffmpeg' ? 'FILM_EYE_FFMPEG' : 'FILM_EYE_FFPROBE';
  const fromEnv = process.env[envKey];
  if (fromEnv && fs.existsSync(fromEnv)) {
    cache.set(base, fromEnv);
    return fromEnv;
  }
  const exe = process.platform === 'win32' ? `${base}.exe` : base;
  for (const dir of DIRS) {
    const p = path.join(dir, exe);
    if (fs.existsSync(p)) {
      cache.set(base, p);
      return p;
    }
  }
  cache.set(base, base); // 交给 PATH
  return base;
}

/** 跑一条命令，返回 { code, stdout, stderr }。不抛异常——调用方自己判 code。 */
export function run(bin, args, { timeout = 120000 } = {}) {
  const resolved = bin === 'ffmpeg' || bin === 'ffprobe' ? resolveBin(bin) : bin;
  const r = spawnSync(resolved, args, {
    encoding: 'utf8',
    timeout,
    maxBuffer: 32 * 1024 * 1024,
    windowsHide: true,
  });
  return {
    code: typeof r.status === 'number' ? r.status : -1,
    stdout: r.stdout ?? '',
    stderr: r.stderr ?? '',
    error: r.error ?? null,
  };
}

/**
 * 跑一条命令，stdout 按**二进制**拿回来（给解码 PCM 用）。
 * `run()` 是 utf8，音频那种东西过一遍字符串就废了。
 */
export function runRaw(bin, args, { timeout = 120000 } = {}) {
  const resolved = bin === 'ffmpeg' || bin === 'ffprobe' ? resolveBin(bin) : bin;
  const r = spawnSync(resolved, args, {
    encoding: 'buffer',
    timeout,
    maxBuffer: 256 * 1024 * 1024,
    windowsHide: true,
  });
  return {
    code: typeof r.status === 'number' ? r.status : -1,
    stdout: r.stdout ?? Buffer.alloc(0),
    stderr: r.stderr ? r.stderr.toString('utf8') : '',
    error: r.error ?? null,
  };
}

/** 二进制可用吗（给体检和测试用）。 */
export function has(base) {
  const r = run(base, ['-version'], { timeout: 8000 });
  return r.code === 0;
}
/** 把秒数写成 ffmpeg 认的 HH:MM:SS.mmm。 */
export function ts(sec) {
  const s = Math.max(0, Number(sec) || 0);
  const h = Math.floor(s / 3600);
  const m = Math.floor((s % 3600) / 60);
  const r = s - h * 3600 - m * 60;
  const p2 = (x) => String(x).padStart(2, '0');
  return `${p2(h)}:${p2(m)}:${r.toFixed(3).padStart(6, '0')}`;
}

/** 读媒体时长（秒）；读不到返回 null。 */
export function probeDuration(file) {
  const r = run('ffprobe', [
    '-v', 'error',
    '-show_entries', 'format=duration',
    '-of', 'default=noprint_wrappers=1:nokey=1',
    file,
  ]);
  if (r.code !== 0) return null;
  const n = Number(String(r.stdout).trim());
  return Number.isFinite(n) && n > 0 ? n : null;
}
