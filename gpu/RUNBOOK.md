# RUNBOOK · F0 与 valence 旁证实验（给主人，逐行可粘贴）

> 实例：并行智算云单卡（3090/4090 均可），镜像 PyTorch + CUDA。
> 预计总量 <1 卡时。**跑完立刻关机。**
> 判读已先写死在 `run_f0_valence.py` 文件头与交接文档里——云上不改任何参数。

## 0. 上传（在本机 PowerShell，路径按实际实例信息替换）

```powershell
# 把 bundle 和素材传上去（media/ 里放 mp4：红泪石戒指 + 其余跨片素材）
scp -P <端口> -r f:\agent-trae\dsh-leno-film-eye\gpu <user>@<host>:~/film-eye-gpu
New-Item -ItemType Directory f:\agent-trae\media | Out-Null
# 素材拷进 f:\agent-trae\media\ 后：
scp -P <端口> -r f:\agent-trae\media <user>@<host>:~/film-eye-gpu/
```

## 1. 环境（SSH 进实例后逐行粘贴）

```bash
which ffmpeg || (apt-get update && apt-get install -y ffmpeg)
cd ~/film-eye-gpu/gpu
pip3 install -r requirements.txt          # essentia 装不上没关系，实验一不受影响
python3 -c "import torch; print(torch.cuda.is_available())"   # 必须输出 True
```

## 2. 情绪模型（实验二可选；拉不动就跳过，脚本自动标 no-model）

```bash
mkdir -p models
# essentia 的 arousalvalence 模型（音乐 v/a 回归）：
curl -L -o models/arousalvalence-msd-musicnn-1.pb \
  "https://essentia.upf.edu/models/autotagging/msd/msd-musicnn-1.pb" || true
# ↑ 官网模型索引若换位，试：
#   https://essentia.upf.edu/models/ 下 arousalvalence 相关条目
ls -la models/    # 有文件且 >1MB 才算数
```

## 3. 跑

```bash
cd ~/film-eye-gpu/gpu
python3 run_f0_valence.py --media ../media --out ../out
# 只跑 F0（情绪模型彻底拉不动时）：
# python3 run_f0_valence.py --media ../media --out ../out --no-emotion
```

**第一支是《红泪石戒指》时注意看 `[parity]` 行：必须 PASS。FAIL 说明尺子对不上，立即停，把输出发回来。**

## 4. 回收（在实例上打包，本机拉回）

```bash
cd ~/film-eye-gpu && tar czf out.tgz out
# 本机：
# scp -P <端口> <user>@<host>:~/film-eye-gpu/out.tgz f:\agent-trae\
```

拿回来的东西：`out/<片名>.window.tsv`（逐窗，与她的 align.tsv 同 4s 窗可直接 join）、
`out/<片名>.events.tsv`（塌事件 × F0 行为）、`out/summary.json`（sanity 门 + 判读）。

## 5. 关机

产物拉回本地确认能读后，实例**立刻关机**（按量计费）。SSH 密码用完即弃。
