# Google Gemini Omni（视频）

使用 Google 的 Gemini Omni Flash 模型，通过文本提示生成带音频的视频。可选提供参考图像和/或视频以引导或编辑结果。在提示中直接描述期望时长（3-10 秒）和宽高比（16:9 或 9:16）。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用于生成视频的 Gemini 视频模型。 | MODEL | Yes | "Omni Flash" |
| `seed` | Seed 控制节点是否重新运行；无论 seed 如何，结果都是非确定性的。 | INT | Yes | 0 to 2147483647 |
| `prompt` | The text prompt describing the video to generate. Must be at least one non-whitespace character after stripping leading/trailing whitespace. | STRING | Yes | Minimum 1 character after stripping whitespace |
| `images` | Optional reference images to guide the video generation. Maximum of 14 images total. | IMAGE | No | Multiple images allowed (max 14) |
| `videos` | Optional reference videos to guide or edit the video generation. Maximum of 3 videos, each up to 10 seconds. | VIDEO | No | Multiple videos allowed (max 3, each max 10s) |
| `temperature` | Controls randomness in generation (default: 1.0). | FLOAT | No | 0.0 to 2.0 |
| `top_p` | Nucleus sampling parameter (default: 0.95). | FLOAT | No | 0.0 to 1.0 |

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `VIDEO` | The generated video with audio from the Gemini model. | VIDEO |
| `STRING` | Any text response from the model, such as reasoning or explanations. | STRING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/zh.md)

---
**Source fingerprint (SHA-256):** `046842b7ec736283bba355aaa038b02fcf2416020f5f7aee7b0150d2a05bcbe6`
