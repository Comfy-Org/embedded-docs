# 分离 AV 潜空间

LTXVSeparateAVLatent 节点接收组合的音视频潜在表示，并将其拆分为两个独立的潜在变量：一个用于视频，一个用于音频。它适用于任何音视频模型，例如 LTXV 或 MiniMax H3。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `av_latent` | 需要拆分的组合音视频潜在表示。 | LATENT | 是 | N/A |

**注意：** 输入潜在变量的 `samples` 张量预计在第一维度（批次维度）上至少包含两个元素。第一个元素用于视频潜在变量，第二个元素用于音频潜在变量。如果存在 `noise_mask`，则按相同方式拆分。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `video_latent` | 包含拆分后视频数据的潜在表示。 | LATENT |
| `audio_latent` | 包含拆分后音频数据的潜在表示。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateAVLatent/zh.md)

---
**Source fingerprint (SHA-256):** `22ed38bbc1b5716cee380c35c50455810f79c273f51bbe6a535c9ae33192afe6`
