# ByteDance Seedance 2.0 首帧-末帧生成视频

此节点使用字节跳动的 Seedance 2.5 或 Seedance 2.0 模型，根据必需的首帧图像和可选的末帧图像生成视频。首帧定义视频片段的开头，末帧（如果提供）定义结尾，文本提示描述运动。所选模型控制可用的分辨率、时长和输出格式选项。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用于视频生成的模型。Seedance 2.5 是最新模型，支持最长 30 秒的视频和 mp4/mov 输出；Seedance 2.0 提供最高质量和 1080p/4k；Fast 针对速度优化；Mini 是生成速度最快且成本最低的模型。选择模型将在下方显示其特定输入。 | DYNAMIC_COMBO | 是 | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `first_frame` | 视频的首帧图像。`first_frame` 和 `first_frame_asset_id` 必须提供其中之一。 | IMAGE | 否 | - |
| `last_frame` | 视频的末帧图像。 | IMAGE | 否 | - |
| `first_frame_asset_id` | 用作首帧的 Seedance asset_id。与 `first_frame` 图像输入互斥。默认为空字符串。 | STRING | 否 | - |
| `last_frame_asset_id` | 用作末帧的 Seedance asset_id。与 `last_frame` 图像输入互斥。默认为空字符串。 | STRING | 否 | - |
| `seed` | seed 控制节点是否应重新运行；无论 seed 为何值，结果都是非确定性的。默认为 0。 | INT | 否 | 0 to 2147483647 |
| `watermark` | 是否向视频添加水印。默认为 False。 | BOOLEAN | 否 | - |

### Seedance 2.5 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用于视频生成的文本提示。将台词放在双引号中，以引导生成的对话。默认为空字符串。 | STRING | 是 | - |
| `resolution` | 输出视频的分辨率。默认为“720p”。 | COMBO | 是 | `"480p"`<br>`"720p"` |
| `duration` | 输出视频的时长（秒）（4-30）。默认为 5。 | INT | 是 | 4 to 30 |
| `generate_audio` | 为输出视频启用音频生成。默认为 True。 | BOOLEAN | 是 | - |
| `output_format` | 输出视频的容器格式。默认为“mp4”。 | COMBO | 是 | `"mp4"` |

### Seedance 2.0 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用于视频生成的文本提示。默认为空字符串。 | STRING | 是 | - |
| `resolution` | 输出视频的分辨率。 | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | 输出视频的宽高比。默认为“adaptive”。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 输出视频的时长（秒）（4-15）。默认为 7。 | INT | 是 | 4 to 15 |
| `generate_audio` | 为输出视频启用音频生成。默认为 True。 | BOOLEAN | 是 | - |

### 由 Seedance 2.0 Fast 和 Seedance 2.0 Mini 共用

这两个模型具有与 Seedance 2.0 相同的输入，只是仅提供 480p 和 720p 分辨率。

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用于视频生成的文本提示。默认为空字符串。 | STRING | 是 | - |
| `resolution` | 输出视频的分辨率。 | COMBO | 是 | `"480p"`<br>`"720p"` |
| `ratio` | 输出视频的宽高比。默认为“adaptive”。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 输出视频的时长（秒）（4-15）。默认为 7。 | INT | 是 | 4 to 15 |
| `generate_audio` | 为输出视频启用音频生成。默认为 True。 | BOOLEAN | 是 | - |

**约束和限制：**

*   `prompt` 为必填项，且必须包含至少一个非空白字符（忽略开头和结尾的空白）。
*   您必须恰好提供一个首帧来源：`first_frame` 图像或 `first_frame_asset_id`。同时提供两者会引发错误，两者都不提供也会引发错误。
*   `last_frame` 图像和 `last_frame_asset_id` 互斥。两者都可以省略。
*   资产 ID 必须引用状态为 Active 的现有 Seedance 资产。如果资产不是 Active 状态或不是图像资产，则会引发错误。
*   本地图像的宽高比必须介于 0.4 和 2.5 之间（2:5 到 5:2）。
*   对于 Seedance 2.0 模型，本地图像必须至少为 300x300 像素。它们会被自动调整到所选分辨率和宽高比所支持的精确输出尺寸，并且请求以“adaptive”宽高比提交。当 `ratio` 为“adaptive”时，输出宽高比由首帧自身的宽高比决定，并就近取一个受支持的宽高比。当使用资产 ID 而非本地图像时，直接应用所选的 `ratio` 值。
*   对于 Seedance 2.5，以及任何使用资产 ID 的模型，图像会自动缩小到最长边不超过 6000 像素，且每个维度必须在 300 到 6000 像素之间。
*   Seedance 2.5 始终保留首帧自身的宽高比，因此该模型不显示 `ratio` 输入。
*   不同模型的时长限制不同：Seedance 2.5 支持 4 到 30 秒，而 Seedance 2.0、2.0 Fast 和 2.0 Mini 支持 4 到 15 秒。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `output` | 生成的视频。 | VIDEO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/zh.md)

---
**Source fingerprint (SHA-256):** `d87265eb75d67f7d80f76474fc699f7ca87b6edbddda36733d5e440708b074a2`
