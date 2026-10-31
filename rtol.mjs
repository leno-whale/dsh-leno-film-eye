// ρ_tol 压缩对实验（理论 §12.4c）——把「拍的 0.9」换成「测的」
//
// 口径（跑之前写死；改任何一条都要在结果文档里记一笔）：
//   参照 x ：源文件音轨按 pcm_s16le 提出（位精确，无再损失）。
//            注意：若源本身已是有损流（如 B 站 AAC ~190k），测的是「再压一道」的
//            增量损失，不是绝对保真——这一条写进结果，不许省。
//   D(x)  ：AAC-LC（ffmpeg 内置 aac 编码器），320 kbps 与 128 kbps 两档；
//            不动采样率与声道（单声道化在解码侧做，与 lib 的帧算子一致）。
//   特征集 F（全部复用本仓库 lib 的算子，不另造尺子）：
//     A. 窗口 RMS 序列 —— lib/align.js 的帧算子（8 kHz 单声道 s16le，线性域），
//         窗宽 w ∈ {0.5, 4, 30} s（4 s = film_align 默认）；每个窗的 RMS 视作一个 f
//     B. 平均窗 RMS（audioProfile.meanDb 的线性域对应物）
//     C. 峰值窗 RMS（max_volume 的窗域对应物）
//     D. volumedetect：mean_volume / max_volume（dB 差与线性域相对差并报）
//     E. 静段清单（silencedetect noise=-40 dB、d=0.5 s）：条数、总时长
//   统计  ：ρ̂ = 1 − sup_f |f(x) − f(Dx)| / max(|f(x)|, ε)，ε = 1e-4（≈ −80 dBFS）
//           逐特征报差；sup 取全体特征最大。
//   对比对：x→320k、x→128k、320k→128k（§12.4c 原文的字面例子）。
//   判读（先写死）：
//     ρ̂(x→320k) ≥ 0.9  ⇒ §1.2 拍的 0.9 在「再压一道 320k」口径下成立；
//     ρ̂(x→128k) < 0.9  ⇒ 128k 不算 S 内素材，S 的成立范围须写明位率边界。
//   什么能打死它：换素材后 ρ̂ 大幅变动 ⇒ 单素材不外推（结论只对本次素材成立）。
//
// 用法：node rtol.mjs <媒体文件>
// 产物：_tmp/rtol/rtol-<日期>.json（_tmp/ 已在 .gitignore，不进仓库）
// 中间媒体文件放 ~/.dsh/rtol-film-eye/（本机 ffmpeg 只被允许写 .dsh 树），跑完即删。
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { run, runRaw, resolveBin } from './lib/ff.js';
import { audioProfile } from './lib/film.js';

const SRC = process.argv[2];
if (!SRC || !fs.existsSync(SRC)) {
  console.error('用法：node rtol.mjs <媒体文件>');
  process.exit(1);
}

const TMP = path.join(os.homedir(), '.dsh', 'rtol-film-eye'); // ffmpeg 的写入白名单
const OUTDIR = path.join(import.meta.dirname, '_tmp', 'rtol'); // 结果 JSON 落仓库外层
fs.mkdirSync(TMP, { recursive: true });
fs.mkdirSync(OUTDIR, { recursive: true });

const EPS = 1e-4;
const WINDOWS = [0.5, 4, 30];
const RATE = 8000; // 与 lib/align.js 一致

const relDiff = (a, b) => Math.abs(a - b) / Math.max(Math.abs(a), EPS);
const toLinearDb = (db) => Math.pow(10, db / 20);

/** 解码整条音轨 → 8kHz 单声道采样（Float64，满刻度 1.0）。同 lib/align.js 的帧算子。 */
function decodePcm(file) {
  const ffmpeg = resolveBin('ffmpeg');
  const r = runRaw(ffmpeg, ['-hide_banner', '-loglevel', 'error', '-i', file,
    '-vn', '-ac', '1', '-ar', String(RATE), '-f', 's16le', '-'], { timeout: 300000 });
  if (r.code !== 0 || !r.stdout.length) throw new Error(`解码失败：${path.basename(file)} ${r.stderr.slice(-200)}`);
  const n = Math.floor(r.stdout.length / 2);
  const out = new Float64Array(n);
  for (let i = 0; i < n; i += 1) out[i] = r.stdout.readInt16LE(i * 2) / 32768;
  return out;
}

/** 按窗宽切 RMS（线性域；不做 align.js 里那步 dB 取整，避免二次损失）。 */
function windowRms(samples, window) {
  const per = Math.floor(window * RATE);
  const arr = [];
  for (let i = 0; i < samples.length; i += per) {
    const n = Math.min(per, samples.length - i);
    let sum = 0;
    for (let k = 0; k < n; k += 1) sum += samples[i + k] * samples[i + k];
    arr.push(Math.sqrt(sum / n));
  }
  return arr;
}

/** 一个文件的全部特征。静段与整体响度直接调 lib/film.js（不重写 silencedetect 的解析）。 */
function featuresOf(file) {
  const pcm = decodePcm(file);
  const win = {};
  for (const w of WINDOWS) win[w] = windowRms(pcm, w);
  const all4 = win[4];
  const prof = audioProfile(file, { noiseDb: -40, minSilence: 0.5 });
  return {
    win,
    meanRms: all4.reduce((a, b) => a + b, 0) / all4.length,
    peakRms: Math.max(...all4),
    volMeanDb: prof.meanDb,
    volMaxDb: prof.maxDb,
    silCount: prof.silences.length,
    silTotalSec: prof.silences.reduce((a, s) => a + (s.seconds ?? 0), 0),
  };
}

