> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/zh.md)

## 概述

使用 SAM3 的基于记忆的跟踪器在视频帧间跟踪对象。此节点处理一系列视频帧，并跨帧维护对象身份，通过初始遮罩或文本提示来定义要跟踪的内容。

## 输入

| 参数 | 数据类型 | 是否必需 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | 是 | 批量视频帧 | 作为批量图像的视频帧 |
| `model` | MODEL | 是 | SAM3 模型 | 用于跟踪的 SAM3 模型 |
| `initial_mask` | MASK | 否 | 每个对象一个遮罩 | 第一帧中要跟踪的对象遮罩（每个对象一个）。如果未提供 `conditioning`，则此项为必需。 |
| `conditioning` | CONDITIONING | 否 | 文本条件 | 用于在跟踪过程中检测新对象的文本条件。如果未提供 `initial_mask`，则此项为必需。 |
| `detection_threshold` | FLOAT | 否 | 0.0 到 1.0（默认值：0.5） | 文本提示检测的分数阈值 |
| `max_objects` | INT | 否 | 0 到 64（默认值：0） | 最大跟踪对象数。初始遮罩计入此限制。0 表示使用内部上限 64。 |
| `detect_interval` | INT | 否 | 1 到无限制（默认值：1） | 每 N 帧运行一次检测（1=每帧）。值越大越节省计算资源。 |

**注意：** 必须提供 `initial_mask` 或 `conditioning` 中的至少一个。如果两者都省略，节点将报错。

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `track_data` | SAM3TrackData | 包含所有视频帧中对象遮罩和元数据的跟踪数据 |

---
**Source fingerprint (SHA-256):** `30768bdf5839c1d7b984675e68a127a27f21b17724a2dc885e27f00c272db3cb`
