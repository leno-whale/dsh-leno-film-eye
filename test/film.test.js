import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

import { has, run, resolveBin, probeDuration } from '../lib/ff.js';
import { sheets, audioProfile, shots } from '../lib/film.js';
import { align } from '../lib/align.js';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const TMP = path.join(HERE, '..', '.tmp-test');
const SAMPLE = path.join(TMP, 'sample.mp4');

const ffmpegOk = has('ffmpeg') && has('ffprobe');
const skip = ffmpegOk ? false : `ffmpeg 不可用（解析到 ${resolveBin('ffmpeg')}）`;

function makeSample() {
  fs.mkdirSync(TMP, { recursive: true });
  // 6 秒：前 2 秒有声音，后 4 秒静音（apad 补齐，别用 -shortest——那会把整段截成 2 秒）；
  // 画面用 testsrc2（一直在动，能测出抽帧与镜头）
  const r = run('ffmpeg', [
    '-hide_banner', '-loglevel', 'error', '-y',
    '-f', 'lavfi', '-i', 'testsrc2=size=320x240:rate=10:duration=6',
    '-f', 'lavfi', '-i', 'sine=frequency=440:duration=2',
    '-af', 'apad',
    '-t', '6', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-c:a', 'aac',
    SAMPLE,
  ]);
  if (r.code !== 0) throw new Error(`造样片失败：${r.stderr.split('\n').filter(Boolean).slice(-2).join(' / ')}`);
}

test('能解析到 ffmpeg/ffprobe，并能读到时长', { skip }, () => {
  makeSample();
  const d = probeDuration(SAMPLE);
  assert.ok(d && d > 5 && d < 7, `时长应约 6 秒，实际 ${d}`);
});

test('film_sheets：九张拼一页，出图且能打开', { skip }, () => {
  makeSample();
  const outDir = path.join(TMP, 'sheets');
  fs.rmSync(outDir, { recursive: true, force: true });
  const r = sheets(SAMPLE, { interval: 1, max: 1, outDir });
  assert.equal(r.ok, true, r.error);
  assert.equal(r.count, 1, '6 秒 / 每 1 秒 → 一页九格够用');
  const size = fs.statSync(r.files[0]).size;
  assert.ok(size > 1000, `拼图应该是有效 JPEG，实际 ${size} 字节`);
});

test('film_audio：静音段能数出来（前 2 秒有声，后 4 秒静）', { skip }, () => {
  makeSample();
  const r = audioProfile(SAMPLE, { minSilence: 0.5 });
  assert.equal(r.ok, true, r.error);
  assert.ok(r.meanDb !== null, '要读到平均音量');
  assert.equal(r.silences.length >= 1, true, `应至少一段静音，实际 ${r.silences.length}`);
  assert.ok(r.silences[0].start >= 1.5, `静音应从 2 秒附近开始，实际 ${r.silences[0].start}`);
});

test('film_shots：镜头数与平均时长算得出来', { skip }, () => {
  makeSample();
  const r = shots(SAMPLE, { threshold: 0.3 });
  assert.equal(r.ok, true, r.error);
  assert.ok(r.shotCount >= 1, '至少一个镜头');
  assert.ok(r.duration > 5, `时长应约 6 秒，实际 ${r.duration}`);
  assert.equal(typeof r.cutsPerMinute, 'number');
});

test('film_align：时间/音量/切点/帧对齐，且能看出尾巴静音', { skip }, async () => {
  makeSample();
  const outDir = path.join(TMP, 'align');
  fs.rmSync(outDir, { recursive: true, force: true });
  const r = await align(SAMPLE, { interval: 1, outDir });
  assert.equal(r.ok, true, r.error);
  // 6 秒 / 每 1 秒 → 约 6 行（末行可能因取整多一格）
  assert.ok(r.rows.length >= 5 && r.rows.length <= 7, `行数应约 6，实际 ${r.rows.length}`);
  assert.equal(typeof r.rows[0].db, 'number', '每行都要有音量');
  assert.equal(r.frames.length, r.rows.length, '帧数应与行数一致');
  assert.equal(r.silentTail, true, '样片后 4 秒是静音，尾巴应判为静音');
  assert.ok(fs.existsSync(outDir + path.sep + 'align.tsv'), 'align.tsv 要落盘');
  const tsv = fs.readFileSync(outDir + path.sep + 'align.tsv', 'utf8').trim().split('\n');
  assert.equal(tsv[0], 't\tdb\tcut\tframe', 'TSV 表头固定');
  assert.equal(tsv.length, r.rows.length + 1);
});

test('文件不存在时给出可读错误，不抛异常', () => {
  const r = sheets(path.join(TMP, 'nope.mp4'));
  assert.equal(r.ok, false);
  assert.match(r.error, /读不到时长|不存在/);
});
