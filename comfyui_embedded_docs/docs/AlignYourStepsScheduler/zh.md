# AlignYourSteps调度器

AlignYourStepsScheduler 节点为不同扩散模型类型创建去噪过程中使用的 sigma 值。它会为所选模型挑选基础噪声水平，根据 `denoise` 设置调整步数，并返回一个以 0 结尾的 sigma 值张量。

## 输入
| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model_type` | 用于选择基础噪声水平的模型类型（默认值："SD1"） | COMBO | 是 | `"SD1"`<br>`"SDXL"`<br>`"SVD"` |
| `steps` | 要生成的采样步数总数（默认值：10） | INT | 是 | 1 to 10000 |
| `denoise` | 控制采样过程的使用量：1.0 使用全部步数，较低的值使用较少步数，0.0 返回空的 sigma 张量（默认值：1.0） | FLOAT | 是 | 0.0 to 1.0 |

## 输出
| Output Name | Description | Data Type |
| --- | --- | --- |
| `sigmas` | 去噪过程中计算得到的 sigma 值。如果 `denoise` 为 0.0，则返回空张量。 | SIGMAS |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/zh.md)

---
**Source fingerprint (SHA-256):** `3adbe1016c1ff4b9b7ad3737f50b168f54444d4ca355488e60537d1136f85d3f`
