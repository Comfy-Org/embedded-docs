> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/zh.md)

## ## 概述

使用 SAM3 的基于记忆的追踪器，在视频帧间追踪物体。此节点处理一系列视频帧，并通过初始遮罩或文本提示定义追踪目标，从而在帧间保持物体身份。

## ## 输入

| 参数 | 数据类型 | 是否必需 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | 是 | 批量视频帧 | 作为批量图像输入的视频帧 |
| `model` | MODEL | 是 | SAM3 模型 | 用于追踪的 SAM3 模型 |
| `initial_mask` | MASK | 否 | 每个物体一个遮罩 | 第一帧中要追踪的物体遮罩（每个物体一个）。如果未提供 `conditioning`，则此项为必需。 |
| `conditioning` | CONDITIONING | 否 | 文本条件 | 用于在追踪过程中检测新物体的文本条件。如果未提供 `initial_mask`，则此项为必需。 |
| `detection_threshold` | FLOAT | 否 | 0.0 到 1.0（默认值：0.5） | 文本提示检测的分数阈值 |
| `max_objects` | INT | 否 | 0 到无限制（默认值：0） | 最大追踪物体数（0 表示无限制）。初始遮罩计入此限制。 |
| `detect_interval` | INT | 否 | 1 到无限制（默认值：1） | 每 N 帧运行一次检测（1 表示每帧）。较高的值可节省计算资源。 |

**注意：** 必须提供 `initial_mask` 或 `conditioning` 中的至少一项。如果两者均省略，节点将报错。

## ## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `track_data` | SAM3TrackData | 包含所有视频帧中物体遮罩及元数据的追踪数据 |