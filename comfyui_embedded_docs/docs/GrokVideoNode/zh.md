# Grok 视频

Grok Video 节点用于根据文本描述生成短视频。它可以使用提示词从零开始生成视频，也可以对单个输入图像进行动画处理，并可选地由提示词引导。该节点向外部 API 发送请求并返回生成的视频。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用于视频生成的模型。 | COMBO | 是 | "grok-imagine-video"<br>"grok-imagine-video-1.5" |
| `prompt` | 所需视频的文本描述。当提供输入图像且模型为 grok-imagine-video-1.5 时，此参数为可选。 | STRING | 是 | - |
| `resolution` | 输出视频的分辨率。1080p 仅适用于 grok-imagine-video-1.5 模型。 | COMBO | 是 | "480p"<br>"720p"<br>"1080p" |
| `aspect_ratio` | 输出视频的宽高比（默认值："auto"）。 | COMBO | 是 | "auto"<br>"16:9"<br>"4:3"<br>"3:2"<br>"1:1"<br>"2:3"<br>"3:4"<br>"9:16" |
| `duration` | 输出视频的时长（秒）（默认值：6）。 | INT | 是 | 1 到 15 |
| `seed` | 用于决定节点是否重新运行的种子；无论种子如何，实际结果都是不确定的（默认值：0）。 | INT | 是 | 0 到 2147483647 |
| `image` | 可选的起始图像。如果省略，则仅根据文本提示生成视频。 | IMAGE | 否 | - |

**注意：**
- "1080p" 分辨率仅适用于 `grok-imagine-video-1.5` 模型。若将 `grok-imagine-video` 模型与 1080p 一起选择，则会引发错误。
- 仅支持一个输入图像。提供多个图像会引发错误。
- 除非模型设置为 `grok-imagine-video-1.5` 且提供了输入图像，否则 `prompt` 为必填项。在必填时，提示词去除空白后必须至少包含 1 个字符。
- `seed` 仅决定节点是否重新运行；无论种子值如何，生成的结果都是不确定的。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `output` | 生成的视频。 | VIDEO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoNode/zh.md)

---
**Source fingerprint (SHA-256):** `c708c8cd78749aa533db63e2bc5938ef14fa78cf95f8ba4628d0c586f8723297`
