# TypeSafe Jev (Score)

TypeSafe Jev (Score) 节点会对连接的文本、图像或两者进行 1 到 10 的评分，并将该评分与阈值进行比较。将 `result` 连接到 If/Else Switch 节点以根据评分执行操作，或读取 `score` 以使用原始评分。这是一个 API 节点：它在 Comfy 的服务器上运行，并且需要拥有带额度的 Comfy.org 账户。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要使用的 Jev 模型。当前只有一个模型可用：`jev-1.14.0`。 | COMBO | 是 | `"jev-1.14.0"` |
| `question` | 要评分的内容，范围为 1 到 10。请说明 1 和 10 分别代表什么，如默认值所示（默认值：`Rate the technical quality of the image from 1 (worst) to 10 (best).`）。 | STRING | 是 | 1 到 1000 个字符 |
| `threshold` | 当评分至少为此值时，`result` 为 true（默认值：5.0）。 | FLOAT | 是 | 1.0 到 10.0（步长：0.1） |
| `images` | 问题所涉及的图像。总共最多 32 张图像；批处理输入会按每张图像分别计数。每张图像的长边会根据图像总数受到限制：最多 4 张图像时为 1568 px，最多 8 张时为 1024 px，最多 16 张时为 768 px，最多 32 张时为 512 px，因此批处理越大，每张图像的细节就越少。 | AUTOGROW | 否 | 0 到 32 张图像 |
| `text` | 问题所涉及的文本，例如提示词或 LLM 响应。 | STRING | 否 | 0 到 3000 个字符 |

**说明：**

- 请连接文本或至少一张图像；当两者都为空时，该节点会引发错误。
- 评分按 1 到 10 报告，当评分至少为 `threshold` 时，`result` 为 true。
- 计费基于 token；节点上的价格徽章显示每 100 万 token 的大致费率。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `result` | 当 `score` 至少为 `threshold` 时为 True。 | BOOLEAN |
| `score` | 从 1（最差）到 10（最好）的评分。 | FLOAT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevScore/zh.md)

---
**Source fingerprint (SHA-256):** `7e1970e903d2099ab3d7481a758c5291e87614b9eaf116d0ced6a1bcd36dc126`
