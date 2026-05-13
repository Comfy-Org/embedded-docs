> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/zh.md)

### 概述

Kling 图生视频节点使用文本提示从起始参考图像生成视频。它接收一张图像作为第一帧，并根据正面和负面文本描述创建视频序列，支持模型、时长、宽高比和生成模式等可配置选项。

## 输入

| 参数 | 数据类型 | 是否必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `start_frame` | IMAGE | 是 | - | 用于生成视频的参考图像。 |
| `prompt` | STRING | 是 | - | 正面文本提示。 |
| `negative_prompt` | STRING | 是 | - | 负面文本提示。 |
| `model_name` | COMBO | 是 | `"kling-v2-master"`<br>`"kling-v2-1-master"`<br>`"kling-v2-5-turbo"`<br>`"kling-v2-1"`<br>`"kling-v1-6"`<br>`"kling-v1-5"`<br>`"kling-v1-4"`<br>`"kling-v1-0"` | 用于视频生成的模型（默认值：`"kling-v2-master"`）。 |
| `cfg_scale` | FLOAT | 是 | 0.0 至 1.0 | 控制视频对提示的遵循程度。数值越高表示遵循程度越强（默认值：0.8）。 |
| `mode` | COMBO | 是 | `"std"`<br>`"pro"` | 生成模式。`"std"` 为标准质量，`"pro"` 为更高质量（默认值：`"std"`）。 |
| `aspect_ratio` | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"` | 生成视频的宽高比（默认值：`"16:9"`）。 |
| `duration` | COMBO | 是 | `"5"`<br>`"10"` | 生成视频的时长（秒）（默认值：`"5"`）。 |

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的视频输出。 |
| `video_id` | STRING | 生成视频的唯一标识符。 |
| `duration` | STRING | 生成视频的时长信息。 |

---
**Source fingerprint (SHA-256):** `2f82997307265dba6714733523e265d1e0a25fd7491b043f05d7d000b7b9b2f3`
