# HunyuanRefinerLatent

HunyuanRefinerLatent 节点处理用于细化操作的 conditioning 和 latent 输入。它对正向和负向 conditioning 应用噪声增强，同时结合潜在图像数据，并生成具有特定维度的新 latent 输出以进行进一步处理。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 要处理的正向 conditioning 输入 | CONDITIONING | 是 | - |
| `negative` | 要处理的负向 conditioning 输入 | CONDITIONING | 是 | - |
| `latent` | 潜在表示输入 | LATENT | 是 | - |
| `noise_augmentation` | 要应用的噪声增强量（默认值：0.10，步长：0.01，高级参数） | FLOAT | 是 | 0.0 - 1.0 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 已处理的正向 conditioning，包含应用的噪声增强和潜在图像拼接 | CONDITIONING |
| `negative` | 已处理的负向 conditioning，包含应用的噪声增强和潜在图像拼接 | CONDITIONING |
| `latent` | 一个新的零填充潜在张量，其批次大小和最后三个维度大小与输入 `latent` 相同，但具有 32 个通道 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/zh.md)

---
**Source fingerprint (SHA-256):** `4c5669cf2ad5ba00e176876741b7d8d3f092cc58d2163871a10fd769ee4ff84c`
