# VOIDInpaintConditioning

VOIDInpaintConditioning 节点准备使用 CogVideoX 模型进行修复（inpainting）所需的 conditioning 数据。它接收源视频和预处理后的 quadmask，通过 VAE 对其进行编码，并将它们组合成一个 32 通道的 conditioning 信号（16 通道遮罩 + 16 通道遮罩视频），模型使用该信号来填充遮罩区域。

## 输入
| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 将要附加修复潜空间信息的正面 conditioning | CONDITIONING | 是 | - |
| `negative` | 将要附加修复潜空间信息的负面 conditioning | CONDITIONING | 是 | - |
| `vae` | 用于将遮罩和遮罩视频编码到潜空间中的 VAE 模型 | VAE | 是 | - |
| `video` | 源视频帧 [T, H, W, 3] | IMAGE | 是 | - |
| `quadmask` | 来自 VOIDQuadmaskPreprocess 的预处理 quadmask [T, H, W] | MASK | 是 | - |
| `width` | 视频和遮罩调整到的宽度（默认值：672） | INT | 是 | 16 to MAX_RESOLUTION (step: 8) |
| `height` | 视频和遮罩调整到的高度（默认值：384） | INT | 是 | 16 to MAX_RESOLUTION (step: 8) |
| `length` | 要处理的像素帧数。对于 CogVideoX-Fun-V1.5（patch_size_t=2），latent_t 必须为偶数——产生奇数 latent_t 的长度会被向下取整（例如 49 → 45）（默认值：45） | INT | 是 | 1 to MAX_RESOLUTION (step: 1) |
| `batch_size` | 输出噪声 latent 的批次大小（默认值：1） | INT | 是 | 1 to 64 |

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 已添加修复潜空间信息的正面 conditioning | CONDITIONING |
| `negative` | 已添加修复潜空间信息的负面 conditioning | CONDITIONING |
| `latent` | 形状为 [batch_size, 16, latent_t, latent_h, latent_w] 的零填充噪声 latent 张量 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/zh.md)

---
**Source fingerprint (SHA-256):** `885e462c0f17a3e9610146a05ba3b9c879db0112d3961c95a83f63ba2cd511f1`
