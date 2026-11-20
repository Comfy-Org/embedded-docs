# Google Gemini Decision (Yes/No)

对你连接的文本、图像、音频或视频提出一个是/否问题，并获得一个可用于路由的布尔值。将 `result` 连接到 If/Else Switch 节点，把运行导向两条路径之一；当你想了解模型为何这样回答时，可以读取 `answer` 和 `probability`。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要使用的模型（默认：`"gemini-decision-1"`）。 | COMBO | 是 | `"gemini-decision-1"` |
| `question` | 关于所连接内容的是/否问题，最多 5000 个字符。提问时应使「是」对应你希望采取行动的情况（默认："Is there a person in the image?"）。 | STRING | 是 | 1 到 5000 个字符 |
| `threshold` | `result` 变为 true 所需的「是」概率阈值。明确的肯定回答得分约为 0.85 到 0.92，因此 0.9 及以上会拒绝其中许多回答（默认：0.5）。 | FLOAT | 是 | 0.01 到 0.99（步长 0.01） |
| `images` | 要提问的图像，在各可扩展插槽（`image_1` ... `image_16`）中最多 16 张。批处理的图像按每张图像计一次。 | IMAGE | 否 | 最多 16 张图像 |
| `audio` | 要提问的音频片段。 | AUDIO | 否 | - |
| `video` | 要提问的视频片段。 | VIDEO | 否 | - |
| `text` | 问题所针对的文本，例如提示词或 LLM 回复，最多 20000 个字符。 | STRING | 否 | 最多 20000 个字符 |

至少连接 `text`、`images`、`audio` 或 `video` 中的一项；当没有任何可供查看的内容时，该节点会报错。若有多张图像，请在问题中用 `image_1`、`image_2` 等名称来指代它们。

## 输出

| 输出名 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `result` | 以布尔值表示的答案：true 表示「是」，false 表示「否」。 | BOOLEAN |
| `answer` | 以字符串 `"yes"` 或 `"no"` 表示的答案。 | STRING |
| `probability` | 「是」的概率，介于 0 和 1 之间。 | FLOAT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionYesNo/zh.md)

---
**Source fingerprint (SHA-256):** `0339031baf5648609b82526bed97ce8744986878bcbb706dcd3aa79a7370d83f`
