# 空Latent视频（LTXV）

EmptyLTXVLatentVideo 节点为视频生成创建一个空的潜在张量。它生成一个用零填充的潜在表示，具有指定的宽度、高度、长度和批大小，可随时用作 LTXV 视频工作流的起始点。该潜在张量以压缩形式存储视频：空间维度除以 32，帧数减少 8 倍。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `width` | 潜在视频的宽度（以像素为单位）（默认值：768，步长：32） | INT | 是 | 64 to MAX_RESOLUTION |
| `height` | 潜在视频的高度（以像素为单位）（默认值：512，步长：32） | INT | 是 | 64 to MAX_RESOLUTION |
| `length` | 潜在视频的帧数（默认值：97，步长：8） | INT | 是 | 1 to MAX_RESOLUTION |
| `batch_size` | 一个批次中生成的潜在视频数量（默认值：1） | INT | 否 | 1 to 4096 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `samples` | 生成的用零填充的空潜在张量。该潜在张量还带有一个 `downscale_ratio_spacial` 值为 32，表示应用于宽度和高度的空间下采样比例。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/zh.md)

---
**Source fingerprint (SHA-256):** `0b1e57baf9730d852b03b6bccbb8a033e2be9b9cd2420a0aa3638c31f6d3cd26`
