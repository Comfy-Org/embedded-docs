# HeyGen Decision (Yes/No)

针对你连接的文本、图像、音频或视频提出一个是/否问题，并得到一个可用于路由的布尔值。将 `result` 连接到 If/Else Switch 节点，即可在两条路径之间进行选择；读取 `answer` 和 `probability` 可以了解答案的明确程度。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要使用的模型。`heygen-decision-1-turbo` 比 `heygen-decision-1` 更快且成本更低（默认：`"heygen-decision-1"`）。 | COMBO | 是 | `"heygen-decision-1"`<br>`"heygen-decision-1-turbo"` |
| `question` | 关于所连接内容的 yes/no 问题，最多 5000 个字符。提问时应让 "yes" 对应你希望采取行动的情况（默认："Is there a person in the image?"）。 | STRING | 是 | 1 到 5000 个字符 |
| `threshold` | `result` 变为 true 时 "yes" 的概率阈值；明确的答案接近 0 或 1（默认：0.5）。 | FLOAT | 是 | 0.01 到 0.99（步长 0.01） |
| `images` | 要询问的图像，总共最多 4 张，将批次中的每一帧都计算在内。它们按插座顺序依次编号为 `image_1` 到 `image_4`。 | IMAGE | 否 | 最多 4 张图像 |
| `audio_1` | 要询问的音频，最长 30 分钟。 | AUDIO | 否 | 最多 30 分钟 |
| `video_1` | 要询问的视频，最长 60 秒。 | VIDEO | 否 | 最多 60 秒 |
| `text` | 问题所针对的文本，例如提示词或 LLM 回复，最多 20000 个字符。 | STRING | 否 | 最多 20000 个字符 |

至少连接 `text`、`images`、`audio_1` 或 `video_1` 中的一项，并在问题中通过插座名称引用它们，例如 "Does image_2 show the same person as image_1?"。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `result` | 以布尔值表示的答案：true 表示 "yes"，false 表示 "no"。 | BOOLEAN |
| `answer` | 以字符串 `"yes"` 或 `"no"` 表示的答案。 | STRING |
| `probability` | "yes" 的概率，取值在 0 到 1 之间。 | FLOAT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenDecisionYesNo/zh.md)

---
**Source fingerprint (SHA-256):** `5a6a606d5c6ef62eb3424bd54a0da3dc177da7d0acf4b5c235a62b78ad8d2df1`
