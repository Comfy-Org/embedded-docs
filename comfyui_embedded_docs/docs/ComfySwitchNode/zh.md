# 切换

Switch 节点根据布尔条件在两个可能的输入之间进行选择。当 `switch` 启用时，它输出 `on_true` 输入；当 `switch` 禁用时，它输出 `on_false` 输入，从而使您能够在工作流中创建条件逻辑并选择不同的数据路径。此节点当前标记为实验性。

## 输入
| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `switch` | 布尔条件，决定传递哪个输入。当启用（true）时，选择 `on_true` 输入。当禁用（false）时，选择 `on_false` 输入。 | BOOLEAN | 是 |  |
| `on_false` | 当 `switch` 禁用（false）时传递给输出的数据。仅当 `switch` 为 false 时需要此输入。 | MATCH_TYPE | 否 |  |
| `on_true` | 当 `switch` 启用（true）时传递给输出的数据。仅当 `switch` 为 true 时需要此输入。 | MATCH_TYPE | 否 |  |

**输入要求说明：** `on_false` 和 `on_true` 输入是条件必需的。节点仅在 `switch` 为 true 时请求 `on_true` 输入，仅在 `switch` 为 false 时请求 `on_false` 输入。两个输入的数据类型必须相同。

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `output` | 选定的数据。如果 `switch` 为 true，则为 `on_true` 输入的值；如果 `switch` 为 false，则为 `on_false` 输入的值。 | MATCH_TYPE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/zh.md)

---
**Source fingerprint (SHA-256):** `d0adda02e7f997f27182cb26e11e934660ae5bd80f3091bed2fed7c981632ce5`
