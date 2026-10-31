#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 素材预检：在跑正式实验之前，先算定音率，不够就不跑。
#
# 为什么要有这一步：2026-10-31 那次 6 支片定音率只有 0.22，跑完才发现
# 20 个塌事件一条都判不了。同样的时间可以在开跑前 30 秒内知道。
#
# 抽样方式（v2，为长片改）：
#   只取开头会误判 —— 访谈/纪录片开头常有片头音乐。改为全片等间隔取 SEG_N 段，
#   每段 SEG_SEC 秒，避开首尾 5%，报「均值 / 最低段」。
#   判读看均值，但最低段 < 0.2 要单独说明（说明片里有一段几乎无人声）。
#
# 门槛（写死，不许看完结果再改）：
#   voiced_mean ≥ 0.60 → 可以跑
#   0.40–0.60          → 边缘，跑了也只能当探索，判读标 gray
#   < 0.40             → 不跑，换素材
#
# 口径与 run_f0_valence.py 默认一致：16kHz、hop 160(10ms)、librosa pyin(fmin 65 / fmax 500)。
# 为什么不用 crepe：2026-10-31 实测同一段访谈，crepe periodicity 只有 7.0%，
# 放大 16 倍无变化（排除电平），而 pyin 给出 70.3% / 166.7Hz。crepe 训练集以歌唱/乐器为主，
# 对纯说话声系统性偏低。两种 meter 的数值不可比。
#
# 用法：python3 precheck.py --media ../media [--device cpu]
import argparse
import subprocess
import sys
from pathlib import Path

import numpy as np

SEG_N = 4
SEG_SEC = 30
RATE = 16000
HOP = 160
VOICED_CONF = 0.5
GATE_OK = 0.60
GATE_EDGE = 0.40


def duration(path):
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(path)], capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except (ValueError, AttributeError):
        return None


def segments(dur):
    """全片等间隔取 SEG_N 段，避开首尾 5%；短片则退化为整片。"""
    if not dur or dur <= 0:
        return [(0.0, SEG_SEC * SEG_N)]
    lo, hi = dur * 0.05, dur * 0.95
    if hi - lo <= SEG_SEC:
        return [(lo, max(1.0, hi - lo))]
    if hi - lo < SEG_SEC * SEG_N:
        step = (hi - lo - SEG_SEC) / max(1, SEG_N - 1)
        return [(lo + i * step, SEG_SEC) for i in range(SEG_N)]
    step = (hi - lo - SEG_SEC) / (SEG_N - 1)
    return [(lo + i * step, SEG_SEC) for i in range(SEG_N)]


def decode(path, start, sec):
    r = subprocess.run(
        ["ffmpeg", "-hide_banner", "-loglevel", "error", "-ss", str(start),
         "-t", str(sec), "-i", str(path), "-vn", "-ac", "1", "-ar", str(RATE),
         "-f", "s16le", "-"], capture_output=True)
    if r.returncode != 0 or not r.stdout:
        return None
    return np.frombuffer(r.stdout, dtype=np.int16).astype(np.float32) / 32768.0


def voiced_ratio(x, device=None):
    """pyin 判有音高 —— 与正式实验默认口径一致。device 保留仅为调用兼容，pyin 走 CPU。"""
    import librosa
    _, vflag, _ = librosa.pyin(x, fmin=65, fmax=500, sr=RATE, hop_length=HOP)
    return float(np.mean(vflag))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--media", required=True, type=Path)
    ap.add_argument("--device", default="cuda")
    args = ap.parse_args()

    files = sorted([p for p in args.media.iterdir()
                    if p.suffix.lower() in (".mp4", ".mkv", ".mov", ".wav", ".m4a", ".flac")])
    if not files:
        print(f"没有可读素材：{args.media}", file=sys.stderr)
        return 1

    for p in files:
        dur = duration(p)
        segs = segments(dur)
        print(f"\n{p.name}  时长 {'%.1f min' % (dur / 60) if dur else '未知'}"
              f"  抽样 {len(segs)} 段 × {SEG_SEC}s")
        vals = []
        for start, sec in segs:
            x = decode(p, start, sec)
            if x is None or x.size == 0:
                print(f"  @{start:6.0f}s  解码失败")
                continue
            v = voiced_ratio(x, args.device)
            vals.append(v)
            print(f"  @{start:6.0f}s  voiced={v:.2f}")
        if not vals:
            print("  无有效段")
            continue
        mean, lo = float(np.mean(vals)), float(np.min(vals))
        verdict = ("可跑" if mean >= GATE_OK
                   else "边缘（只作探索）" if mean >= GATE_EDGE
                   else "不跑，换素材")
        print(f"  → 均值 {mean:.2f} / 最低 {lo:.2f}  【{verdict}】"
              + ("  ⚠ 有一段几乎无人声" if lo < 0.2 else ""))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
