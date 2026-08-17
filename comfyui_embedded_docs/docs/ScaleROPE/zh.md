# 缩放ROPE

ScaleROPE 节点通过对其 X、Y 和 T（时间）分量应用独立的缩放和偏移因子，来修改模型的旋转位置嵌入（ROPE）。这是一个高级实验性节点，用于调整模型的位置编码行为。

## 输入
| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | 要修改其 ROPE 参数的模型。 | MODEL | Yes | - |
| `scale_x` | 应用于 ROPE 的 X 分量的缩放因子（默认值：1.0）。 | FLOAT | Yes | 0.0 - 100.0 (step 0.1) |
| `shift_x` | 应用于 ROPE 的 X 分量的偏移值（默认值：0.0）。 | FLOAT | Yes | -256.0 - 256.0 (step 0.1) |
| `scale_y` | 应用于 ROPE 的 Y 分量的缩放因子（默认值：1.0）。 | FLOAT | Yes | 0.0 - 100.0 (step 0.1) |
| `shift_y` | 应用于 ROPE 的 Y 分量的偏移值（默认值：0.0）。 | FLOAT | Yes | -256.0 - 256.0 (step 0.1) |
| `scale_t` | 应用于 ROPE 的 T（时间）分量的缩放因子（默认值：1.0）。 | FLOAT | Yes | 0.0 - 100.0 (step 0.1) |
| `shift_t` | 应用于 ROPE 的 T（时间）分量的偏移值（默认值：0.0）。 | FLOAT | Yes | -256.0 - 256.0 (step 0.1) |

## 输出
| Output Name | Description | Data Type |
| --- | --- | --- |
| `model` | 应用了新的 ROPE 缩放和偏移参数的模型。 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ScaleROPE/zh.md)

---
**Source fingerprint (SHA-256):** `5d5ab0182b78c8c12ceaf44685a91e666ce15fa099fd194e3605bbdb9cc3c961`
