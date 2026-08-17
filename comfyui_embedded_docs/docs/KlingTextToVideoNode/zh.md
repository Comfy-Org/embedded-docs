# Kling 文本转视频

Kling 文本转视频节点使用 Kling 视频生成服务将文本提示转换为短视频片段。您提供正面和负面提示，以及宽高比、配置比例和生成模式等设置，节点将返回生成的视频及其标识符和时长。

## 输入
| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述所需视频内容的正面文本提示。多行输入。不能为空。 | STRING | Yes | Maximum 2500 characters |
| `negative_prompt` | 描述视频中需要避免的内容的负面文本提示。多行输入。可以为空。 | STRING | Yes | Maximum 2500 characters |
| `cfg_scale` | 控制视频遵循提示词程度的配置比例值（默认值：1.0）。 | FLOAT | No | 0.0 to 1.0 |
| `aspect_ratio` | 视频宽高比设置（默认值："16:9"）。 | COMBO | No | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `mode` | 用于视频生成的配置，格式如下：模式 / 时长 / 模型名称（默认值："pro mode / 5s duration / kling-v2-5-turbo"）。5 秒模式费用为 0.35 美元，10 秒模式费用为 0.70 美元。 | COMBO | No | `"pro mode / 5s duration / kling-v2-5-turbo"`<br>`"pro mode / 10s duration / kling-v2-5-turbo"` |

## 输出
| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `output` | 生成的视频输出。 | VIDEO |
| `video_id` | 生成的视频的唯一标识符。 | STRING |
| `duration` | 生成的视频的时长信息。 | STRING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/zh.md)

---
**Source fingerprint (SHA-256):** `6a63b0b8bc45dc5a6300cdfe7a373399eeead36de6727f7aae2c026ba0deaea8`
