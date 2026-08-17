# WanFunInpaint视频

此节点通过在起始帧和结束帧之间进行修补来创建视频序列。它接收正向和负向条件输入以及可选帧图像，以生成视频潜在表示。该节点支持可配置的尺寸和长度参数来处理视频生成。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 用于视频生成的正向条件提示 | CONDITIONING | 是 | - |
| `negative` | 视频生成中需避免的负向条件提示 | CONDITIONING | 是 | - |
| `vae` | 用于编码/解码操作的 VAE 模型 | VAE | 是 | - |
| `width` | 输出视频宽度（像素，默认：832，步长：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `height` | 输出视频高度（像素，默认：480，步长：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `length` | 视频序列中的帧数（默认：81，步长：4） | INT | 是 | 1 to MAX_RESOLUTION |
| `batch_size` | 每批生成的视频数量（默认：1） | INT | 是 | 1 to 4096 |
| `clip_vision_output` | 用于额外条件输入的 CLIP 视觉输出（可选） | CLIP_VISION_OUTPUT | 否 | - |
| `start_image` | 视频生成的起始帧图像（可选） | IMAGE | 否 | - |
| `end_image` | 视频生成的结束帧图像（可选） | IMAGE | 否 | - |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 处理后的正向条件输出 | CONDITIONING |
| `negative` | 处理后的负向条件输出 | CONDITIONING |
| `latent` | 生成的视频潜在表示 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/zh.md)

---
**Source fingerprint (SHA-256):** `70b58e961c5df12f94183245ce320197439b2505b47d0bb3ff643b25c9fe6175`
