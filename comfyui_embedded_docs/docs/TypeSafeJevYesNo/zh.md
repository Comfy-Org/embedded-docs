# TypeSafe Jev (Yes/No)

TypeSafe Jev (Yes/No) 节点针对已连接的文本、图像或二者提出一个是/否问题，并将答案作为布尔值返回。将 `result` 连接到 If/Else Switch 节点以路由工作流，或读取 `probability` 以根据模型的确定程度执行操作。这是一个 API 节点，需要 Comfy.org 账号和 API 密钥。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要使用的 Jev 模型。目前只有一个模型可用：`jev-1.14.0`。 | COMBO | 是 | `"jev-1.14.0"` |
| `question` | 已连接的文本和图像要回答的是/否问题。提问时应使“是”对应你要采取行动的情况；如果有多个图像插槽，请使用它们的名称，例如 `image_2 是否与 image_1 显示同一个人？`（默认：`图像中有一个人吗？`）。 | STRING | 是 | 1 到 1000 个字符 |
| `threshold` | 当“是”的概率至少达到此值时，答案为“是”（默认：0.5）。 | FLOAT | 是 | 0.01 到 0.99（步长 0.01） |
| `images` | 问题所涉及的图像。总共最多 32 张图像；批量输入中的每张图像各计一次，超过 4 张图像时会以较小尺寸发送。 | AUTOGROW | 否 | 0 到 32 张图像 |
| `text` | 问题所涉及的文本，例如提示词或 LLM 响应。 | STRING | 否 | 0 到 3000 个字符 |

**注意：**

- 连接文本或至少一张图像；当二者均为空时，节点会报错。
- 当 `probability` 至少为 `threshold` 时，`result` 为 true，并且 `answer` 会以 `yes` 或 `no` 返回相同的判定。
- 计费基于 token；节点上的价格徽章显示每 100 万 token 的近似费率。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `result` | 作为布尔值的答案：当“是”的概率至少为 `threshold` 时为 true。 | BOOLEAN |
| `answer` | 以文本 `yes` 或 `no` 表示的答案。 | STRING |
| `probability` | “是”的概率，从 0（肯定为否）到 1（肯定为是）。 | FLOAT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevYesNo/zh.md)

---
**Source fingerprint (SHA-256):** `e8c7de5558c61e7c9058b28104a72d8d8961165983d02d63a5c9078c40855385`
