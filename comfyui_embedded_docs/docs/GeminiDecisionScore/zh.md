# Google Gemini Decision (Score)

对你连接的文本、图像、音频或视频进行 1 到 10 的评分，并获得分数以及一个在你设置的阈值处翻转的布尔值。可用它来筛选或排序输出，例如仅保留评分至少为 7 的图像，并将 `result` 连接到 If/Else Switch 节点以据此执行操作。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要使用的模型（默认：`"gemini-decision-1"`）。 | COMBO | 是 | `"gemini-decision-1"` |
| `question` | 要评分的内容，并说明 1 和 10 分别代表什么（默认："Rate the technical quality of the image from 1 (worst) to 10 (best)."）。 | STRING | 是 | 1 到 5000 个字符 |
| `threshold` | 当分数至少为此值时，`result` 为 true。清晰锐利的图像评分约为 7 到 8，严重损坏的图像约为 3 到 5（默认：6.0）。 | FLOAT | 是 | 1.0 到 10.0（步长：0.1） |
| `images` | 要评分的图像，通过可增长槽位（`image_1` ... `image_16`）最多 16 张。批量图像中的每张图像各计一次。 | IMAGE | 否 | 最多 16 张图像 |
| `audio` | 要评分的音频片段。 | AUDIO | 否 | - |
| `video` | 要评分的视频片段。 | VIDEO | 否 | - |
| `text` | 问题所针对的文本，例如提示词或 LLM 响应，最多 20000 个字符。 | STRING | 否 | 最多 20000 个字符 |

至少连接 `text`、`images`、`audio` 或 `video` 中的一项；当没有任何可评分内容时，节点会报错。如果有多张图像，请在问题中分别命名为 `image_1`、`image_2` 等。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `result` | 当分数至少为 `threshold` 时为 True，否则为 False。 | BOOLEAN |
| `score` | 1 到 10 的评分。 | FLOAT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionScore/zh.md)

---
**Source fingerprint (SHA-256):** `9b0a68cc7f29b1d4d23e23e051a008f34932aac6d1fe1a16e45a0e70b4df412f`
