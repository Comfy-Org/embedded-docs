# TypeSafe Jev (Choice)

TypeSafe Jev (Choice) 节点会从你自己提供的选项中，为连接的文本、图像或两者选择一项。将 `choice` 连接到 Branch 节点，该节点的输入携带选项名称；或使用 `option_index` 根据所选选项的位置进行切换。Branch 节点最多接受 32 个输入，因此选项数量超过该限制的列表只能通过 `option_index` 进行路由。这是一个 API 节点：它在 Comfy 的服务器上运行，并且需要带有积分的 Comfy.org 账户。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要使用的 Jev 模型。目前只有一个模型可用：`jev-1.14.0`。 | COMBO | 是 | `"jev-1.14.0"` |
| `question` | 选项所回答的问题。当存在多个图像插槽时，使用它们的名称，例如 `Which season is shown in image_1?`（默认：`What style is the image?`）。 | STRING | 是 | 1 到 1000 个字符 |
| `options` | 可供选择的选项，每行一个。每行开头和结尾的空白字符会被去除，并且选项必须唯一（忽略大小写），因此重复选项或仅大小写不同的两个选项会被拒绝。为不符合任何选项的输入添加一个诸如 `other` 的选项（默认：`photo`、`illustration`、`3d render`、`anime`、`sketch` 和 `other`，每行一个）。 | STRING | 是 | 2 到 50 个选项，每个最多 40 个字符 |
| `images` | 问题所涉及的图像。总共最多 32 张图像；批量输入按每张图像计一次。每张图像的长边受图像总数限制：最多 4 张图像时为 1568 px，最多 8 张时为 1024 px，最多 16 张时为 768 px，最多 32 张时为 512 px，因此较大的批次会降低每张图像的细节。 | AUTOGROW | 否 | 0 到 32 张图像 |
| `text` | 问题所涉及的文本，例如提示词或 LLM 响应。 | STRING | 否 | 0 到 3000 个字符 |

**注意：**

- 连接文本或至少一张图像；当两者都为空时，节点会报错。
- 当提供的选项少于 2 个或多于 50 个、某个选项超过 40 个字符，或两个选项忽略大小写后相同时，节点会报错。
- `option_index` 从 0 开始计数，因此列表中的第一个选项索引为 0。
- 计费基于 token；节点上的价格徽章显示每 100 万 token 的大致费率。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `choice` | 所选选项，已去除开头和结尾的空白字符。如果某个 Branch 输入的名称保留了这些空格，将无法匹配。 | STRING |
| `option_index` | 所选选项在选项列表中的位置，从 0 开始。 | INT |
| `confidence` | Jev 的确信程度，从 0（没有明显胜出者）到 1（确定）。 | FLOAT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevChoice/zh.md)

---
**Source fingerprint (SHA-256):** `b1cd36d600f5c07935c455d9e926e6c0a53f172fcc1a6f602c8d4dc70eeffabe`
