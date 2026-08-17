# 文本音频编码（AceStep）

TextEncodeAceStepAudio 节点通过将标签和歌词组合成词元，并以可调的歌词强度进行编码，来处理用于音频条件生成的文本输入。它接收一个 CLIP 模型以及文本描述和歌词，将它们一起进行词元化，并生成适用于音频生成任务的条件数据。该节点通过一个控制歌词对最终输出影响力的强度参数，允许对歌词的影响进行微调。

## 输入
| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `clip` | 用于词元化和编码的 CLIP 模型 | CLIP | 是 | - |
| `tags` | 用于音频条件生成的文本标签或描述（支持多行输入和动态提示） | STRING | 是 | - |
| `lyrics` | 用于音频条件生成的歌词文本（支持多行输入和动态提示） | STRING | 是 | - |
| `lyrics_strength` | 控制歌词对条件输出影响的程度（默认值：1.0，步长：0.01） | FLOAT | 否 | 0.0 - 10.0 |

## 输出
| Output Name | Description | Data Type |
| --- | --- | --- |
| `conditioning` | 包含已处理文本词元并应用了歌词强度的编码条件数据 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio/zh.md)

---
**Source fingerprint (SHA-256):** `2226c9f25dd26bf454bcce2e298d6d261dace5a9bbed164a2fcf0e1204d7c3f4`
