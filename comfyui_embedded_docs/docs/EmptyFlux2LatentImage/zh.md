# 空Latent图像（Flux2）

EmptyFlux2LatentImage 节点创建一个空白、空的潜在表示。它生成一个填充为零的张量，作为 Flux 模型去噪过程的起点。潜在变量的维度由输入的宽度和高度决定，按 16 倍缩小。

## 输入
| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `width` | 最终生成图像的宽度。潜在宽度将是该值除以 16。默认值为 1024。 | INT | 是 | 16 to 16384 |
| `height` | 最终生成图像的高度。潜在高度将是该值除以 16。默认值为 1024。 | INT | 是 | 16 to 16384 |
| `batch_size` | 单批生成的潜在样本数量。默认值为 1。 | INT | 否 | 1 to 4096 |

**注意：** `width` 和 `height` 输入必须能被 16 整除，因为节点内部会除以该因子来创建潜在维度。

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `samples` | 填充为零的潜在张量。形状为 `[batch_size, 128, height // 16, width // 16]`。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyFlux2LatentImage/zh.md)

---
**Source fingerprint (SHA-256):** `f8356568f0ab521a3f246d1f672492e74f9a2f449694961b913bd14a5f0f3878`
