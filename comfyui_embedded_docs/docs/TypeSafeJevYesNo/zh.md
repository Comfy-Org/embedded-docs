# TypeSafe Jev (Yes/No)

TypeSafe Jev (Yes/No) 节点针对已连接的文本、图像或两者提出一个是/否问题，并以布尔值形式返回答案。将 `result` 连接到 If/Else Switch 节点即可对工作流进行路由，或读取 `probability` 以便根据模型的确定程度采取相应操作。这是一个 API 节点：它运行在 Comfy 的服务器上，需要拥有带额度的 Comfy.org 账户。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要使用的 Jev 模型。目前只有一个模型可用：`jev-1.14.0`。 | COMBO | 是 | `"jev-1.14.0"` |
| `question` | 由已连接的文本和图像来回答的是/否问题。提问时应使「是」对应你希望采取操作的情况；当存在多个图像输入接口时，请使用它们的名称，例如 `Does image_2 show the same person as image_1?`（默认：`Is there a person in the image?`）。 | STRING | 是 | 1 到 1000 个字符 |
| `threshold` | 当「是」的概率至少达到该值时，答案即为「是」（默认：0.5）。 | FLOAT | 是 | 0.01 到 0.99（步长 0.01） |
| `images` | 问题所针对的图像。图像总数最多为 32 张；批处理输入按每张图像各计一次。每张图像的长边会根据图像总数受到限制：最多 4 张图像时为 1568 px，最多 8 张时为 1024 px，最多 16 张时为 768 px，最多 32 张时为 512 px，因此批次越大，每张图像的细节就越少。 | AUTOGROW | 否 | 0 到 32 张图像 |
| `text` | 问题所针对的文本，例如提示词或 LLM 的回复。 | STRING | 否 | 0 到 3000 个字符 |

**注意：**

- 请连接文本或至少一张图像；当两者均为空时，节点会报错。
- 当 `probability` 至少达到 `threshold` 时，`result` 为 true，而 `answer` 以 `yes` 或 `no` 返回相同的判定结果。
- 计费基于 token；节点上的价格标签显示了每 1M token 的大致费率。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `result` | 以布尔值表示的答案：当「是」的概率至少达到 `threshold` 时为 true。 | BOOLEAN |
| `answer` | 以文本 `yes` 或 `no` 表示的答案。 | STRING |
| `probability` | 「是」的概率，从 0（肯定为否）到 1（肯定为是）。 | FLOAT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevYesNo/zh.md)

---
**Source fingerprint (SHA-256):** `e8c7de5558c61e7c9058b28104a72d8d8961165983d02d63a5c9078c40855385`
