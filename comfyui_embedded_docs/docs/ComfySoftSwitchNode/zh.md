# ComfySoftSwitchNode

Soft Switch 节点根据布尔条件在两个可能的输入值之间进行选择。当 `switch` 为 true 时，它输出 `on_true` 输入的值；当 `switch` 为 false 时，它输出 `on_false` 输入的值。该节点设计为惰性节点，即它只根据开关状态计算所需的输入。

## 输入
| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `switch` | 决定传递哪个输入的布尔条件。为 true 时选择 `on_true` 输入，为 false 时选择 `on_false` 输入。 | BOOLEAN | 是 | true<br>false |
| `on_false` | 当 `switch` 条件为 false 时输出的值。此输入为可选，但 `on_false` 和 `on_true` 中至少需要连接一个。 | MATCH_TYPE | 否 |  |
| `on_true` | 当 `switch` 条件为 true 时输出的值。此输入为可选，但 `on_false` 和 `on_true` 中至少需要连接一个。 | MATCH_TYPE | 否 |  |

**注意：** `on_false` 和 `on_true` 输入必须具有相同的数据类型，如节点内部模板所定义。要使节点正常工作，这两个输入中至少需要连接一个。如果仅连接一个输入，则无论 `switch` 状态如何，该值都会传递到输出。

## 输出
| 输出名 | 描述 | 数据类型 |
| --- | --- | --- |
| `output` | 所选值。它将与连接的 `on_false` 或 `on_true` 输入的数据类型匹配。 | MATCH_TYPE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/zh.md)

---
**Source fingerprint (SHA-256):** `7bf4bed69d8fd8c360e971ab8068382cd8ebaa02004d5df44312977a7309ae00`
