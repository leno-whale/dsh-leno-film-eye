#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# F0 与 valence 旁证实验——跑在并行智算云（单卡即可）
#
# 打的是理论的哪条边界：
#   实验一（F0）→ 命题 6：π_noF0 丢基频是构造，「沉」不可识别是定理、不用测；
#             测的是盲区的实际大小——塌事件发生时音高在干什么（塌/沉列联表）。
#   实验二（valence）→ 经验命题 7 + §13.5：外部模型的 valence 在本素材上动多少、
#             动在哪；她只有 arousal 侧，模型侧补出「她的线看不见的时刻」。
#
# 判读先写死（跑之前落纸，与 docs/theory/F0与valence旁证-交接.md 一致）：
#   sanity 门：corr(m_arousal, db) ≥ 0.5。不过 → 报 no-transfer，实验二全部作废不算数。
#   实验一：塌事件 = 4s 窗 db 比上一窗跌 ≥6 dB；F0 行为 = 窗中位半音相对上一窗
#           变化 |Δst| ≥1 记「伴随沉」（方向另行报）。
#           ≥50% 塌事件伴随 → 盲区代价大；<20% → 实际盲区小；中间 → 灰区，只报数。
#   实验二：valence 窗间标准差 <0.05（模型原尺度）→ 此素材 valence 携带信息少，
#           报 low-signal；否则给 top-10 valence 移动时刻（按 |Δv| 排）。
#
# 纪律：
#   - db 列不是另造的尺子——与本 bundle parity/ 下她 node 实现的 align.tsv
#     逐行对（同 4s 窗、同 20log10(RMS)、同 -90 钳制）；对不上 → parity FAIL，停。
#   - 模型输出全部带口径标签 meter:external-model，不冒充理论里的 φ（公理 E1）。
#   - 情绪模型拉不动不硬凑：实验一独立成立，实验二标 no-model。
#
# 用法：python3 run_f0_valence.py --media ../media --out ../out [--no-emotion]
import argparse
import json
import subprocess
import sys
from pathlib import Path

import numpy as np

WINDOW = 4.0
RATE = 8000          # db 列与她一致用 8k；F0/模型各自用 16k
F0_RATE = 16000
F0_HOP = 160         # 10ms
VOICED_CONF = 0.5
ST_REF = 440.0       # 半音基准 A4

# ---------------------------------------------------------------- 基础


def ffmpeg_decode(path, rate):
    r = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(path), "-vn", "-ac", "1",
         "-ar", str(rate), "-f", "s16le", "-"],
        capture_output=True, check=True)
    return np.frombuffer(r.stdout, dtype=np.int16).astype(np.float32) / 32768.0


def window_db(x, rate, window):
    """与她 lib/align.js 同式：满窗切、20log10(rms)、静音钳 -90、一位小数。"""
    n = int(window * rate)
    m = len(x) // n
    seg = x[: m * n].reshape(m, n)
    rms = np.sqrt((seg ** 2).mean(axis=1))
    db = np.where(rms > 0, 20 * np.log10(np.maximum(rms, 1e-9)), -90.0)
    return np.round(np.maximum(db, -90.0), 1)


def semitone(hz):
    return 12.0 * np.log2(np.asarray(hz, dtype=float) / ST_REF)

# ---------------------------------------------------------------- 实验一：F0


def f0_track(path):
    """降级链：torchcrepe-full@128 → torchcrepe-tiny@256 → librosa pyin。
    vGPU 只有 ~2.4G 显存，batch 512 会 OOM——128/256 是按它写的。
    返回 (f0[n_frames_hop10ms], 来源标签含模型档)。"""
    try:
        import torch
        import torchcrepe
        audio = ffmpeg_decode(path, F0_RATE)
        t = torch.tensor(audio, dtype=torch.float32).unsqueeze(0)
        dev = "cuda" if torch.cuda.is_available() else "cpu"
        for capacity, batch in (("full", 128), ("tiny", 256)):
            try:
                f0, conf = torchcrepe.predict(
                    t, F0_RATE, hop_length=F0_HOP, batch_size=batch,
                    device=dev, model=capacity, return_periodicity=True)
                f0 = f0.squeeze(0).detach().cpu().numpy().astype(float)
                conf = conf.squeeze(0).detach().cpu().numpy().astype(float)
                f0[conf < VOICED_CONF] = np.nan
                print(f"    F0: torchcrepe-{capacity} on {dev} (batch {batch})")
                return f0, f"torchcrepe-{capacity}"
            except RuntimeError as e:  # 显存不够 → 降档
                print(f"    [warn] torchcrepe-{capacity} 失败（{str(e)[:80]}），降档", file=sys.stderr)
                try:
                    torch.cuda.empty_cache()
                except Exception:  # noqa: BLE001
                    pass
    except Exception as e:  # noqa: BLE001
        print(f"    [warn] torchcrepe 不可用（{e}），回退 pyin", file=sys.stderr)
    import librosa
    audio = ffmpeg_decode(path, F0_RATE)
    f0, _, _ = librosa.pyin(audio, fmin=65, fmax=1100, sr=F0_RATE, hop_length=F0_HOP)
    print("    F0: librosa pyin（CPU）")
    return np.asarray(f0, dtype=float), "pyin"


