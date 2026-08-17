# 图像到视频（Hunyuan Video 15 ）

HunyuanVideo15ImageToVideo 节点基于 HunyuanVideo 1.5 模型，为视频生成准备 conditioning 和潜空间数据。它会为视频序列创建一个初始潜变量表示，并可选地集成起始图像或 CLIP 视觉输出，以引导生成过程。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 用于描述视频应包含内容的正面 conditioning 提示。 | CONDITIONING | 是 | - |
| `negative` | 用于描述视频应避免内容的负面 conditioning 提示。 | CONDITIONING | 是 | - |
| `vae` | 用于将起始图像编码到潜空间的 VAE（变分自编码器）模型。 | VAE | 是 | - |
| `width` | 输出视频帧的宽度（以像素为单位）。必须能被 16 整除。（默认值：848） | INT | 是 | 16 至 MAX_RESOLUTION，步长：16 |
| `height` | 输出视频帧的高度（以像素为单位）。必须能被 16 整除。（默认值：480） | INT | 是 | 16 至 MAX_RESOLUTION，步长：16 |
| `length` | 视频序列中的总帧数。该值以 4 为步长递增。（默认值：33） | INT | 是 | 1 至 MAX_RESOLUTION，步长：4 |
| `batch_size` | 单个批次中生成的视频序列数量。（默认值：1） | INT | 是 | 1 至 4096 |
| `start_image` | 用于初始化视频生成的可选起始图像。如果提供，该图像将被编码并用于对前几帧进行 conditioning。仅使用图像的前 `length` 帧。 | IMAGE | 否 | - |
| `clip_vision_output` | 可选的 CLIP 视觉嵌入，用于为生成提供额外的视觉 conditioning。 | CLIP_VISION_OUTPUT | 否 | - |

**注意：** 当提供 `start_image` 时，它会使用双线性插值自动调整大小以匹配指定的 `width` 和 `height`，并且仅使用其 RGB 通道。将使用图像批次的前 `length` 帧。然后，编码后的图像会以 `concat_latent_image` 的形式连同相应的 `concat_mask` 一起添加到 `positive` 和 `negative` conditioning 中。该掩码在起始图像覆盖的帧上设置为 0.0，在其余帧上设置为 1.0。当提供 `clip_vision_output` 时，它也会被添加到 `positive` 和 `negative` conditioning 中。

## 输出

| 输出名 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 修改后的正面 conditioning，可能现已包含编码后的起始图像或 CLIP 视觉输出。 | CONDITIONING |
| `negative` | 修改后的负面 conditioning，可能现已包含编码后的起始图像或 CLIP 视觉输出。 | CONDITIONING |
| `latent` | 一个空的潜变量张量，其维度已根据指定的批次大小、视频长度、宽度和高度进行配置。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15ImageToVideo/zh.md)

---
**Source fingerprint (SHA-256):** `dbedf7f378ae9613c8f47fe9876a4576c815055b4cdb6bf687b7575fcd7ea80a`
