# Hunyuan Video 15 Latent 使用模型放大

## 输入
| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 用于细化放大后样本的 Hunyuan Video 1.5 潜在放大模型。 | LATENT_UPSCALE_MODEL | 是 | N/A |
| `samples` | 要放大的潜在图像表示。 | LATENT | 是 | N/A |
| `upscale_method` | 用于初始放大步骤的插值算法（默认：`"bilinear"`）。 | COMBO | 否 | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` |
| `width` | 放大后潜在空间的目标宽度（以像素为单位）。值为 0 时将根据目标高度和原始宽高比自动计算宽度。最终输出宽度将是 16 的倍数（默认：1280）。 | INT | 否 | 0 to 16384 (step 8) |
| `height` | 放大后潜在空间的目标高度（以像素为单位）。值为 0 时将根据目标宽度和原始宽高比自动计算高度。最终输出高度将是 16 的倍数（默认：720）。 | INT | 否 | 0 to 16384 (step 8) |
| `crop` | 决定如何裁剪放大后的潜在空间以匹配目标尺寸。 | COMBO | 否 | `"disabled"`<br>`"center"` |

**关于尺寸的说明：** 如果 `width` 和 `height` 均设置为 0，则节点原样返回输入的 `samples`。如果仅有一个维度设置为 0，则另一维度会根据原始宽高比自动计算。最终尺寸始终会调整为至少 64 像素，且可被 16 整除。

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `LATENT` | 放大并经过模型细化后的潜在图像表示。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/zh.md)

---
**Source fingerprint (SHA-256):** `71af49eefb010aadd30f8699b751ad901b1ee385d6cbeedd3a83995a1a623516`