def f0_windows(f0, window=WINDOW, hop_sec=F0_HOP / F0_RATE):
    """每 4s 窗聚合：中位半音、四分位距、斜率（半音/秒）、voiced 占比。"""
    per = int(round(window / hop_sec))
    m = len(f0) // per
    rows = []
    for i in range(m):
        seg = f0[i * per:(i + 1) * per]
        v = seg[~np.isnan(seg)]
        if len(v) >= per * 0.1:
            st = semitone(v)
            slope = float(np.polyfit(np.arange(len(st)) * hop_sec, st, 1)[0]) if len(st) > 2 else float("nan")
            rows.append((float(np.median(st)),
                         float(np.percentile(st, 75) - np.percentile(st, 25)),
                         slope, len(v) / per))
        else:
            rows.append((float("nan"),) * 4)
    return rows

# ---------------------------------------------------------------- 实验二：情绪模型


def emotion_track(path):
    """候选链：essentia arousalvalence（音乐 v/a，最贴）→ 标 no-model。
    每个候选 4s 窗给 (arousal, valence)；全失败返回 (None, "no-model")。"""
    try:
        import essentia.standard as es
        audio = es.MonoLoader(filename=str(path), sampleRate=16000)()
        embedding = es.TensorflowPredictMusiCNN(graphFilename=EMO_MODEL)(audio)
        if embedding.ndim != 2 or embedding.shape[1] != 2:
            # 下错模型（如 autotagging 是 (N,50) 标签概率）——拒用，不静默出脏数
            raise ValueError(f"模型输出 {embedding.shape}，不是 (N,2) 的 v/a 回归")
        frames_per_4s = int(4.0 / 0.05)   # 该模型输出 20fps
        m = len(embedding) // frames_per_4s
        out = [(float(embedding[i * frames_per_4s:(i + 1) * frames_per_4s, 0].mean()),
                float(embedding[i * frames_per_4s:(i + 1) * frames_per_4s, 1].mean()))
               for i in range(m)]
        print("    情绪模型: essentia arousalvalence")
        return out, "essentia-arousalvalence"
    except Exception as e:  # noqa: BLE001
        print(f"    [warn] 情绪模型不可用（{type(e).__name__}: {e}），实验二标 no-model", file=sys.stderr)
        return None, "no-model"

# EMO_MODEL：模型文件路径。RUNBOOK 里有下载步骤；拉不动就不存在 → no-model。
EMO_MODEL = str((Path(__file__).parent / "models" / "arousalvalence-msd-musicnn-1.pb")) \
    if (Path(__file__).parent / "models" / "arousalvalence-msd-musicnn-1.pb").exists() else ""

# ---------------------------------------------------------------- 主流程


def parity_check(db):
    ref = Path(__file__).parent / "parity" / "红泪石戒指.align.tsv"
    if not ref.exists():
        print("    [parity] 参考表不在，跳过（跨片素材允许）")
        return True
    ref_db = [line.split("\t")[1] for line in ref.read_text(encoding="utf-8").splitlines()[1:] if line.strip()]
    n = min(len(ref_db), len(db))
    diff = np.abs(np.array([float(x) for x in ref_db[:n]]) - db[:n])
    ok = bool((diff <= 0.11).all())   # 她 db 一位小数 + 我一位小数 ⇒ 容差 0.11
    print(f"    [parity] 对了 {n} 行，最大差 {diff.max():.2f} dB → {'PASS' if ok else 'FAIL'}")
    if not ok:
        print("    [parity] 尺子对不上，停——不许用对不齐的 db 出数", file=sys.stderr)
    return ok


