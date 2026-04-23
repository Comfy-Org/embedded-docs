> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2/zh.md)

GeminiNanoBanana2 节点使用 Google 的 Vertex AI Gemini 模型来生成或编辑图像。其工作原理是向 API 发送一个文本提示，以及可选的参考图像或文件，并返回生成的图像和任何附带的文本。

## 输入参数

| 参数 | 数据类型 | 必填 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | 不适用 | 描述要生成图像或应用编辑的文本提示。包含模型应遵循的任何约束、风格或细节。 |
| `model` | COMBO | 是 | `"Nano Banana 2 (Gemini 3.1 Flash Image)"` | 用于图像生成的具体 Gemini 模型。 |
| `seed` | INT | 是 | 0 到 18446744073709551615 | 当种子固定为特定值时，模型会尽力为重复请求提供相同的响应。不保证输出是确定性的。此外，更改模型或参数设置（例如温度）可能会导致响应发生变化，即使使用相同的种子值。默认使用随机种子值。（默认值：42） |
| `aspect_ratio` | COMBO | 是 | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` | 如果设置为 'auto'，则匹配输入图像的宽高比；如果未提供图像，通常生成 16:9 的正方形。（默认值："auto"） |
| `resolution` | COMBO | 是 | `"1K"`<br>`"2K"`<br>`"4K"` | 目标输出分辨率。对于 2K/4K，使用 Gemini 原生超分功能。 |
| `response_modalities` | COMBO | 是 | `"IMAGE"`<br>`"IMAGE+TEXT"` | 决定模型将返回的内容类型。（高级） |
| `thinking_level` | COMBO | 是 | `"MINIMAL"`<br>`"HIGH"` | 控制模型推理过程的深度。 |
| `images` | IMAGE | 否 | 不适用 | 可选的参考图像。要包含多张图像，请使用 Batch Images 节点（最多 14 张）。 |
| `files` | CUSTOM | 否 | 不适用 | 可选文件，用作模型的上下文。接受来自 Gemini Generate Content Input Files 节点的输入。 |
| `system_prompt` | STRING | 否 | 不适用 | 规定 AI 行为的基础指令。（高级） |

**注意：** `images` 输入最多支持 14 张图像。如果提供更多，节点将引发错误。

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `image` | IMAGE | 模型生成或编辑的主要图像。 |
| `string` | STRING | 模型返回的任何文本内容。 |
| `thought_image` | IMAGE | 模型思考过程中的第一张图像。仅在 thinking_level 为 HIGH 且 response_modalities 为 IMAGE+TEXT 时可用。 |