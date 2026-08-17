# 图像到视频（Wan）

WanImageToVideo 节点为视频生成任务准备 conditioning 和 latent 表示。它创建一个空的 latent 空间用于视频生成，并可选择性地整合起始图像和 CLIP vision 输出以指导视频生成过程。该节点根据提供的图像和视觉数据修改 `positive` 和 `negative` conditioning 输入。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 用于引导生成的正向 conditioning 输入 | CONDITIONING | 是 | - |
| `negative` | 用于引导生成的负向 conditioning 输入 | CONDITIONING | 是 | - |
| `vae` | 用于将图像编码到 latent 空间的 VAE 模型 | VAE | 是 | - |
| `width` | 输出视频的宽度（默认：832，步长：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `height` | 输出视频的高度（默认：480，步长：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `length` | 视频中的帧数（默认：81，步长：4） | INT | 是 | 1 to MAX_RESOLUTION |
| `batch_size` | 每批生成的视频数量（默认：1） | INT | 是 | 1 to 4096 |
| `clip_vision_output` | 可选的 CLIP vision 输出，用于额外的 conditioning | CLIP_VISION_OUTPUT | 否 | - |
| `start_image` | 可选的起始图像，用于初始化视频生成。提供时，图像会调整大小以匹配指定的宽度和高度，视频的初始帧将从该图像初始化。其余帧以中性灰（0.5）填充。仅使用图像的前 `length` 帧。 | IMAGE | 否 | - |

**注意：** 当提供 `start_image` 时，节点使用 VAE 对图像序列进行编码，并对 conditioning 输入应用掩码。该掩码覆盖所有帧，但由起始图像初始化的帧除外，从而使生成能够基于所提供的图像进行。当提供 `clip_vision_output` 参数时，它会为 `positive` 和 `negative` 输入添加基于视觉的 conditioning。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 更新后的正向 conditioning，包含图像和视觉数据 | CONDITIONING |
| `negative` | 更新后的负向 conditioning，包含图像和视觉数据 | CONDITIONING |
| `latent` | 准备好用于视频生成的空 latent 空间张量，形状为 [batch_size, 16, ((length-1)//4)+1, height//8, width//8] | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/zh.md)

---
**Source fingerprint (SHA-256):** `46779f9f2f3da16826b7b547761a96597a3b6b43ce51a9c13367987642f3d5b7`
