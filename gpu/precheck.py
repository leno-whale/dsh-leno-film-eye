#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 素材预检：在跑正式实验之前，先算每支片的定音率，不够就不跑。
#
# 为什么要有这一步：2026-10-31 那次 6 支片定音率只有 0.22，跑完才发现
# 20 个塌事件一条都判不了。同样的时间可以在开跑前 30 秒内知道。
#
# 门槛（写死，不许看完结果再改）：
#   voiced_mean ≥ 0.60 → 可以跑
#   0.40–0.60          → 边缘，跑了也只能当探索，判读标 gray
#   < 0.40             → 不跑，换素材
#
# 口径与 run_f0_valence.py 完全一致：16kHz、hop 160(10ms)、torchcrepe full、conf>0.5。
# 只取前 PRE_SEC 秒（默认 90），足够估比例，不必整片解码。
#
# 用法：python3 precheck.py --media ../media [--device cpu]
import argparse
import subprocess
import sys
from pathlib import Path

import numpy as np

PRE_SEC = 90
RATE = 16000
HOP = 160
VOICED_CONF = 0.5
GATE_OK = 0.60
GATE_EDGE = 0.40


def decode(path, sec):
    r = subprocess.run(
        ["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(path),
         "-t", str(sec), "-vn", "-ac", "1", "-ar", str(RATE), "-f", "s16le", "-"],
        capture_output=True)
    if r.returncode != 0 or not r.stdout:
        return None
    return np.frombuffer(r.stdout, dtype=np.int16).astype(np.float32) / 32768.0


def voiced_ratio(x, device):
    import torch
    import torchcrepe
    t = torch.from_numpy(x).unsqueeze(0)
    _, conf = torchcrepe.predict(
        t, RATE, hop_length=HOP, batch_size=128, device=device,
        model="full", return_periodicity=True)
    return float((conf > VOICED_CONF).float().mean())


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

    print(f"{'文件':34s} {'前90s定音率':>10s}  判读")
    results = []
    for p in files:
        x = decode(p, PRE_SEC)
        if x is None or x.size == 0:
            print(f"{p.name[:34]:34s} {'—':>10s}  无音轨/解码失败")
            continue
        v = voiced_ratio(x, args.device)
        verdict = ("可跑" if v >= GATE_OK
                   else "边缘（只作探索）" if v >= GATE_EDGE
                   else "不跑，换素材")
        results.append((p.name, v))
        print(f"{p.name[:34]:34s} {v:10.2f}  {verdict}")

    if results:
        ok = [r for r in results if r[1] >= GATE_OK]
        print(f"\n达标 {len(ok)}/{len(results)}（门槛 {GATE_OK}）")
        if not ok:
            print("没有一支过门槛 —— 别跑正式实验，换素材。")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
