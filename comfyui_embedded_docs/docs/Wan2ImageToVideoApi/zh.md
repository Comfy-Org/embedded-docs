# Wan 2.7 图像转视频

Wan 2.7 图像转视频节点可根据首帧图像生成视频。您还可以选择提供末帧图像以创建两帧之间的过渡，或提供音频文件来引导视频的运动和节奏。该节点使用 AI 模型根据您的文本描述为场景添加动画效果。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 用于视频生成的 AI 模型。 | COMBO | 是 | `"wan2.7-i2v"` |
| `first_frame` | 首帧图像。输出的宽高比由此图像决定。 | IMAGE | 是 | - |
| `last_frame` | 末帧图像。模型会生成从首帧过渡到末帧的视频。 | IMAGE | 否 | - |
| `audio` | 用于驱动视频生成的音频（例如，唇形同步、节拍匹配动作）。时长：2秒-30秒。如果未提供，模型会自动生成匹配的背景音乐或音效。 | AUDIO | 否 | - |
| `seed` | 用于生成的随机种子（默认值：0）。 | INT | 是 | 0 到 2147483647 |
| `prompt_extend` | 是否使用 AI 辅助增强提示词（默认值：True）。这是一个高级设置。 | BOOLEAN | 是 | True<br>False |
| `watermark` | 是否在结果中添加 AI 生成的水印（默认值：False）。这是一个高级设置。 | BOOLEAN | 是 | True<br>False |

### wan2.7-i2v 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `model.prompt` | 描述画面元素和视觉特征的提示词。支持英文和中文。 | STRING | 是 | - |
| `model.negative_prompt` | 描述需要避免的内容的负面提示词。 | STRING | 是 | - |
| `model.resolution` | 输出视频的分辨率。 | COMBO | 是 | `"720P"`<br>`"1080P"` |
| `model.duration` | 生成视频的时长（秒）（默认值：5）。 | INT | 是 | 2 到 15 |

**注意：** `audio` 输入有时长限制。如果提供，音频文件必须为 2 到 30 秒。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `output` | 生成的视频文件。 | VIDEO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ImageToVideoApi/zh.md)

---
**Source fingerprint (SHA-256):** `81b0dc9500ff00e1428422d3d9c8df8f790c1d9dec547dcba0d1aa239f8a8beb`
