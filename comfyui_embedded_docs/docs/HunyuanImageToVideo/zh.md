# 图像到视频（Hunyuan）

## 输入
| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 用于引导视频生成的正面条件输入 | CONDITIONING | 是 | - |
| `vae` | 用于将图像编码到潜在空间的 VAE 模型 | VAE | 是 | - |
| `width` | 输出视频的宽度（像素）（默认值：848，步长：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `height` | 输出视频的高度（像素）（默认值：480，步长：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `length` | 输出视频的帧数（默认值：53，步长：4） | INT | 是 | 1 to MAX_RESOLUTION |
| `batch_size` | 同时生成的视频数量（默认值：1） | INT | 是 | 1 to 4096 |
| `guidance_type` | 将起始图像融入视频生成的方法（默认值："v1 (concat)"） | COMBO | 是 | "v1 (concat)"<br>"v2 (replace)"<br>"custom" |
| `start_image` | 用于初始化视频生成的可选起始图像 | IMAGE | 否 | - |

**注意：** 当提供了 `start_image` 时，节点会根据所选的 `guidance_type` 使用不同的引导方法：

- "v1 (concat)"：将图像潜在表示与视频潜在表示拼接，并应用遮罩将图像混合到视频中。
- "v2 (replace)"：用图像潜在表示替换初始视频帧，并应用噪声遮罩。
- "custom"：将图像用作引导的参考潜在表示。

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 当提供 `start_image` 时，应用图像引导后的修正正面条件 | CONDITIONING |
| `latent` | 可供视频生成模型进一步处理的视频潜在表示 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/zh.md)

---
**Source fingerprint (SHA-256):** `0ed00d59513492f31760a18ce3b0edf10b64cad848ba52c4e47d5f61fae9accc`
