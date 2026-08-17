# 调整对比度

调整对比度节点修改输入图像的对比度级别。它通过调整图像亮部和暗部之间的差异来工作。因子为 1.0 时图像保持不变，低于 1.0 时降低对比度，高于 1.0 时增加对比度。

## 输入
| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `image` | 要调整对比度的输入图像。 | IMAGE | 是 | - |
| `factor` | 对比度因子。1.0 = 无变化，<1.0 = 降低对比度，>1.0 = 增加对比度。（默认值：1.0） | FLOAT | 否 | 0.0 - 2.0 |

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `image` | 调整对比度后得到的图像。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustContrast/zh.md)

---
**Source fingerprint (SHA-256):** `1f5fbd0f0b739492bc171d3c43ea2150a3ca76dc3ede9bf63cb97c45a90b9e44`
