#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MV 试点：db 仍取原混音（塌是混音级事件），F0 取 demucs 分离出的 vocals 轨。
# 尺子标签 demucs+pyin，与 pyin/crepe 分表（docs/theory/F0与valence旁证-交接.md §3.9）。
#
# 这是一条**混合前端**，不许拿 vocals.wav 去算 db——那会把「塌」的定义改掉。
# fmax=1000 是开跑前按歌唱音域定的（说话用的 500 会削掉女声高音）。
#
# 用法：python3 demucs_pilot.py --media ../x.mp4 --vocals ../htdemucs/x/vocals.wav --out ../out-mv-demucs
import argparse
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
import run_f0_valence as R  # noqa: E402

F0_FMAX = 1000.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--media", required=True, type=Path)
    ap.add_argument("--vocals", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    import librosa

    db = R.window_db(R.ffmpeg_decode(args.media, R.RATE), R.RATE, R.WINDOW)
    audio = R.ffmpeg_decode(args.vocals, R.F0_RATE)
    f0, _, _ = librosa.pyin(audio, fmin=65, fmax=F0_FMAX, sr=R.F0_RATE,
                            hop_length=R.F0_HOP)
    f0 = np.asarray(f0, dtype=float)
    fw = R.f0_windows(f0)
    print(f"    F0: demucs+pyin（vocals，fmin 65 / fmax {F0_FMAX:g}）")

    n = min(len(db), len(fw))
    ts = np.arange(n) * R.WINDOW
    rows = []
    for i in range(n):
        st, iqr, slope, voiced = fw[i]
        rows.append({"t": float(ts[i]), "db": float(db[i]),
                     "f0_med_st": round(st, 2) if st == st else None,
                     "f0_iqr_st": round(iqr, 2) if iqr == iqr else None,
                     "f0_slope_st_s": round(slope, 3) if slope == slope else None,
                     "voiced": round(voiced, 2) if voiced == voiced else None,
                     "m_arousal": None, "m_valence": None})

    stem = args.out / args.media.stem
    stem.with_suffix(".window.tsv").write_text(
        "\t".join(rows[0].keys()) + "\n" +
        "\n".join("\t".join("" if v is None else str(v) for v in r.values()) for r in rows) + "\n",
        encoding="utf-8")

    events = []
    for i in range(1, n):
        if db[i] - db[i - 1] > R.DROP_DB:
            continue
        a, b = fw[i - 1][0], fw[i][0]
        dec = a == a and b == b
        dst = (b - a) if dec else float("nan")
        if dec and abs(dst) > 12:
            dec = False
        events.append({"t": float(ts[i]), "drop_db": round(float(db[i] - db[i - 1]), 1),
                       "f0_delta_st": round(dst, 2) if dec else None,
                       "with_sink": bool(dst <= -1) if dec else None})
    stem.with_suffix(".events.tsv").write_text(json.dumps(events, ensure_ascii=False, indent=1),
                                               encoding="utf-8")

    v = [r["voiced"] for r in rows if r["voiced"] is not None]
    q = [r["f0_iqr_st"] for r in rows if r["f0_iqr_st"] is not None]
    dec = [e for e in events if e["with_sink"] is not None]
    print(f"    窗 {n}；有音高窗 {len(v)}；voiced 均值 {np.mean(v) if v else 0:.2f}；"
          f"窗内 IQR 中位 {np.median(q) if q else float('nan'):.2f}")
    print(f"    6 dB 事件 {len(events)}；可判 {len(dec)}；沉 {sum(e['with_sink'] for e in dec)}")
    print(f"    → {stem.with_suffix('.window.tsv')}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
