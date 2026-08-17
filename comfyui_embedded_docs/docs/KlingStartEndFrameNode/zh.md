# Kling 起止帧生成视频

此节点会生成一段在您提供的起始图像和结束图像之间过渡的视频序列。它会生成中间的所有帧，以产生从第一帧到最后一帧的平滑过渡。此节点调用图像转视频 API，但仅支持可与 `image_tail` 请求字段配合使用的输入选项。

## 输入
| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|------|-----------|------|------|
| `start_frame` | 参考图像 - URL 或 Base64 编码字符串，不能超过 10MB，分辨率不得低于 300*300px，宽高比在 1:2.5 ~ 2.5:1 之间。Base64 不应包含 data:image 前缀。 | IMAGE | 是 | - |
| `end_frame` | 参考图像 - 结束帧控制。URL 或 Base64 编码字符串，不能超过 10MB，分辨率不得低于 300*300px。Base64 不应包含 data:image 前缀。 | IMAGE | 是 | - |
| `prompt` | 正向文本提示词 | STRING | 是 | - |
| `negative_prompt` | 负向文本提示词 | STRING | 是 | - |
| `cfg_scale` | 控制提示词引导的强度（默认值：0.5） | FLOAT | 否 | 0.0-1.0 |
| `aspect_ratio` | 生成视频的宽高比（默认值："16:9"） | COMBO | 否 | "16:9"<br>"9:16"<br>"1:1" |
| `mode` | 用于视频生成的配置，格式为：mode / duration / model_name。（默认值："pro mode / 5s duration / kling-v2-5-turbo"）。所有可用选项均使用 pro mode 和 kling-v2-5-turbo 模型，差别仅在于视频时长。 | COMBO | 否 | "pro mode / 5s duration / kling-v2-5-turbo"<br>"pro mode / 10s duration / kling-v2-5-turbo" |

**图像限制：**

- 必须同时提供 `start_frame` 和 `end_frame`，且文件大小不能超过 10MB
- 两张图像的最低分辨率：300×300 像素
- `start_frame` 的宽高比必须介于 1:2.5 与 2.5:1 之间
- Base64 编码的图像不应包含 "data:image" 前缀

**提示词限制：**

- 正向提示词不能为空
- 正向和负向提示词均不得超过 500 个字符
- 如果 `negative_prompt` 留空，则请求中不会包含该字段

**价格：**

- "pro mode / 5s duration / kling-v2-5-turbo"：每次生成 $0.35 USD
- "pro mode / 10s duration / kling-v2-5-turbo"：每次生成 $0.70 USD

## 输出
| 输出名称 | 描述 | 数据类型 |
|-------------|------|-----------|
| `output` | 生成的视频序列 | VIDEO |
| `video_id` | 生成视频的唯一标识符 | STRING |
| `duration` | 生成视频的时长 | STRING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/zh.md)

---
**Source fingerprint (SHA-256):** `a27977226360a425614255f8330ce7fd8ba94b8c3020eb8fdddc01eb74f035c1`
