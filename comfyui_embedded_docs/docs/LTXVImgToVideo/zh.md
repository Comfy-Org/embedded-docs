# 图像到视频（LTXV）

LTXVImgToVideo 节点用于为从输入图像生成视频准备潜在表示。图像被调整到请求的宽度和高度，经 VAE 编码后放置在潜在序列的第一帧。使用 `strength` 创建噪声掩码，以控制原始图像内容被保留或修改的程度，正面和负面条件数据保持不变地传递。

## 输入
| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 输入提供的正面条件数据，原样返回。 | CONDITIONING | 是 | - |
| `negative` | 输入提供的负面条件数据，原样返回。 | CONDITIONING | 是 | - |
| `vae` | 用于将输入图像编码到潜在空间的 VAE 模型。 | VAE | 是 | - |
| `image` | 输入图像，调整大小并编码后构成视频潜在序列的开头。 | IMAGE | 是 | - |
| `width` | 输出视频宽度（像素）（默认值：768，步长：32）。 | INT | 是 | 64 to MAX_RESOLUTION |
| `height` | 输出视频高度（像素）（默认值：512，步长：32）。 | INT | 是 | 64 to MAX_RESOLUTION |
| `length` | 生成视频的帧数（默认值：97，步长：8）。 | INT | 是 | 9 to MAX_RESOLUTION |
| `batch_size` | 一个潜在批次中生成的视频数量（默认值：1）。 | INT | 是 | 1 to 4096 |
| `strength` | 控制第一个潜在帧中保留多少编码图像内容。值为 1.0 时完全保留原始图像，值为 0.0 时允许最大程度修改（默认值：1.0）。 | FLOAT | 是 | 0.0 to 1.0 |

注意：`MAX_RESOLUTION` 是 ComfyUI 安装允许的最大分辨率。

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 未修改地传递正面条件数据。 | CONDITIONING |
| `negative` | 未修改地传递负面条件数据。 | CONDITIONING |
| `latent` | 包含序列起始处编码输入图像的视频潜在表示，以及基于 `strength` 的噪声掩码。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/zh.md)

---
**Source fingerprint (SHA-256):** `4ebc7f80b4d9ac3329e3349c7048885de22b827b5bdd102976687afd7e07a16b`
