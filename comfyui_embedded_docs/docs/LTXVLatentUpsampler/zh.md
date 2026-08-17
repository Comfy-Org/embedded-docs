# LTXV潜空间上采样器

LTXVLatentUpsampler 节点将视频潜在表示的空间分辨率提高两倍。它使用专门的放大模型处理潜在数据，首先使用所提供的 VAE 的通道统计信息对数据进行反归一化，然后再重新归一化。此节点专为潜在空间内的视频工作流设计。

## 输入
| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `samples` | 要放大的视频的输入潜在表示。 | LATENT | Yes |  |
| `upscale_model` | 用于对潜在数据执行 2 倍放大的已加载模型。 | LATENT_UPSCALE_MODEL | Yes |  |
| `vae` | 用于在放大前对输入潜在变量进行反归一化、并在放大后对输出潜在变量进行归一化的 VAE 模型。 | VAE | Yes |  |

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `LATENT` | 放大后的潜在表示，其空间尺寸与输入相比增加了一倍。输出潜在变量与输入具有相同的批量大小、通道数和时间长度，并被转换回与输入潜在变量相同的数据类型。输入中的 `noise_mask`（如果存在）将从输出中移除。 | LATENT |

注意：此节点标记为实验性。

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVLatentUpsampler/zh.md)

---
**Source fingerprint (SHA-256):** `7d7f0b733cb3758e9ec985cac30134d719b130b5b86c35bfdd14576a5b4575db`
