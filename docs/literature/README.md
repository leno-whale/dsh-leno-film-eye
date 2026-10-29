# 文献（声音与情绪）

这是「看电影」插件（`dsh-leno-film-eye`）的文献目录：**声音 → 情绪**这条链上，
哪些结论有实证支撑、哪些只是我的猜测。

## 收录规则

1. **优先学术与工程的权威来源**：顶会（ACL/EMNLP/ISMIR/ACM MM）、期刊、有代码与数据集的工程实现。
2. **arXiv 只当线索**，不当定论；能落到已发表版本就落已发表版本。
3. 先看摘要判断相关性，再决定要不要整篇下；下了的记在下面这张表里。
4. 拿不到的写进「没拿到」，交给人去取——不猜内容。

## 已下载

| # | 文献 | 出处 | 本地文件 | 状态 |
|---|---|---|---|---|
| 1 | emotion2vec: Self-Supervised Pre-Training for Speech Emotion Representation | arXiv 2312.15185（上交/复旦/港中文/阿里） | `emotion2vec-2023-arxiv-2312.15185.pdf` | **已精读** |
| 2 | Emosical: An Emotion-Annotated Musical Theatre Dataset | Findings of EMNLP 2024, pp. 4169–4180 | `emosical-2024-findings-emnlp.pdf` | 摘要已读 |
| 3 | （音乐情绪多输出基准，Neural Computing and Applications 2026） | Springer, doi 10.1007/s00521-026-12370-y | `mer-multi-output-2026-springer-s00521.pdf` | 摘要待读 |
| 4 | EMID: An Emotional Aligned Dataset in Audio-Visual Modality | ACM MM Workshop McGE 2023, arXiv 2308.07622 | `emid-2023-arxiv-2308.07622.pdf` | 摘要已读 |
| 5 | GlobalMood: A cross-cultural benchmark for music emotion recognition | ISMIR 2025, arXiv 2505.09539 | `globalmood-2025-arxiv-2505.09539.pdf` | 未读 |
| 6 | Developing a benchmark for emotional analysis of music（DEAM） | Aljanaki, Yang & Soleymani 2017, PLoS ONE 12(3): e0173392 | `deam-2017-plosone-e0173392.pdf` | 未读 |
| 7 | ITU-R BS.1770-5：节目响度与真峰值的测量算法 | ITU-R 建议书，2023-11 | `itu-r-bs1770-5-2023.pdf` | 未读 |
| 8 | EBU R 128：响度归一化与最大允许电平 | EBU 技术建议，2014 | `ebu-r128-2014.pdf` | 未读 |

## 没拿到

| 文献 | 原因 | 备注 |
|---|---|---|
| GlobalMood（ISMIR `final_papers/308.pdf`） | HTTP 404 | 已改用 arXiv 2505.09539 下到，见 #5 |
| Zentner, Grandjean & Scherer (2008), *Emotions evoked by the sound of music*, Emotion 8(4):494–521（GEMS） | APA 付费墙；OpenAlex 与 Semantic Scholar 均无开放版 | **需要人工取**（机构登录）。它是「离散 vs 维度」之外的第三条路（九因子模型） |

## 已经改变我骨架的结论

- **标签空间要分两套**（emotion2vec）：人声情绪在 SER 实践里是**离散类 + 强度**（IEMOCAP 把 5 类并成 4 类）；连续维度 $(v,a)$ 是音乐/MIR 那套。混用会得到一套什么都没对准的量。
- **时间必须分层，且整句标签会磨平局部**（emotion2vec 的整句级 + 帧级双损失）：一个 16 秒的塌陷在整句标签里会消失，所以「整片一个情绪」这种输出是错的。
- **唱歌属于语音的子集**（Emosical 用唱段做情绪标注）：歌词是唱出来的话，落点在 SER 边界内，不该塞进音乐那套连续维度。
- **跨模态情绪一致性可以做量化**（EMID）：它用 13 维情绪模型做音乐—图像配对，并用心理实验验证配对准确性——这给「声音和画面是不是同一个动作」提供了可操作的形式，而不是纯审美判断。
