# SAM3 视频跟踪

使用 SAM3 的基于记忆的追踪器跨视频帧追踪对象。此节点处理一系列视频帧，并通过初始掩码或文本提示来定义要追踪的内容，以在帧间维持对象身份。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `images` | 视频帧（批量图像） | IMAGE | 是 | 批量视频帧 |
| `model` | 用于追踪的 SAM3 模型 | MODEL | 是 | SAM3 模型 |
| `initial_mask` | 用于首帧追踪的掩码（每个对象一个）。如果未提供 `conditioning`，则此项为必填。 | MASK | 否 | 每个对象一个掩码 |
| `conditioning` | 在追踪过程中检测新对象的文本条件。如果未提供 `initial_mask`，则此项为必填。 | CONDITIONING | 否 | 文本条件 |
| `detection_threshold` | 文本提示检测的分数阈值（默认值：0.5）。 | FLOAT | 是 | 0.0 to 1.0 |
| `max_objects` | 最大追踪对象数。初始掩码计入此限制。0 使用内部上限 64（默认值：4）。 | INT | 是 | 0 to 64 |
| `detect_interval` | 每 N 帧运行一次检测（1=每帧）。值越大越节省计算资源（默认值：1）。 | INT | 是 | 1 or higher |

**注意：** 必须提供 `initial_mask` 或 `conditioning`。如果两者均省略，节点将引发错误。如果两者都提供，初始掩码定义从首帧开始追踪的对象，文本提示在追踪过程中检测其他对象。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `track_data` | 包含所有视频帧中对象掩码和元数据的追踪数据，包括原始帧尺寸。 | SAM3_TRACK_DATA |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/zh.md)

---
**Source fingerprint (SHA-256):** `ef584628b334997a001a857a7deffb7eda34db8fa50e3d734a07b5e92566d48d`
