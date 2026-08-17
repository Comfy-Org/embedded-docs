# Kling 图像转视频

Kling 图像到视频节点使用文本提示从起始参考图像生成视频。它将图像用作第一帧，并根据正向和负向文本描述创建视频序列，同时提供模型、时长、生成模式和宽高比等可配置选项。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|------|------|----------|------|------|
| `start_frame` | 用于生成视频的参考图像。必须至少为 300x300 像素，且宽高比在 1:2.5 和 2.5:1 之间。 | IMAGE | 是 | - |
| `prompt` | 正向文本提示词。最大长度 500 个字符。 | STRING | 是 | - |
| `negative_prompt` | 负向文本提示词。最大长度 500 个字符，可为空。 | STRING | 是 | - |
| `model_name` | 用于视频生成的模型（默认值：`"kling-v2-5-turbo"`）。 | COMBO | 是 | `"kling-v2-5-turbo"` |
| `cfg_scale` | 控制视频遵循提示词的程度。数值越高，遵循度越强（默认值：0.8）。 | FLOAT | 是 | 0.0 to 1.0 |
| `mode` | 生成模式（默认值：`"pro"`）。 | COMBO | 是 | `"pro"` |
| `aspect_ratio` | 生成视频的宽高比（默认值：`"16:9"`）。 | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | 生成视频的时长（秒）（默认值：`"5"`）。 | COMBO | 是 | `"5"`<br>`"10"` |

注意：正向提示词不能为空。正向和负向提示词均限制为 500 个字符。输入图像必须至少为 300x300 像素，且宽高比在 1:2.5 和 2.5:1 之间。

## 输出

| 输出名称 | 描述 | 数据类型 |
|----------|------|----------|
| `output` | 生成的视频。 | VIDEO |
| `video_id` | 生成视频的唯一标识符。 | STRING |
| `duration` | 生成视频的时长。 | STRING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/zh.md)

---
**Source fingerprint (SHA-256):** `f4a461819bc05f92d867bddcc78a66ad7beaa10707ef8cae3e7eb9e6f72c890a`
