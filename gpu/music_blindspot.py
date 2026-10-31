#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MV/音乐侧盲区：6 dB 塌事件在「音乐段 / 非音乐段」的塌→沉共现率。
#
# 判读先写死（docs/theory/F0与valence旁证-交接.md §3.8）：
#   段分类只看 f0/voiced，不看 db、不看 sink：
#     有调性窗 ⇔ voiced ≥ 0.5 且 f0_iqr ≤ 1.0 半音；
#     连续 ≥3 个有调性窗 = 音乐段，其余 = 非音乐段。
#   事件仍是 6 dB、沉仍是降 ≥1 半音且 |Δst| ≤ 12；两段 p 不相加。
#   有调性窗 <60 → 无法分段；任一段可判 <20 → 该段 insufficient。
#   若两段 Δst 中位数差 <1 半音，说明分类没分开，分段读数作废。
#
# 只读 window.tsv，不需要 torch。用法：python3 music_blindspot.py --out ../out-mv-pyin
import argparse
import sys
from pathlib import Path

import numpy as np

WINDOW = 4.0
DROP_DB = -6.0
TONE_VOICED = 0.5
TONE_IQR = 1.0
MIN_RUN = 3
MIN_TONAL = 60
MIN_DECIDED = 20


def load(path):
    lines = [l for l in path.read_text(encoding="utf-8").splitlines() if l]
    head = lines[0].split("\t")
    return [dict(zip(head, l.split("\t"))) for l in lines[1:] if len(l.split("\t")) == len(head)]


def num(row, key):
    s = row.get(key, "")
    return float(s) if s else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    files = sorted(args.out.glob("*.window.tsv"))
    if not files:
        print(f"没有 window.tsv：{args.out}", file=sys.stderr)
        return 1

    rows_by_file = {}
    tonal_total = wins_total = 0
    for f in files:
        rows = load(f)
        rows_by_file[f] = rows
        wins_total += len(rows)
        for r in rows:
            v, q = num(r, "voiced"), num(r, "f0_iqr_st")
            if v is not None and q is not None and v >= TONE_VOICED and q <= TONE_IQR:
                tonal_total += 1

    if tonal_total < MIN_TONAL:
        print(f"有调性窗 {tonal_total}/{wins_total} < {MIN_TONAL} → insufficient："
              f"这批素材不是音乐为主，分段比较做不了。")
        return 0

    print(f"窗 {wins_total}，有调性窗 {tonal_total}（{tonal_total / wins_total:.2f}）")
    print(f"{'片':24s}{'窗':>5s}{'有调性':>7s}{'音乐段窗':>9s}")

    buckets = {"music": [], "other": []}
    for f, rows in rows_by_file.items():
        tonal = [bool((num(r, "voiced") or 0) >= TONE_VOICED and
                      (num(r, "f0_iqr_st") is not None) and num(r, "f0_iqr_st") <= TONE_IQR)
                 for r in rows]
        music = [False] * len(rows)
        i = 0
        while i < len(tonal):
            if tonal[i]:
                j = i
                while j < len(tonal) and tonal[j]:
                    j += 1
                if j - i >= MIN_RUN:
                    for k in range(i, j):
                        music[k] = True
                i = j
            else:
                i += 1
        print(f"{f.name[:24]:24s}{len(rows):5d}{sum(tonal):7d}{sum(music):9d}")

        # 事件：按「跌后的窗」归段（段由 f0 定，事件由 db 定，互不借用）
        for k in range(1, len(rows)):
            d0, d1 = num(rows[k - 1], "db"), num(rows[k], "db")
            if d0 is None or d1 is None or d1 - d0 > DROP_DB:
                continue
            a, b = num(rows[k - 1], "f0_med_st"), num(rows[k], "f0_med_st")
            dec = a is not None and b is not None
            dst = (b - a) if dec else float("nan")
            if dec and abs(dst) > 12:
                dec = False
            buckets["music" if music[k] else "other"].append(
                {"dec": dec, "sink": bool(dec and dst <= -1),
                 "dst": dst if dec else float("nan")})

    print()
    meds = {}
    for name, label in (("music", "音乐段"), ("other", "非音乐段")):
        ev = buckets[name]
        dec = [e for e in ev if e["dec"]]
        sinks = [e for e in dec if e["sink"]]
        p = (len(sinks) / len(dec)) if dec else float("nan")
        print(f"{label}：事件 {len(ev)}，可判 {len(dec)}，沉 {len(sinks)}，p={p:.2f}")
        if dec:
            meds[name] = float(np.median([e["dst"] for e in dec]))
        if len(dec) < MIN_DECIDED:
            print(f"  → insufficient：可判 {len(dec)} < {MIN_DECIDED}，p 不采信")

    if "music" in meds and "other" in meds:
        gap = abs(meds["music"] - meds["other"])
        print(f"\n分类检验：Δst 中位 音乐 {meds['music']:.1f} / 非音乐 {meds['other']:.1f} "
              f"半音，差 {gap:.1f}")
        if gap < 1.0:
            print("  → 差 <1 半音：分类没分开，分段读数作废（§3.8 第 3 条）。")
    print("\n两段 p 不相加；阈值与沉的定义未改。")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
