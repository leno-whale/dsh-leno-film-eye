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
#           变化 ≥1 且方向为降（down）才记「伴随沉」；|Δst|>12 视作八度误判，判不了。
#           分母只算可判事件（前后窗都有定音），未定音另报 p_undecidable。
#           ≥50% 塌事件伴随 → 盲区代价大；<20% → 实际盲区小；中间 → 灰区，只报数。
#   实验二：valence 窗间标准差 <0.05（模型原尺度）→ 此素材 valence 携带信息少，
#           报 low-signal；否则给 top-10 valence 移动时刻（按 |Δv| 排）。
#
#   【独立口径 · 3 dB】2026-10-31 追加，作者已裁决「另开」。不是上一条的重分析，是另一条实验臂：
#           塌事件 = 4s 窗 db 环比跌 ≥3 dB（--drop-db -3）。
#           事件定义变了 ⇒ 3 dB 的结果与 6 dB **不可比、不可合并**：6 dB 事件必定也是 3 dB 事件，
#           反之不然，两个事件总体不同，pooled p 也不许相加。
#           判读规则**逐字沿用**（沉 = 降 ≥1 半音且方向 down；|Δst|>12 判无效；
#           可判 <20 报 insufficient；≥50% / <20% / 中间灰区）——换阈值时改判读就是凑数。
#           新增一条只对本口径的诚实记录：连续下坡会被切成多个相邻事件，它们**不独立**，
#           故 summary 另报 n_runs（连续事件段数）；CI 按 run 算，不按事件算。
#
# 纪律：
#   - db 列不是另造的尺子——与本 bundle parity/ 下她 node 实现的 align.tsv
#     逐行对（同 4s 窗、同 20log10(RMS)、同 -90 钳制）；对不上 → parity FAIL，停。
#   - 模型输出全部带口径标签 meter:external-model，不冒充理论里的 φ（公理 E1）。
#   - 情绪模型拉不动不硬凑：实验一独立成立，实验二标 no-model。
#
# 用法：python3 run_f0_valence.py --media ../media --out ../out [--no-emotion]
#       [--f0 pyin|crepe] [--f0-scope all|events] [--drop-db -6|-3]
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
# 判读最小可判样本。n=20 时 0/20 的 Wilson 95% 上界约 0.16（<0.2）、20/20 的下界约 0.84（>0.5），
# 才够区分本题的两个判读区间；n<20 一律报 insufficient，不许出「盲区大/小」。
MIN_DECIDED = 20
ST_REF = 440.0       # 半音基准 A4
DROP_DB = -6.0       # 塌阈值默认 -6 dB；-3 是独立口径，结果单列，不与 -6 合并

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


def f0_track(path, meter="pyin"):
    """F0 尺子，两种 meter 的结果**不可比**，不许混进同一张表：
      pyin  —— 默认。对说话声稳。2026-10-31 实测：同一段访谈 pyin voiced 70.3%、f0 中位 166.7Hz。
      crepe —— 对歌唱/乐器好；对纯说话声 periodicity 系统性偏低
               （同一段 crepe voiced 仅 7.0%，且放大 16 倍无变化，排除电平问题）。
    pyin 的 fmax 设 500：说话基频上限约 350Hz，留余量且减少倍频错误；
    若跑音乐素材再调回 1100 并换标签。
    返回 (f0[n_frames_hop10ms], 来源标签)。"""
    if meter == "pyin":
        import librosa
        audio = ffmpeg_decode(path, F0_RATE)
        # 分块跑：pyin 是逐帧 Viterbi，整片一次性算又慢又全程静默，容易被当成卡死
        # 而中断终端（2026-10-31 已因此丢过一次 26 分钟片）。每块 CHUNK_SEC 秒，
        # 块长对齐到 hop，拼接后帧不偏。代价：块边界处 Viterbi 重置，边界几十毫秒不可靠。
        CHUNK_SEC = 300
        step = int(CHUNK_SEC * F0_RATE / F0_HOP) * F0_HOP
        total = len(audio)
        parts = []
        for i in range(0, total, step):
            seg = audio[i:i + step]
            if len(seg) < F0_HOP * 8:
                break
            f, _, _ = librosa.pyin(seg, fmin=65, fmax=500, sr=F0_RATE, hop_length=F0_HOP)
            parts.append(f)
            print(f"    pyin {min(i + step, total) / F0_RATE:6.0f} / {total / F0_RATE:.0f} s",
                  flush=True)
        f0 = np.concatenate(parts) if parts else np.array([], dtype=float)
        print(f"    F0: librosa pyin（CPU，fmin 65 / fmax 500，{len(parts)} 块）")
        return np.asarray(f0, dtype=float), "pyin"

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
    print("    F0: librosa pyin（CPU，回退）")
    return np.asarray(f0, dtype=float), "pyin"


