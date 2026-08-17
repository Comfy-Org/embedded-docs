# Nano Banana 2

此节点通过 Gemini 图像模型将文本提示发送到 Google Vertex AI API，从而生成或编辑图像。它可以根据描述创建新图像，或使用可选的参考图像修改现有图像。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 选择要使用的 Gemini 图像模型。所选模型决定了可用的分辨率选项和特定于模型的输入。 | DYNAMIC_COMBO | 是 | `"Nano Banana 2 (Gemini 3.1 Flash Image)"`<br>`"Nano Banana 2 Lite"` |
| `prompt` | 描述要生成的图像或要应用的编辑的文本提示。包含模型应遵循的任何约束、样式或细节。不能为空。（默认：空） | STRING | 是 | N/A |
| `seed` | 当种子固定为特定值时，模型会尽最大努力为重复请求提供相同的响应。但不保证输出一定确定。此外，即使使用相同的种子值，更改模型或参数设置（例如 temperature）也可能导致响应发生变化。默认使用随机种子值。（默认：42） | INT | 是 | 0 到 18446744073709551615 |
| `response_modalities` | 确定响应格式。IMAGE 仅返回图像；IMAGE+TEXT 返回图像和文本响应。（默认：IMAGE）高级参数。 | COMBO | 是 | `"IMAGE"`<br>`"IMAGE+TEXT"` |
| `system_prompt` | 规定 AI 行为的基础指令。如果留空，将使用指示模型始终生成图像的内置提示。高级参数。 | STRING | 否 | N/A |
| `temperature` | 控制生成时的随机性。数值越低，结果越集中/确定。（默认：1.0）高级参数。 | FLOAT | 否 | 0.0 到 2.0（步长 0.01） |
| `top_p` | 核采样阈值。数值越低越集中，越高越多样。（默认：0.95）高级参数。 | FLOAT | 否 | 0.0 到 1.0（步长 0.01） |

### Nano Banana 2 (Gemini 3.1 Flash Image) 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | 如果设置为 'auto'，则匹配输入图像的宽高比；如果没有提供图像，通常生成 16:9 的图像。（默认：auto） | COMBO | 是 | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"`<br>`"1:4"`<br>`"4:1"`<br>`"8:1"`<br>`"1:8"` |
| `resolution` | 目标输出分辨率。 | COMBO | 是 | `"1K"`<br>`"2K"`<br>`"4K"` |
| `thinking_level` | 选择模型使用的思考级别。 | COMBO | 是 | `"MINIMAL"`<br>`"HIGH"` |

### Nano Banana 2 Lite 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | 如果设置为 'auto'，则匹配输入图像的宽高比；如果没有提供图像，通常生成 16:9 的图像。（默认：auto） | COMBO | 是 | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"`<br>`"1:4"`<br>`"4:1"`<br>`"8:1"`<br>`"1:8"` |
| `resolution` | 目标输出分辨率。 | COMBO | 是 | `"1K"` |
| `thinking_level` | 选择模型使用的思考级别。 | COMBO | 是 | `"MINIMAL"`<br>`"HIGH"` |

### 参考输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `images` | 可选的参考图像。总共最多 14 张图像。可增长插槽：连接 `image_1` 到 `image_14`。 | IMAGE | 否 | 0 到 14 张图像 |
| `files` | 可选的用作模型上下文的文件。接受来自 Gemini Generate Content Input Files 节点的输入。 | GEMINI_INPUT_FILES | 否 | N/A |

**注意：** 最多可将 14 张参考图像连接到 `images` 输入。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `IMAGE` | 生成的或编辑后的图像。 | IMAGE |
| `STRING` | 模型生成的文本描述或说明。当没有返回文本时为空，例如当 `response_modalities` 设置为 `IMAGE` 时。 | STRING |
| `thought_image` | 模型思考过程中产生的第一张图像。仅在 `thinking_level` 为 HIGH 且使用 IMAGE+TEXT 模式时可用。 | IMAGE |

**注意：** 当 `response_modalities` 设置为 `IMAGE` 时，`STRING` 输出为空。

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2V2/zh.md)

---
**Source fingerprint (SHA-256):** `347d28aeb46aa91f7515a31c385a3e3f805a1861116a21dd2ef6575ab7fd4f3e`
