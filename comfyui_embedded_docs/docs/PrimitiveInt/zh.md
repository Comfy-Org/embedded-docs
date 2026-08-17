# 整数

PrimitiveInt 节点提供了一种在工作流中处理整数值的简单方法。它接受一个整数输入并输出相同的值，这对于在节点之间传递整数参数或为其他操作设置特定的数值非常有用。

## 输入
| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `value` | 要输出的整数值（默认值：0） | INT | 是 | -9223372036854775807 至 9223372036854775807 |

注意：`value` 参数被设置为固定的生成后控制行为，因此该值不会在每次生成后自动更改。

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `output` | 原样传递输入的整数值 | INT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveInt/zh.md)

---
**Source fingerprint (SHA-256):** `b928ec40c781043c1c8652de3aebedc755d9b63be9e2c773e3fb26ce4d594bba`
