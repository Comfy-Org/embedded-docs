# TypeSafe Jev (Choice)

TypeSafe Jev (Choice) 节点会从你自定义的选项中，为所连接的文本、图像或两者选出其中一项。将 `choice` 连接到 Branch 节点，该节点的输入即为各选项名称；也可使用 `option_index` 按所选选项的位置进行切换。这是一个 API 节点，需要 Comfy.org 账号和 API 密钥。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要使用的 Jev 模型。目前仅有一个模型可用：`jev-1.14.0`。 | COMBO | 是 | `"jev-1.14.0"` |
| `question` | 各选项所回答的问题。当存在多个图像输入端口时，请使用它们的名称，例如 `Which season is shown in image_1?`（默认：`What style is the image?`）。 | STRING | 是 | 1 到 1000 个字符 |
| `options` | 可供选择的选项，每行一个。可为不符合任何选项的输入添加诸如 `other` 的选项（默认：`photo`、`illustration`、`3d render`、`anime`、`sketch` 和 `other`，每行一个）。 | STRING | 是 | 2 到 50 个选项，每个不超过 40 个字符 |
| `images` | 问题所涉及的图像。总共最多 32 张图像；批处理的输入每张图像各计一次，超过 4 张图像时将以较小的尺寸发送。 | AUTOGROW | 否 | 0 到 32 张图像 |
| `text` | 问题所涉及的文本，例如提示词或 LLM 响应。 | STRING | 否 | 0 到 3000 个字符 |

**说明：**

- 请连接文本或至少一张图像；当两者均为空时，节点会报错。
- 当给定的选项少于 2 个或多于 50 个、当某个选项超过 40 个字符，或当两个选项仅字母大小写不同时，节点会报错。
- `option_index` 从 0 开始计数，因此列表中的第一个选项索引为 0。
- 计费基于 token；节点上的价格徽章显示每 1M token 的大致费率。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `choice` | 所选中的选项，与 `options` 中显示的完全一致。 | STRING |
| `option_index` | 所选选项在选项列表中的位置，从 0 开始。 | INT |
| `confidence` | Jev 的确定程度，从 0（没有明确胜出者）到 1（确定）。 | FLOAT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevChoice/zh.md)

---
**Source fingerprint (SHA-256):** `b1cd36d600f5c07935c455d9e926e6c0a53f172fcc1a6f602c8d4dc70eeffabe`
