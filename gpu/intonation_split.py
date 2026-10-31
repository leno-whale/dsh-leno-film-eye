#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 3 dB 事件的语调拆分：句内跌 vs 跨句跌（docs/theory/F0与valence旁证-交接.md §3.10）。
#
# 规则先写死：
#   ffmpeg silencedetect, noise=-40dB, d=0.3s（默认，不调）；
#   事件（跌后窗起点 t）若 [t-1, t+1] 与某段静音相交 → 跨句，否则句内；
#   run 的层按首个事件判定；
#   沉/可判/run 定义一律沿用；两层 p 不合并；按 run 聚类 bootstrap（1000 次）出差值 CI。
# 不改 §3.7 的任何读数。
#
# 用法：python3 intonation_split.py --media ../media --out ../out-voiceset-3db-2026-10-31
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

import numpy as np

WINDOW = 4.0
DROP_DB = -3.0
PAUSE_DB = -40
PAUSE_SEC = 0.3
WIN = 1.0            # 判定窗口 [t-1, t+1]
MIN_RUNS = 20
N_BOOT = 1000


def silences(path):
    """返回 [(start, end)]；末段没结束时 end=inf。"""
    r = subprocess.run(
        ["ffmpeg", "-nostats", "-v", "info", "-i", str(path), "-vn", "-ac", "1",
         "-ar", "8000", "-af", f"silencedetect=noise={PAUSE_DB}dB:d={PAUSE_SEC}",
         "-f", "null", "-"], capture_output=True, text=True, errors="replace")
    out, starts = [], []
    for line in r.stderr.splitlines():
        m = re.search(r"silence_start:\s*([0-9.]+)", line)
        if m:
            starts.append(float(m.group(1)))
            continue
        m = re.search(r"silence_end:\s*([0-9.]+)", line)
        if m and starts:
            out.append((starts.pop(), float(m.group(1))))
    out.extend((s, float("inf")) for s in starts)
    return out


def load_rows(path):
    lines = [l for l in path.read_text(encoding="utf-8").splitlines() if l]
    head = lines[0].split("\t")
    return [dict(zip(head, l.split("\t"))) for l in lines[1:] if len(l.split("\t")) == len(head)]


def num(row, key):
    s = row.get(key, "")
    return float(s) if s else None


def wilson(k, n, z=1.959963984540054):
    if n == 0:
        return float("nan"), float("nan")
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return max(0.0, c - h), min(1.0, c + h)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--media", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    cache = args.out / "silences.json"
    if cache.exists():
        sil = {k: [tuple(x) for x in v] for k, v in json.loads(cache.read_text(encoding="utf-8")).items()}
        print(f"停顿表复用 {cache}")
    else:
        sil = {}
        for p in sorted(args.media.iterdir()):
            if p.suffix.lower() not in {".mp4", ".mkv", ".webm", ".flv", ".m4a", ".mp3", ".wav"}:
                continue
            sil[p.stem] = silences(p)
            print(f"  {p.name}: 静音段 {len(sil[p.stem])}")
        cache.write_text(json.dumps(sil, ensure_ascii=False), encoding="utf-8")
        print(f"停顿表 → {cache}")

    runs = {"cross": [], "within": []}   # 每个元素 = (可判?, 沉?)
    ev_total = ev_cross = 0
    for f in sorted(args.out.glob("*.window.tsv")):
        rows = load_rows(f)
        stem = f.name.replace(".window.tsv", "")
        pauses = sil.get(stem, [])
        idxs = [i for i in range(1, len(rows))
                if (num(rows[i], "db") is not None and num(rows[i - 1], "db") is not None
                    and num(rows[i], "db") - num(rows[i - 1], "db") <= DROP_DB)]
        # run 分组
        groups, cur = [], []
        for i in idxs:
            if cur and i == cur[-1] + 1:
                cur.append(i)
            else:
                if cur:
                    groups.append(cur)
                cur = [i]
        if cur:
            groups.append(cur)
        for g in groups:
            t = float(rows[g[0]]["t"])
            cross = any(s <= t + WIN and e >= t - WIN for s, e in pauses)
            dec_ev, sink_ev = 0, 0
            for i in g:
                a, b = num(rows[i - 1], "f0_med_st"), num(rows[i], "f0_med_st")
                if a is None or b is None:
                    continue
                d = b - a
                if abs(d) > 12:
                    continue
                dec_ev += 1
                sink_ev += 1 if d <= -1 else 0
            ev_total += len(g)
            ev_cross += len(g) if cross else 0
            if dec_ev == 0:
                continue
            runs["cross" if cross else "within"].append((dec_ev, sink_ev))

    print(f"\n事件 {ev_total}，其中跨句 {ev_cross}（{ev_cross / max(1, ev_total):.2f}）")
    stats = {}
    for name, label in (("cross", "跨句跌"), ("within", "句内跌")):
        R = runs[name]
        n = sum(a for a, _ in R)
        k = sum(b for _, b in R)
        p = k / n if n else float("nan")
        lo, hi = wilson(k, n)
        stats[name] = (n, k, p, R)
        print(f"{label}: run {len(R)}，可判事件 {n}，沉 {k}，p={p:.3f}，Wilson [{lo:.2f}, {hi:.2f}]")
        if len(R) < MIN_RUNS:
            print(f"  → insufficient：run {len(R)} < {MIN_RUNS}")

    if len(runs["cross"]) >= MIN_RUNS and len(runs["within"]) >= MIN_RUNS:
        rng = np.random.default_rng(0)
        diffs = []
        for _ in range(N_BOOT):
            ps = {}
            for name in ("cross", "within"):
                R = runs[name]
                pick = [R[j] for j in rng.integers(0, len(R), len(R))]
                dsum = sum(a for a, _ in pick)
                ps[name] = (sum(b for _, b in pick) / dsum) if dsum else np.nan
            diffs.append(ps["cross"] - ps["within"])
        lo, hi = np.nanpercentile(diffs, [2.5, 97.5])
        print(f"\n差值（跨句 − 句内）= {stats['cross'][2] - stats['within'][2]:+.3f}，"
              f"cluster bootstrap 95% = [{lo:+.3f}, {hi:+.3f}]")
        if lo > 0:
            print("判读：差值 CI 不含 0 且跨句更高 → 0.59 主要由非表达性下降驱动。")
        elif hi < 0:
            print("判读：跨句反而更低 —— 语调解释反了，先查停顿检测与窗口对齐。")
        else:
            print("判读：差值 CI 含 0 → 不能说语调解释了 0.59。")
    else:
        print("\n两层 run 有一层 <20，不做差值检验。")
    print("\n两层 p 不合并；§3.7 的 0.592 不变。")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
