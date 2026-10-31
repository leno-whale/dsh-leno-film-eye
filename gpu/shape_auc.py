#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 命题 6a 的可恢复性检验：用强度轨迹形态 Φ 预测「塌是否伴随沉」。
#
# 依据 docs/theory/命题6-可恢复性提案.md：
#   Φ = (T_t^-, D, L_0) = (跌速 dB/s, 跌倒深度 dB, 跌前窗强度 dB)
#   sink = 1 当且仅当 f0 中位半音相对上一窗降 ≥1 且 |Δ| ≤ 12（剔除八度误判）
#   AUC ≈ 0.5 → π_noF0 对沉完全盲（命题 6 加强）
#   AUC > 0.5 → 部分可恢复，恢复上界即 AUC（命题 6 弱化为「不可直接识别」）
#
# 只读 window.tsv，不重跑任何模型；不需要 torch。
# 用法：python3 shape_auc.py [--out ../out]
import argparse
import sys
from pathlib import Path

import numpy as np

WINDOW = 4.0
DROP_DB = -6.0        # 塌阈值，先写死，不许为 AUC 好看去动
SINK_ST = -1.0        # 降 ≥1 半音算沉
OCTAVE_ST = 12.0      # |Δ| > 12 视为八度误判


def auc(scores, labels):
    """单变量 AUC（Mann–Whitney），正类分数越高越像 sink。"""
    pos = [s for s, y in zip(scores, labels) if y]
    neg = [s for s, y in zip(scores, labels) if not y]
    if not pos or not neg:
        return None
    wins = 0.0
    for p in pos:
        for q in neg:
            wins += 1.0 if p > q else (0.5 if p == q else 0.0)
    return wins / (len(pos) * len(neg))


def load_rows(path):
    lines = [l for l in path.read_text(encoding="utf-8").splitlines() if l]
    head = lines[0].split("\t")
    out = []
    for line in lines[1:]:
        cells = line.split("\t")
        if len(cells) != len(head):
            continue
        out.append(dict(zip(head, cells)))
    return out


def events_of(rows):
    """重建塌事件，返回 Φ 与 sink；不可判的 with_sink=None。"""
    ev = []
    for i in range(1, len(rows)):
        db0 = rows[i - 1].get("db", "")
        db1 = rows[i].get("db", "")
        if not db0 or not db1:
            continue
        drop = float(db1) - float(db0)
        if drop > DROP_DB:
            continue
        f0a = rows[i - 1].get("f0_med_st", "")
        f0b = rows[i].get("f0_med_st", "")
        decidable = bool(f0a) and bool(f0b)
        dst = (float(f0b) - float(f0a)) if decidable else float("nan")
        if decidable and abs(dst) > OCTAVE_ST:
            decidable = False
        ev.append({
            "t": float(rows[i].get("t") or 0),
            "slope": round(drop / WINDOW, 2),   # T_t^-
            "depth": round(-drop, 1),           # D
            "l0": round(float(db0), 1),         # L_0
            "sink": bool(decidable and dst <= SINK_ST),
            "decidable": decidable,
        })
    return ev


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=Path(__file__).parent / "out-2026-10-31")
    args = ap.parse_args()

    files = sorted(args.out.glob("*.window.tsv"))
    if not files:
        print(f"没有 window.tsv：{args.out}", file=sys.stderr)
        return 1

    all_ev = []
    print(f"{'片':24s} {'窗':>4s} {'塌':>3s} {'可判':>4s} {'沉':>3s}")
    for f in files:
        rows = load_rows(f)
        ev = events_of(rows)
        dec = [e for e in ev if e["decidable"]]
        sinks = [e for e in dec if e["sink"]]
        print(f"{f.name[:24]:24s} {len(rows):4d} {len(ev):3d} {len(dec):4d} {len(sinks):3d}")
        all_ev.extend(ev)

    dec = [e for e in all_ev if e["decidable"]]
    print(f"\n合计：塌 {len(all_ev)}，可判 {len(dec)}，"
          f"不可判 {len(all_ev) - len(dec)}，沉 {sum(e['sink'] for e in dec)}")

    if len(dec) < 2 or len({e["sink"] for e in dec}) < 2:
        print("\nAUC：undefined —— 可判样本里没有正负两类，算不了。")
        print("（这正是本次的处境：不是「盲区小」，是没有样本。）")
        return 0

    labels = [e["sink"] for e in dec]
    for key, desc in (("slope", "T_t^- 跌速 dB/s"), ("depth", "D 跌倒深度 dB"), ("l0", "L_0 跌前强度 dB")):
        a = auc([e[key] for e in dec], labels)
        print(f"AUC[{desc:20s}] = {a:.3f}" if a is not None else f"AUC[{desc}] = undefined")

    print("\n判读：CI 含 0.5 → 完全盲；显著 > 0.5 → 部分可恢复（上界即 AUC）。")
    print("注意：未按 L_0 分层；分层前的结果不得当结论（见提案 §四.2）。")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
