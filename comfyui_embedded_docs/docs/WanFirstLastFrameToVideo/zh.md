# Wan首尾帧视频

## 输入
| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 用于引导视频生成的正向文本条件 | CONDITIONING | 是 | - |
| `negative` | 用于引导视频生成的负向文本条件 | CONDITIONING | 是 | - |
| `vae` | 用于将图像编码到潜空间的 VAE 模型 | VAE | 是 | - |
| `width` | 输出视频宽度（默认：832，步长：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `height` | 输出视频高度（默认：480，步长：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `length` | 视频序列中的帧数（默认：81，步长：4） | INT | 是 | 1 to MAX_RESOLUTION |
| `batch_size` | 同时生成的视频数量（默认：1） | INT | 是 | 1 to 4096 |
| `clip_vision_start_image` | 从起始图像提取的 CLIP 视觉特征 | CLIP_VISION_OUTPUT | 否 | - |
| `clip_vision_end_image` | 从结束图像提取的 CLIP 视觉特征 | CLIP_VISION_OUTPUT | 否 | - |
| `start_image` | 视频序列的起始帧图像 | IMAGE | 否 | - |
| `end_image` | 视频序列的结束帧图像 | IMAGE | 否 | - |

**注意：** 当同时提供 `start_image` 和 `end_image` 时，节点会创建一个在这两帧之间过渡的视频序列。在处理前，`start_image` 会被裁剪为前 `length` 帧，`end_image` 会被裁剪为后 `length` 帧。如果只提供其中一个，缺失的一侧将用中性灰色帧填充。掩码在起始帧和结束帧存在的位置设置为 0，在其他位置设置为 1。`clip_vision_start_image` 和 `clip_vision_end_image` 参数为可选；当两者都提供时，它们的 CLIP 视觉特征会拼接并应用于正向和负向条件。当仅提供一个时，将单独使用其特征。

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 经过视频帧编码和 CLIP 视觉特征应用的正向条件 | CONDITIONING |
| `negative` | 经过视频帧编码和 CLIP 视觉特征应用的负向条件 | CONDITIONING |
| `latent` | 维度与指定视频参数匹配的空潜在张量 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/zh.md)

---
**Source fingerprint (SHA-256):** `0072e441cb80334c3c961d1bbf2d081c78bc38ed1eacca840c577a2d01b36f05`
