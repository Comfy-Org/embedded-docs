# Google Gemini

此节点允许用户与 Google 的 Gemini AI 模型交互，以生成文本响应。您可以提供多种类型的输入，包括文本、图像、音频、视频和文件，作为模型的上下文，以生成更相关、更有意义的响应。该节点会自动处理所有 API 通信和响应解析。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 输入给模型的文本，用于生成响应。您可以包含详细的指令、问题或上下文。默认值：空字符串。 | STRING | 是 | - |
| `model` | 用于生成响应的 Gemini 模型。默认值：gemini-3-1-pro。 | COMBO | 是 | "gemini-2.5-pro"<br>"gemini-2.5-flash"<br>"gemini-3-pro-preview"<br>"gemini-3-1-pro"<br>"gemini-3-1-flash-lite" |
| `seed` | 当 `seed` 固定为特定值时，模型会尽力为重复请求提供相同的响应。但不保证确定性输出。此外，即使使用相同的 `seed` 值，更改模型或参数设置（例如 temperature）也可能导致响应发生变化。默认情况下，使用随机种子值。默认值：42。 | INT | 是 | 0 to 18446744073709551615 |
| `images` | 可选。用作模型上下文的图像。要包含多张图像，可以使用 Batch Images 节点。默认值：无。 | IMAGE | 否 | - |
| `audio` | 可选。用作模型上下文的音频。默认值：无。 | AUDIO | 否 | - |
| `video` | 可选。用作模型上下文的视频。默认值：无。 | VIDEO | 否 | - |
| `files` | 可选。用作模型上下文的文件。接受来自 Gemini Generate Content Input Files 节点的输入。默认值：无。 | GEMINI_INPUT_FILES | 否 | - |
| `system_prompt` | 基础指令，用于规定 AI 的行为。默认值：空字符串。这是一个高级参数。 | STRING | 否 | - |

注意：此节点已标记为弃用。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `STRING` | Gemini 模型生成的文本响应。如果模型未返回文本，则节点输出 “Empty response from Gemini model...”。 | STRING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/zh.md)

---
**Source fingerprint (SHA-256):** `d1c53a5d80182085a36302867c8875df696adec6aaea9a9519a21bd6b9543d8f`
