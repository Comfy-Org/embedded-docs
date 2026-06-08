GeminiImage 节点利用 Google 的 Gemini AI 模型生成文本和图像响应。它允许您提供多模态输入，包括文本提示、图像和文件，以创建连贯的文本和图像输出。该节点处理与最新 Gemini 模型的所有 API 通信和响应解析。

## 输入

| 参数 | 描述 | 数据类型 | 输入类型 | 默认值 | 取值范围 |
| --- | --- | --- | --- | --- | --- |
| `prompt` | 用于生成的文本提示 | STRING | required | "" | - |
| `model` | 用于生成响应的 Gemini 模型。 | COMBO | required | gemini_2_5_flash_image_preview | `gemini_2_5_flash_image_preview`<br>`gemini_2_5_pro_exp_03_25`<br>`gemini_2_0_flash_exp_image_generation` |
| `seed` | 当种子固定为特定值时，模型会尽力为重复请求提供相同的响应。不保证输出具有确定性。此外，更改模型或参数设置（例如温度）可能会导致响应发生变化，即使使用相同的种子值也是如此。默认情况下，使用随机种子值。 | INT | required | 42 | 0 到 18446744073709551615 |
| `images` | 可选图像，用作模型的上下文。要包含多个图像，可以使用“批处理图像”节点。 | IMAGE | optional | None | - |
| `files` | 可选文件，用作模型的上下文。接受来自“Gemini 生成内容输入文件”节点的输入。 | GEMINI_INPUT_FILES | optional | None | - |

**注意：** 该节点包含隐藏参数（`auth_token`、`comfy_api_key`、`unique_id`），这些参数由系统自动处理，无需用户输入。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `IMAGE` | 来自 Gemini 模型的生成图像响应 | IMAGE |
| `STRING` | 来自 Gemini 模型的生成文本响应 | STRING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage/zh.md)

---
**Source fingerprint (SHA-256):** `bf55ec4f5a869a6bc5a15366f55f86ad25f9498c14056acc80951d3637bf08f2`
