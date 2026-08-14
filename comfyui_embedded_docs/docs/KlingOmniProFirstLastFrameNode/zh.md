# Kling Omni 首尾帧到视频 (Pro)

此节点使用最新的 Kling AI 模型，根据起始帧、可选结束帧或参考图片生成视频。它可以创建单个视频，也可以创建多镜头故事板，并为每个片段设置独立提示词和时长。该节点处理这些输入以生成指定长度和分辨率的视频，并可选择生成音频。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model_name` | 用于视频生成的特定 Kling AI 模型。 | COMBO | 是 | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | 描述视频内容的文本提示词。可以包含正面和负面描述。启用故事板时忽略此项。 | STRING | 是 | - |
| `duration` | 生成视频的期望时长（秒），默认值：5。 | INT | 是 | 3 到 15 |
| `first_frame` | 视频序列的起始图像。 | IMAGE | 是 | - |
| `end_frame` | 视频的可选结束帧。不能与 `reference_images` 同时使用。不适用于故事板。 | IMAGE | 否 | - |
| `reference_images` | 最多 6 张额外的参考图像。 | IMAGE | 否 | - |
| `resolution` | 生成视频的输出分辨率（默认值："1080p"）。 | COMBO | 否 | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `storyboards` | 生成一系列具有独立提示词和时长的视频片段。仅 `kling-v3-omni` 支持。启用后，每个故事板都需要提供提示词和时长输入。 | DYNAMIC_COMBO | 否 | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `generate_audio` | 为视频生成音频（默认值：False）。仅 `kling-v3-omni` 支持。 | BOOLEAN | 否 | True / False |
| `seed` | Seed 控制节点是否应重新运行；无论 seed 取值如何，结果都是非确定性的（默认值：0）。 | INT | 否 | 0 到 2147483647 |

### 故事板输入

当 `storyboards` 设置为 `"disabled"` 以外的值时，会为每个选定的片段添加以下输入（N 的范围为 1 到所选故事板的数量）：

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `storyboard_N_prompt` | 故事板片段 N 的提示词。最多 512 个字符。（默认值：""） | STRING | 是 | - |
| `storyboard_N_duration` | 故事板片段 N 的时长（秒）（默认值：4）。 | INT | 是 | 1 到 15 |

**重要限制：**

* `end_frame` 输入不能与 `reference_images` 输入同时使用。
* `end_frame` 输入不能与故事板同时使用。
* `kling-video-o1` 模型不支持超过 10 秒的时长、音频生成、4k 分辨率或故事板。
* 如果未将 `end_frame` 或任何 `reference_images` 与 `kling-video-o1` 模型一起提供，则 `duration` 只能设置为 5 或 10 秒。
* 所有输入图像（`first_frame`、`end_frame` 以及任何 `reference_images`）的宽度和高度都必须至少为 300 像素。
* 所有输入图像的宽高比必须在 1:2.5 到 2.5:1 之间。
* 最多可通过 `reference_images` 输入提供 6 张图像。
* `prompt` 文本长度必须在 1 到 2500 个字符之间（启用故事板时允许 0 个字符）。
* 提示词可以使用占位符 `@image`、`@image1`、`@image2` 等来引用输入图像；这些占位符会自动转换为 API 兼容的图像引用格式。
* 启用故事板时，所有故事板片段的总时长必须等于全局 `duration` 值。
* 每个故事板提示词的长度必须在 1 到 512 个字符之间。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `output` | 生成的视频文件。 | VIDEO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProFirstLastFrameNode/zh.md)

---
**Source fingerprint (SHA-256):** `2b26914ba29c3d877a981e41acb44d15dfacc604d86d7cc232ebfa7fda0ae3b8`
