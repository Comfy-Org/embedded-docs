# Nano Banana 2

此节点使用 Google 的 Vertex AI Gemini 模型（Nano Banana 2 / Gemini 3.1 Flash Image）同步生成或编辑图像。它会将文本提示以及可选的参考图像或文件发送到 API，并返回生成的图像、任何附带的文本，以及可选地返回模型思考过程中的图像。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述要生成的图像或要应用的编辑的文本提示。请包含模型应遵循的任何约束、样式或细节。必须至少包含一个非空白字符。 | STRING | 是 | N/A |
| `model` | 用于图像生成的特定 Gemini 模型。唯一可用的选项映射到 `gemini-3.1-flash-image-preview` 模型。 | COMBO | 是 | `"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | 当种子固定为特定值时，模型会尽力为重复请求提供相同的响应。但不保证确定性输出。此外，即使使用相同的种子值，更改模型或参数设置（如温度）也可能导致响应发生变化。默认情况下，使用随机种子值。（默认值：42） | INT | 是 | 0 到 18446744073709551615 |
| `aspect_ratio` | 如果设置为 `"auto"`，则与输入图像的宽高比匹配；如果未提供图像，通常生成 16:9 的画面。（默认值：`"auto"`） | COMBO | 是 | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` |
| `resolution` | 目标输出分辨率。对于 2K/4K，使用 Gemini 原生超分辨率器。 | COMBO | 是 | `"1K"`<br>`"2K"`<br>`"4K"` |
| `response_modalities` | 确定模型返回的内容类型：`IMAGE` 仅返回图像，`IMAGE+TEXT` 还会返回模型的推理文本。（高级） | COMBO | 是 | `"IMAGE"`<br>`"IMAGE+TEXT"` |
| `thinking_level` | 控制模型推理过程的深度。 | COMBO | 是 | `"MINIMAL"`<br>`"HIGH"` |
| `images` | 可选的参考图像。要包含多张图像，请使用 Batch Images 节点（最多 14 张）。 | IMAGE | 否 | 最多 14 张图像 |
| `files` | 可选的文件，作为模型的上下文。接受来自 Gemini Generate Content Input Files 节点的输入。 | GEMINI_INPUT_FILES | 否 | N/A |
| `system_prompt` | 决定 AI 行为的基础指令。（默认值：要求模型始终生成图像的内置指令）（高级） | STRING | 否 | N/A |

**注意：** `images` 输入最多接受 14 张图像；提供更多会引发错误。当提供超过 10 张参考图像时，前 10 张会作为文件 URL 发送，其余图像会作为内联数据发送。`prompt` 去除空白字符后不能为空。此节点已标记为弃用。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `image` | 模型生成或编辑的主要图像。 | IMAGE |
| `string` | 模型返回的任何文本内容。 | STRING |
| `thought_image` | 模型思考过程中生成的第一张图像。仅在 `thinking_level` 为 HIGH 且使用 IMAGE+TEXT 模态时可用。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2/zh.md)

---
**Source fingerprint (SHA-256):** `d781c92f04d420985f8a5a593eb5f28f1f7b2af13abd11f2a7f6f285edcd9900`
