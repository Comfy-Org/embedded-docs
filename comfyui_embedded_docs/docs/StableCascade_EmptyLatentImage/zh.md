# 空Latent图像（Stable Cascade）

StableCascade_EmptyLatentImage 节点为 Stable Cascade 模型创建空的潜在张量。它会生成两个独立的潜在表示——一个用于 C 阶段，另一个用于 B 阶段——其维度根据输入分辨率和压缩设置确定。此节点为 Stable Cascade 生成流程提供起点。

## 输入
| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `width` | 输出图像的宽度（像素）（默认值：1024，步长：8） | INT | 是 | 256 to MAX_RESOLUTION |
| `height` | 输出图像的高度（像素）（默认值：1024，步长：8） | INT | 是 | 256 to MAX_RESOLUTION |
| `compression` | 用于确定 C 阶段潜在维度的压缩因子（默认值：42，步长：1）。这是一个高级参数。 | INT | 是 | 4 to 128 |
| `batch_size` | 每批生成的潜在样本数量（默认值：1） | INT | 否 | 1 to 4096 |

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `stage_c` | C 阶段潜在张量，维度为 [batch_size, 16, height//compression, width//compression] | LATENT |
| `stage_b` | B 阶段潜在张量，维度为 [batch_size, 4, height//4, width//4] | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/zh.md)

---
**Source fingerprint (SHA-256):** `f336f87d0ec14b3716efda2cfaa194b1f80707d64821bb56ade7d88d9bd5b53f`
