# Nano Banana Pro（Google Gemini 图像）

Nano Banana Pro (Google Gemini Image) 使用 Google 的 Vertex AI Gemini 图像模型生成或编辑图像。它将文本提示以及可选的参考图像或文件发送到 Gemini API，并返回生成的图像以及可选的文本响应。

## 输入
| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述要生成的图像或要应用的编辑的文本提示。可包含模型应遵循的任何约束、样式或细节。默认值：空字符串。 | STRING | 是 | N/A |
| `model` | 要使用的 Gemini 图像模型。“Nano Banana 2 (Gemini 3.1 Flash Image)”选项作为 `gemini-3.1-flash-image` 发送到 API；“gemini-3-pro-image-preview”作为 `gemini-3-pro-image` 发送。 | COMBO | 是 | `"gemini-3-pro-image-preview"`<br>`"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | 当种子固定为特定值时，模型会尽力为重复请求提供相同的响应。不保证确定性输出。即使使用相同的种子值，更改模型或其他参数设置也可能导致响应变化。默认值：42。 | INT | 是 | 0 到 18446744073709551615 |
| `aspect_ratio` | 输出图像所需的宽高比。如果设置为“auto”，则会匹配输入图像的宽高比；如果没有提供图像，通常会生成一张 16:9 的图像。默认值：“auto”。 | COMBO | 是 | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` |
| `resolution` | 目标输出分辨率。对于 2K/4K，使用 Gemini 原生超分辨率器。 | COMBO | 是 | `"1K"`<br>`"2K"`<br>`"4K"` |
| `response_modalities` | 选择“IMAGE”仅输出图像，或选择“IMAGE+TEXT”同时返回生成的图像和文本响应。 | COMBO | 是 | `"IMAGE+TEXT"`<br>`"IMAGE"` |
| `images` | 用作视觉上下文的可选参考图像。要包含多张图像，请使用 Batch Images 节点（最多 14 张）。 | IMAGE | 否 | N/A |
| `files` | 用作模型上下文的可选文件。接受来自 Gemini Generate Content Input Files 节点的输入。 | GEMINI_INPUT_FILES | 否 | N/A |
| `system_prompt` | 用于规定模型行为的基础指令。默认值：预定义的系统提示，指示模型始终生成图像。 | STRING | 否 | N/A |

**约束条件：**

* `prompt` 去除首尾空白后不能为空；否则会引发错误。
* `images` 输入最多接受 14 张图像。如果提供超过 14 张，则会引发错误。
* `files` 输入必须连接到输出 `GEMINI_INPUT_FILES` 数据类型的节点。

## 输出
| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `image` | Gemini 模型生成或编辑的图像。 | IMAGE |
| `string` | 模型的文本响应。当 `response_modalities` 设置为“IMAGE”时，此输出为空。 | STRING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/zh.md)

---
**Source fingerprint (SHA-256):** `02293dad786d4b441da3174fa76f6c5847f122d294bd7e1f765ffd72420034a4`
