# ARVideoI2V

## 概述
此节点为 AR（自回归）视频模型准备图像到视频的生成设置。它接收一个起始图像，使用 VAE 将其编码到潜在空间中，并将编码后的图像存储到模型的配置中。这样，视频采样过程就可以将该图像作为第一帧使用，从而无需单独的图像到视频模型架构即可有效初始化生成过程。

## 输入
| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 用于生成的 AR 视频模型。 | MODEL | 是 | - |
| `vae` | 用于将起始图像编码到潜在空间的 VAE 模型。 | VAE | 是 | - |
| `start_image` | 将作为生成视频第一帧的初始图像。 | IMAGE | 是 | - |
| `width` | 生成视频帧的宽度（默认值：832）。 | INT | 是 | 16 to 8192 (step: 16) |
| `height` | 生成视频帧的高度（默认值：480）。 | INT | 是 | 16 to 8192 (step: 16) |
| `length` | 生成视频的总帧数（默认值：81）。 | INT | 是 | 1 to 1024 (step: 4) |
| `batch_size` | 单个批次中生成的视频序列数量（默认值：1）。 | INT | 是 | 1 to 64 |

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `MODEL` | 克隆后的模型，其配置中存储了编码后的起始图像，用于视频生成。 | MODEL |
| `LATENT` | 一个空的潜在张量，形状为 [batch_size, 16, lat_t, height/8, width/8]，其中 lat_t = ((length - 1) // 4) + 1 是根据请求的视频长度推导出的潜在帧数。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ARVideoI2V/zh.md)

---
**Source fingerprint (SHA-256):** `984834951b9d5a22aef51c85a5019fd8ba58cdb2d6fff235371ed29f316896d8`
