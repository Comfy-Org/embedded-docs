# 视频切片

Video Slice 节点允许您从视频中提取特定片段。您可以定义开始时间和持续时间来修剪视频，或者简单地跳过开头帧。如果请求的持续时间长于剩余视频，节点可以返回可用的部分或引发错误。

## 输入
| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `video` | 要切片的输入视频。 | VIDEO | 是 | - |
| `start_time` | 开始时间（秒），默认值为 0.0。 | FLOAT | 否 | -1e5 to 1e5 |
| `duration` | 持续时间（秒），0 表示无限制（默认值：0.0）。 | FLOAT | 否 | 0.0 and above |
| `strict_duration` | 如果为 True，当无法实现指定持续时间时，将引发错误（默认值：False）。 | BOOLEAN | 否 | - |

注意：当 `duration` 为 0 时，节点从 `start_time` 切片到视频末尾。如果无法创建请求的片段——例如，因为 `start_time` 超出了视频末尾——节点将引发错误。

## 输出
| Output Name | Description | Data Type |
| --- | --- | --- |
| `video` | 修剪后的视频片段。 | VIDEO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Video Slice/zh.md)

---
**Source fingerprint (SHA-256):** `439b76528742c1fbe230eee9502e945847ae99a58a9bd81a7a7dc3b20e15d450`
