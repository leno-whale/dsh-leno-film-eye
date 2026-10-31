# F0 与 valence 旁证：交接说明（实验跑完后随 PR 交付）

> 状态：**骨架，数字待填**（云上跑完回填，字段全部预留）。
> 这是外部模型的探针实验，不是理论内的测量。它在理论里的位置只有两处：
> 命题 6（π_noF0 丢基频）的**盲区实际大小**，与经验命题 7 / §13.5（只有 arousal 侧、
> 西方框架跨文化）的**域内代价**。此外不主张任何东西。

## 一、它是什么 / 不是什么

- **是**：外部尺子（torchcrepe / pyin 的 F0；essentia arousalvalence 的 v/a）在她素材上的读数，
  全部带口径标签 `meter:external-model`。db 列除外——db 用的是她自己的帧算子口径，
  且首片与 node 实现逐行对过（`gpu/parity/`，对不上会自动停）。
- **不是**：φ 的输出。公理 E1（三套标签空间不可互转）在这里完整适用——模型的
  valence 是工程编码连续 (v,a)，不许与 GEMS/SER/DEAM 三套互转，不许进任何判据。
- **纪律**：判读先写死在 `gpu/run_f0_valence.py` 文件头，跑之前落纸，云上不改参。

## 二、判读（先写死的原文）

1. **sanity 门**：corr(m_arousal, db) ≥ 0.5。不过 → 报 `no-transfer`，实验二作废不算数
   （这正是 §13.5 说的域偏移风险，作废本身就是信息）。
2. **实验一**（F0 → 命题 6 的盲区）：塌事件 = 4s 窗 db 环比跌 ≥6 dB；
   伴随沉 = 窗中位半音 |Δ| ≥1。
   ≥50% 伴随 → 盲区代价大；<20% → 此素材实际盲区小；中间 → 灰区只报数。
3. **实验二**（valence → 经验命题 7 的代价）：窗间 sd <0.05 → `low-signal`；
   否则给 top-10 valence 移动时刻——**这份时刻清单是主交付**，可对照帧逐一核。

## 三、结果（待填）

| 项 | 数值 | 判读 |
|---|---|---|
| parity（首片 db 逐行） | ☐ PASS / FAIL | — |
| F0 来源 | ☐ torchcrepe / pyin | — |
| 塌事件数（首片） | ☐ | — |
| 伴随沉比例 p | ☐ | ☐ 盲区大 / 小 / 灰区 |
| corr(db, m_arousal) | ☐ | ☐ sanity 过 / no-transfer |
| valence sd | ☐ | ☐ low-signal / 在动 |
| top-10 valence 时刻 | ☐ 见 events.tsv | 待人工核帧 |

跨片（若 ≥5 支）：各片 p 与 corr 的分布另表。

## 四、怎么并回她的表

`out/<片名>.window.tsv` 与 `align.tsv` **同 4s 窗、同 t 键**，直接 join：

```bash
paste align.tsv <(cut -f3- ../out/<片名>.window.tsv) > align-plus.tsv
```

## 五、复现

bundle 在 `gpu/`（runbook 逐行可粘贴）；环境单卡 PyTorch；
素材上传不走 B 站（-412 风险维持 P1 不变），全部从本机传。

## 六、什么能打死它（照抄纪律）

1. **域偏移**：情绪模型训练分布是西方流行乐（MTG-Jamondo/MSD 系），中文 MV/BGM 上
   sanity 门不过即作废——不调参救。
2. **CREPE 对纯配乐段失效**：它是人声训练的 pitch tracker；无人声段 F0 读数标 `voiced`
   低信度，判读时只看 voiced ≥0.3 的窗。
3. **塌阈值 6 dB 是先写的**：换阈值会动 p——不许跑完再挑阈值。
4. 单素材不外推；跨片 ≥5 才给分布，否则只标「首跑」。