NAN_STATS = (float("nan"),) * 4


def window_stats(seg):
    """单个 4s 窗的 (中位半音, 四分位距, 斜率, voiced 占比)；定音帧不足 10% 给 NaN。"""
    per = int(round(WINDOW / (F0_HOP / F0_RATE)))
    v = seg[~np.isnan(seg)]
    if len(v) < per * 0.1:
        return NAN_STATS
    st = semitone(v)
    slope = float(np.polyfit(np.arange(len(st)) * (F0_HOP / F0_RATE), st, 1)[0]) if len(st) > 2 else float("nan")
    return (float(np.median(st)),
            float(np.percentile(st, 75) - np.percentile(st, 25)),
            slope, len(v) / per)


def f0_windows(f0, window=WINDOW, hop_sec=F0_HOP / F0_RATE):
    """每 4s 窗聚合：中位半音、四分位距、斜率（半音/秒）、voiced 占比。"""
    per = int(round(window / hop_sec))
    m = len(f0) // per
    return [window_stats(f0[i * per:(i + 1) * per]) for i in range(m)]


def ffmpeg_decode_segment(path, start, dur, rate=F0_RATE):
    r = subprocess.run(
        ["ffmpeg", "-v", "error", "-ss", f"{start:.3f}", "-t", f"{dur:.3f}",
         "-i", str(path), "-vn", "-ac", "1", "-ar", str(rate), "-f", "s16le", "-"],
        capture_output=True, check=True)
    return np.frombuffer(r.stdout, dtype=np.int16).astype(np.float32) / 32768.0


def f0_windows_events(path, db, meter="pyin", drop_db=DROP_DB):
    """两遍法：db 已经定位了塌事件，只扫事件窗口的 F0。
    每个塌窗与它前一窗拼成 8s，一次解码、一次 pyin——逐窗单跑会让 Viterbi
    在每个 4s 边界重置，Δst 直接失真；拼起来才保住上下文。
    返回与 db 等长的 stats 列表，没扫到的窗全 NaN（判定时自然落进「不可判」）。"""
    if meter != "pyin":
        sys.exit("--f0-scope events 只支持 pyin：crepe 走 GPU，整片本来就快，没有两遍法的意义")
    import librosa
    per = int(round(WINDOW / (F0_HOP / F0_RATE)))
    stats = [NAN_STATS] * len(db)
    idxs = [i for i in range(1, len(db)) if db[i] - db[i - 1] <= drop_db]
    print(f"    两遍法（塌阈值 {drop_db:g} dB）：塌 {len(idxs)} 个 → 只算 "
          f"{2 * len(idxs)} 个窗（整片 {len(db)} 窗）")
    for j, i in enumerate(idxs, 1):
        audio = ffmpeg_decode_segment(path, (i - 1) * WINDOW, 2 * WINDOW)
        f, _, _ = librosa.pyin(audio, fmin=65, fmax=500, sr=F0_RATE, hop_length=F0_HOP)
        f = np.asarray(f, dtype=float)
        if len(f) < 2 * per:                      # 尾巴补 NaN，不拿短片段冒充满窗
            f = np.concatenate([f, np.full(2 * per - len(f), np.nan)])
        stats[i - 1] = window_stats(f[:per])
        stats[i] = window_stats(f[per:2 * per])
        print(f"    pyin {j}/{len(idxs)}（t={i * WINDOW:.0f}s）", flush=True)
    return stats

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


