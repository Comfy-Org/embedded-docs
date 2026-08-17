# 预览任意

PreviewAny 节点接受任意输入值，并在界面中将其显示为可读文本。它用于在工作流中的任意位置检查与调试值：字符串原样显示，数字和布尔值转换为文本，其他对象则格式化为 JSON。转换后的文本也会作为字符串输出传递，以便其他节点使用。

## 输入
| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `source` | 要以文本形式预览的值。接受任意数据类型。字符串原样传递；数字和布尔值转换为文本；其他值序列化为带缩进的 JSON。如果 JSON 序列化失败，则使用该值的纯字符串表示；若同样失败，则显示文本“source exists, but could not be serialized.”。 | ANY | 是 | Any data type |

## 输出
| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `UI Text Display` | 在用户界面中显示已转换为文本的输入数据。同一文本也会作为字符串输出返回，供其他节点进一步处理。 | STRING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/zh.md)

---
**Source fingerprint (SHA-256):** `9572eac396aa27a83148a940e4bf37a9ec4e4a47e9526db8bb983611f9237536`
