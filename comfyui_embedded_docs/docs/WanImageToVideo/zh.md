> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/zh.md)

WanImageToVideo 节点为视频生成任务准备条件化（conditioning）和潜在空间（latent）表示。它会为视频生成创建一个空的潜在空间，并可选择性地结合起始图像和 CLIP 视觉输出，以引导视频生成过程。该节点会根据提供的图像和视觉数据修改正向和负向条件化输入。

## 输入

| 参数 | 数据类型 | 是否必填 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 用于引导生成过程的正向条件化输入 |
| `negative` | CONDITIONING | 是 | - | 用于引导生成过程的负向条件化输入 |
| `vae` | VAE | 是 | - | 用于将图像编码到潜在空间的 VAE 模型 |
| `width` | INT | 是 | 16 至 MAX_RESOLUTION | 输出视频的宽度（默认值：832，步长：16） |
| `height` | INT | 是 | 16 至 MAX_RESOLUTION | 输出视频的高度（默认值：480，步长：16） |
| `length` | INT | 是 | 1 至 MAX_RESOLUTION | 视频的帧数（默认值：81，步长：4） |
| `batch_size` | INT | 是 | 1 至 4096 | 每批生成的视频数量（默认值：1） |
| `clip_vision_output` | CLIP_VISION_OUTPUT | 否 | - | 可选的 CLIP 视觉输出，用于额外的条件化 |
| `start_image` | IMAGE | 否 | - | 可选的起始图像，用于初始化视频生成 |

**注意：** 当提供了 `start_image` 时，节点会对图像序列进行编码，并对条件化输入应用掩码。当提供了 `clip_vision_output` 参数时，它会向正向和负向输入添加基于视觉的条件化信息。

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 已整合图像和视觉数据的修改后正向条件化 |
| `negative` | CONDITIONING | 已整合图像和视觉数据的修改后负向条件化 |
| `latent` | LATENT | 可用于视频生成的空潜在空间张量 |

---
**Source fingerprint (SHA-256):** `e9f4350c43e48351523c04d82675c24f868df7b2109530c32b8e752a3ab61e8b`
