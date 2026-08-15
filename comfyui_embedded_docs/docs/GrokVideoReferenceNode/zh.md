# Grok 参考生成视频

Grok Reference-to-Video 节点根据文本提示生成视频，使用最多七张参考图像来引导输出的风格和内容。使用 `grok-imagine-video-1.5` 模型时，您还可以附加最多三个预设语音参考，并直接在提示中使用 `@ImageN` 和 `@AudioN` 标签引用图像和语音。该节点将请求发送至外部 API，等待生成完成，然后下载生成的视频。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用于视频生成的模型。 | DYNAMIC_COMBO | 是 | `"grok-imagine-video-1.5"`<br>`"grok-imagine-video"` |
| `prompt` | 所需视频的文本描述。必须是非空字符串。 | STRING | 是 | N/A |
| `seed` | 用于确定节点是否应重新运行的种子；无论种子如何，实际结果都是不确定的（默认值：0）。 | INT | 否 | 0 to 2147483647 |

### Grok Imagine Video 1.5 输入

当 `model` 设置为 `grok-imagine-video-1.5` 时可用。

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `voice_1` | 可选的预设语音参考；在提示中将其引用为 @Audio1。API 仅支持这些预设语音，不支持自定义音频（默认值：none）。 | COMBO | 否 | 预设语音选项，包括 `"none"` |
| `voice_2` | 可选的第二个语音参考；在提示中为 @Audio2（默认值：none）。 | COMBO | 否 | 预设语音选项，包括 `"none"` |
| `voice_3` | 可选的第三个语音参考；在提示中为 @Audio3（默认值：none）。 | COMBO | 否 | 预设语音选项，包括 `"none"` |
| `resolution` | 输出视频的分辨率。 | COMBO | 是 | `"480p"`<br>`"720p"` |
| `aspect_ratio` | 输出视频的宽高比。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | 输出视频的时长（秒）（默认值：6）。 | INT | 是 | 1 to 15 |

### Grok Imagine Video 输入

当 `model` 设置为 `grok-imagine-video` 时可用。

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `resolution` | 输出视频的分辨率。 | COMBO | 是 | `"480p"`<br>`"720p"` |
| `aspect_ratio` | 输出视频的宽高比。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | 输出视频的时长（秒）（默认值：6）。 | INT | 是 | 2 to 10 |

### 参考输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | 可增长槽位：连接 1 到 7 张参考图像以引导视频生成。使用 `grok-imagine-video-1.5` 时，在提示中按输入顺序将它们引用为 @Image1 ... @Image7；批量输入每张图像计数一次。 | IMAGE | 是 | 1 to 7 images |

**注意：** 显示的子参数取决于所选的 `model`；`grok-imagine-video-1.5` 会增加 `voice_1`、`voice_2` 和 `voice_3` 输入。至少需要一张参考图像，总数上限为 7（批量输入每张图像计数一次）。使用 `grok-imagine-video-1.5` 时，提示可以将已连接的图像引用为 `@Image1` ... `@Image7`，将语音槽位引用为 `@Audio1`、`@Audio2`、`@Audio3`；未编号的 `@image` 或 `@audio` 指第一个。`@AudioN` 指的是 `voice_N` 控件，而不是已启用语音的顺序。引用未连接的图像或设置为 `none` 的语音槽位会导致错误。API 仅支持预设语音，不支持自定义音频。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `video` | 生成的视频文件。 | VIDEO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoReferenceNode/zh.md)

---
**Source fingerprint (SHA-256):** `ac068b34ad7efe786d29f51052a623eaf324041a99b124f6b5f81fadea661a83`