def run_one(path, out_dir, do_emotion=True, f0_meter="pyin", f0_scope="all", drop_db=DROP_DB):
    print(f"  {path.name}")
    x8k = ffmpeg_decode(path, RATE)
    db = window_db(x8k, RATE, WINDOW)
    if path.name.startswith("28871298443") or "红泪石戒指" in path.name:
        if not parity_check(db):
            sys.exit(1)

    ts = np.arange(len(db)) * WINDOW
    if f0_scope == "events":
        fw = f0_windows_events(path, db, f0_meter, drop_db)
        f0_src = f"{f0_meter}(events)"
    else:
        f0, f0_src = f0_track(path, f0_meter)
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

    # 事件表：塌 = db 一窗跌 ≥ drop_db（默认 6，3 dB 是独立口径）；伴随沉 = 窗中位半音相对上一窗降 ≥1
    # 方向必须为 down；|Δ|>12 视为八度误判 → 记 null（判不了）
    events = []
    n_runs = 0
    last_ev = -10
    for i in range(1, n):
        drop = db[i] - db[i - 1]
        if drop <= drop_db:
            if i != last_ev + 1:      # 连续下坡被切成多个事件，只算一段；它们不独立
                n_runs += 1
            last_ev = i
            dst = (fw[i][0] - fw[i - 1][0]) if (fw[i][0] == fw[i][0] and fw[i - 1][0] == fw[i - 1][0]) else float("nan")
            decidable = dst == dst and abs(dst) <= 12
            events.append({
                "t": float(ts[i]), "drop_db": round(float(drop), 1),
                "prev_db": round(float(db[i - 1]), 1),
                "f0_delta_st": round(dst, 2) if decidable else None,
                "with_sink": bool(dst <= -1) if decidable else None,
                "f0_dir": ("down" if dst < 0 else "up") if decidable else None,
            })

    # 汇总 + sanity 门 + 判读
    summ = {"file": path.name, "f0_meter": f0_src, "f0_scope": f0_scope, "emo_meter": emo_src,
            "drop_db": drop_db, "n_windows": n, "n_events": len(events)}
    if events:
        summ["n_runs"] = n_runs
        decided = [e for e in events if e["with_sink"] is not None]
        sinks = [e for e in decided if e["with_sink"]]
        summ["n_decided"] = len(decided)
        summ["n_undecidable"] = len(events) - len(decided)
        summ["p_undecidable"] = round(1 - len(decided) / len(events), 2)
        if decided:
            summ["p_with_sink"] = round(len(sinks) / len(decided), 2)
            if len(decided) < MIN_DECIDED:
                summ["read_exp1"] = (f"insufficient：可判仅 {len(decided)} 条"
                                     f"（需 ≥{MIN_DECIDED}），p 不可采信")
            else:
                summ["read_exp1"] = ("盲区代价大（≥50%）" if summ["p_with_sink"] >= 0.5
                                     else "实际盲区小（<20%）" if summ["p_with_sink"] < 0.2
                                     else "灰区，只报数")
        else:
            summ["read_exp1"] = "insufficient：无一条可判（全部未定音或八度误判）"
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
    ap.add_argument("--f0", choices=("pyin", "crepe"), default="pyin",
                    help="F0 尺子；pyin 对说话声稳，crepe 对歌唱/乐器好；两种结果不可比")
    ap.add_argument("--f0-scope", choices=("all", "events"), default="all",
                    help="all：整片逐窗算 F0（默认）；events：两遍法，只用 db 定位塌事件、"
                         "只对事件邻窗算 F0（仅 pyin，长片用，判读口径不变）")
    ap.add_argument("--drop-db", type=float, default=DROP_DB,
                    help="塌阈值（dB，环比）。默认 -6。**-3 是独立实验臂**：结果单列、"
                         "不与 -6 合并，判读规则不变")
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    files = sorted(p for p in args.media.iterdir()
                   if p.suffix.lower() in {".mp4", ".mkv", ".webm", ".flv", ".m4a", ".mp3", ".wav"})
    if not files:
        sys.exit(f"media 目录里没有媒体文件：{args.media}")
    print(f"素材 {len(files)} 支｜窗口 {WINDOW}s｜塌阈值 {args.drop_db:g} dB｜"
          f"F0 范围 {args.f0_scope}｜判读已先写死（见文件头）")

    summaries = []
    for p in files:
        summaries.append(run_one(p, args.out, do_emotion=not args.no_emotion,
                                 f0_meter=args.f0, f0_scope=args.f0_scope,
                                 drop_db=args.drop_db))

    (args.out / "summary.json").write_text(
        json.dumps({"window_s": WINDOW, "drop_db": args.drop_db, "voiced_conf": VOICED_CONF,
                    "meters_note": "f0/db 列为她的口径；m_* 列 meter:external-model，不进 φ（E1）",
                    "files": summaries}, ensure_ascii=False, indent=2),
        encoding="utf-8")
    print(f"\n完成 → {args.out}/summary.json")


if __name__ == "__main__":
    main()
