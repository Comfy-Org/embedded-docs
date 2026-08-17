# TextGenerateLTX2Prompt

TextGenerateLTX2Prompt 节点是文本生成节点的专门版本。它接收用户的文本提示，并自动使用 LTX2 特定的系统指令进行格式化，然后再发送给语言模型进行增强或补全。该节点可以在纯文本模式或图像参考模式下工作，并会根据所连接的 CLIP 模型自动调整其格式：对于 Gemma 4 模型使用 LTX 2.4 提示格式，对于 Gemma 3 模型则使用 LTX 2.0 格式。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `clip` | 用于文本编码的 CLIP 模型。该模型决定提示格式：Gemma 4 模型使用 LTX 2.4 格式，Gemma 3 模型使用 LTX 2.0 格式。 | CLIP | 是 |  |
| `prompt` | 用户提供的原始文本输入，将被增强或补全。 | STRING | 是 |  |
| `max_length` | 语言模型允许生成的最大 token 数量。 | INT | 是 |  |
| `sampling_mode` | 文本生成期间用于选择下一个 token 的采样策略。 | COMBO | 是 | `"greedy"`<br>`"top_k"`<br>`"top_p"`<br>`"temperature"` |
| `image` | 可选的输入图像。当提供时，节点使用包含图像上下文的不同系统提示，用于图像到视频的生成。 | IMAGE | 否 |  |
| `thinking` | 启用后，模型将在最终答案之前输出其推理过程。推理块会从最终结果中移除。 | BOOLEAN | 否 |  |
| `use_default_template` | 启用后，节点将使用默认聊天模板进行格式化。 | BOOLEAN | 否 |  |
| `video` | 可选的视频输入，可用作生成的额外上下文。 | VIDEO | 否 |  |
| `audio` | 可选的音频输入，可用作生成的额外上下文。 | AUDIO | 否 |  |

**说明：** 节点的行为会根据 `image` 输入是否存在而变化。如果提供了图像，提示会被格式化为图像到视频任务，使用一个系统提示根据图像内容对提示进行扩展。如果未提供图像，则格式化为文本到视频任务，使用一个系统提示将提示扩展为详细的视频生成描述。

所连接的 `clip` 模型也会影响格式化：当 CLIP tokenizer 是 Gemma 4 模型时，节点使用 LTX 2.4 聊天格式和系统提示；否则使用 Gemma 3 / LTX 2.0 聊天格式。生成之后，任何推理块（例如 `<think>...</think>`）都会从输出中移除；如果结果文本为空，则返回原始 `prompt`。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `output` | 由语言模型生成的增强或补全文本字符串，已移除任何推理内容。如果模型未生成任何文本，则返回原始提示。 | STRING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/zh.md)

---
**Source fingerprint (SHA-256):** `8f524ea60a247217dde8a1edaf7a689e253ae05acc9eb52ad47b91e879dba1df`