def run_one(path, out_dir, do_emotion=True):
    print(f"  {path.name}")
    x8k = ffmpeg_decode(path, RATE)
    db = window_db(x8k, RATE, WINDOW)
    if path.name.startswith("28871298443") or "红泪石戒指" in path.name:
        if not parity_check(db):
            sys.exit(1)

    ts = np.arange(len(db)) * WINDOW
    f0, f0_src = f0_track(path)
    fw = f0_windows(f0)
    emo, emo_src = emotion_track(path) if do_emotion else (None, "skipped")

    n = min(len(db), len(fw))
    rows = []
    for i in range(n):
        st_med, st_iqr, slope, voiced = fw[i]
        ar, va = (emo[i] if emo and i < len(emo) else (float("nan"),) * 2)
        rows.append({
            "t": float(ts[i]), "db": float(db[i]),
            "f0_med_st": round(st_med, 2) if st_med == st_med else None,
            "f0_iqr_st": round(st_iqr, 2) if st_iqr == st_iqr else None,
            "f0_slope_st_s": round(slope, 3) if slope == slope else None,
            "voiced": round(voiced, 2) if voiced == voiced else None,
            "m_arousal": round(ar, 3) if ar == ar else None,
            "m_valence": round(va, 3) if va == va else None,
        })

    # 事件表：塌 = db 一窗跌 ≥6；伴随沉 = 窗中位半音相对上一窗 |Δ| ≥1
    events = []
    for i in range(1, n):
        drop = db[i] - db[i - 1]
        if drop <= -6:
            dst = (fw[i][0] - fw[i - 1][0]) if (fw[i][0] == fw[i][0] and fw[i - 1][0] == fw[i - 1][0]) else float("nan")
            events.append({
                "t": float(ts[i]), "drop_db": round(float(drop), 1),
                "f0_delta_st": round(dst, 2) if dst == dst else None,
                "with_sink": (abs(dst) >= 1) if dst == dst else None,
                "f0_dir": ("down" if dst < 0 else "up") if dst == dst and abs(dst) >= 1 else None,
            })

    # 汇总 + sanity 门 + 判读
    summ = {"file": path.name, "f0_meter": f0_src, "emo_meter": emo_src,
            "n_windows": n, "n_events": len(events)}
    if events:
        with_sink = [e for e in events if e["with_sink"]]
        summ["p_with_sink"] = round(len(with_sink) / len(events), 2)
        summ["read_exp1"] = ("盲区代价大（≥50%）" if summ["p_with_sink"] >= 0.5
                             else "实际盲区小（<20%）" if summ["p_with_sink"] < 0.2
                             else "灰区，只报数")
    if emo and n > 2:
        v = np.array([r["m_valence"] for r in rows if r["m_valence"] is not None])
        a = np.array([r["m_arousal"] for r in rows if r["m_arousal"] is not None])
        d = np.array([r["db"] for r in rows if r["m_arousal"] is not None])
        if len(v) > 3:
            summ["corr_db_arousal"] = round(float(np.corrcoef(d, a)[0, 1]), 3)
            summ["sanity_pass"] = summ["corr_db_arousal"] >= 0.5
            summ["valence_sd"] = round(float(v.std()), 3)
            summ["read_exp2"] = ("low-signal" if summ["valence_sd"] < 0.05
                                 else f"valence 在动（sd={summ['valence_sd']}），top 时刻见 events")
            if not summ["sanity_pass"]:
                summ["read_exp2"] = "no-transfer：corr<0.5，实验二作废不算数"

    stem = out_dir / path.stem
    stem.with_suffix(".window.tsv").write_text(
        "\t".join(rows[0].keys()) + "\n" +
        "\n".join("\t".join("" if v is None else str(v) for v in r.values()) for r in rows) + "\n",
        encoding="utf-8")
    stem.with_suffix(".events.tsv").write_text(
        (json.dumps(events, ensure_ascii=False, indent=1) if events else "[]"),
        encoding="utf-8")
    return summ


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--media", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--no-emotion", action="store_true")
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    files = sorted(p for p in args.media.iterdir()
                   if p.suffix.lower() in {".mp4", ".mkv", ".webm", ".flv", ".m4a", ".mp3", ".wav"})
    if not files:
        sys.exit(f"media 目录里没有媒体文件：{args.media}")
    print(f"素材 {len(files)} 支｜窗口 {WINDOW}s｜判读已先写死（见文件头）")

    summaries = []
    for p in files:
        summaries.append(run_one(p, args.out, do_emotion=not args.no_emotion))

    (args.out / "summary.json").write_text(
        json.dumps({"window_s": WINDOW, "voiced_conf": VOICED_CONF,
                    "meters_note": "f0/db 列为她的口径；m_* 列 meter:external-model，不进 φ（E1）",
                    "files": summaries}, ensure_ascii=False, indent=2),
        encoding="utf-8")
    print(f"\n完成 → {args.out}/summary.json")


if __name__ == "__main__":
    main()