// —— 造三份素材：参照 + 两档有损 ——
const ref = path.join(TMP, 'ref.wav');
const a320 = path.join(TMP, 'a320.m4a');
const a128 = path.join(TMP, 'a128.m4a');
const ffmpeg = resolveBin('ffmpeg');
const steps = [
  ['-y', '-i', SRC, '-vn', '-c:a', 'pcm_s16le', ref],
  ['-y', '-i', ref, '-c:a', 'aac', '-b:a', '320k', a320],
  ['-y', '-i', ref, '-c:a', 'aac', '-b:a', '128k', a128],
];
for (const args of steps) {
  const r = run(ffmpeg, ['-hide_banner', '-loglevel', 'error', ...args]);
  if (r.code !== 0) { console.error(`ffmpeg 失败：${args.join(' ')}\n${r.stderr.slice(-300)}`); process.exit(1); }
}

const F = { ref: featuresOf(ref), a320: featuresOf(a320), a128: featuresOf(a128) };

/** 一对文件的逐特征相对差。 */
function compare(x, y) {
  const fx = F[x], fy = F[y];
  const items = [];
  for (const w of WINDOWS) {
    const a = fx.win[w], b = fy.win[w];
    let supRel = 0, sumRel = 0, maxDbD = 0;
    for (let i = 0; i < Math.min(a.length, b.length); i += 1) {
      const rd = relDiff(a[i], b[i]);
      supRel = Math.max(supRel, rd);
      sumRel += rd;
      if (a[i] > 0 && b[i] > 0) {
        const d = 20 * Math.log10(b[i] / a[i]);
        maxDbD = Math.max(maxDbD, Math.abs(d));
      }
    }
    items.push({ feature: `A 窗口RMS w=${w}s`, supRel, meanRel: sumRel / a.length, maxDbDelta: maxDbD, n: a.length });
  }
  items.push({ feature: 'B 平均窗RMS', supRel: relDiff(fx.meanRms, fy.meanRms) });
  items.push({ feature: 'C 峰值窗RMS', supRel: relDiff(fx.peakRms, fy.peakRms) });
  items.push({ feature: 'D mean_volume', supRel: relDiff(toLinearDb(fx.volMeanDb), toLinearDb(fy.volMeanDb)), dbDelta: (fy.volMeanDb - fx.volMeanDb) });
  items.push({ feature: 'D max_volume', supRel: relDiff(toLinearDb(fx.volMaxDb), toLinearDb(fy.volMaxDb)), dbDelta: (fy.volMaxDb - fx.volMaxDb) });
  items.push({ feature: 'E 静段条数', supRel: relDiff(fx.silCount, fy.silCount), x: fx.silCount, y: fy.silCount });
  items.push({ feature: 'E 静段总时长', supRel: relDiff(fx.silTotalSec, fy.silTotalSec), xSec: +fx.silTotalSec.toFixed(1), ySec: +fy.silTotalSec.toFixed(1) });
  const sup = Math.max(...items.map((i) => i.supRel));
  return { pair: `${x} → ${y}`, items, sup, rhoTol: 1 - sup };
}

const pairs = [compare('ref', 'a320'), compare('ref', 'a128'), compare('a320', 'a128')];
const out = {
  date: new Date().toISOString().slice(0, 10),
  source: path.basename(SRC),
  caliber: { ref: 'pcm_s16le 位精确提取', enc: 'AAC-LC 320k/128k，保持源率与声道', frames: 'lib/align.js 帧算子 8kHz 单声道线性域', windows: WINDOWS, eps: EPS, note: '源若已有损（B站 AAC ~190k），测的是再压一道的增量损失' },
  pairs,
};
const outFile = path.join(OUTDIR, `rtol-${out.date}.json`);
fs.writeFileSync(outFile, JSON.stringify(out, null, 2), 'utf8');
fs.rmSync(TMP, { recursive: true, force: true }); // 中间媒体文件删掉，不在 .dsh 留东西

const fmt = (x, d = 4) => (x == null || Number.isNaN(x) ? '—' : x.toFixed(d));

for (const p of pairs) {
  console.log(`\n=== ${p.pair}   ρ̂_tol = ${fmt(p.rhoTol)}（sup 相对差 ${fmt(p.sup)}）===`);
  for (const it of p.items) {
    const win = it.meanRel == null ? '' : `（均值 ${fmt(it.meanRel)}，窗内最大 Δ ${fmt(it.maxDbDelta, 2)} dB，n=${it.n}）`;
    const extra = it.dbDelta != null ? `  Δ=${fmt(it.dbDelta, 2)} dB` : it.x != null ? `  ${it.x}→${it.y}` : it.xSec != null ? `  ${it.xSec}s→${it.ySec}s` : '';
    console.log(`  ${it.feature.padEnd(18)} relDiff ${fmt(it.supRel)}${win}${extra}`);
  }
}
console.log(`\n产物：${outFile}`);
