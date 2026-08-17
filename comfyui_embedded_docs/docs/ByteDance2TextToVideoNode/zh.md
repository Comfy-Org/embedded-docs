# ByteDance Seedance 2.0 文本生成视频

此节点使用字节跳动的 Seedance 2.5 或 2.0 模型，根据文本描述生成视频。它会将你的提示词发送到所选模型，等待视频处理完成，并返回最终结果。

## 输入

`model` 参数是一个动态组合框。当你选择模型时，会显示多个必须填写的模型专属输入，包括文本提示词、分辨率、宽高比、时长和音频生成设置。

### 通用输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|------|------|----------|----------|------|
| `model` | 用于视频生成的模型。Seedance 2.5 是最新模型，可生成最长 30 秒的视频，支持 mp4/mov 输出；Seedance 2.0 提供最高质量，支持 1080p/4k；Fast 以速度优化为主；Mini 是速度最快、成本最低的生成选项。 | DYNAMIC_COMBO | 是 | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | 控制节点是否重新运行；无论种子值如何，结果都是非确定性的（默认值：0）。 | INT | 否 | 0 to 2147483647 |
| `watermark` | 是否在视频中添加水印（默认值：False）。这是一个高级设置。 | BOOLEAN | 否 | True / False |

### Seedance 2.5 输入

当 `model` 设置为 `Seedance 2.5` 时，显示这些输入。

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|------|------|----------|----------|------|
| `prompt` | 视频生成的文本提示词。将台词放在双引号中可引导生成的对话（默认值：空）。 | STRING | 是 | Any text |
| `resolution` | 输出视频的分辨率（默认值："720p"）。 | COMBO | 是 | `"480p"`<br>`"720p"` |
| `ratio` | 输出视频的宽高比（默认值："16:9"）。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 输出视频的时长（秒）（默认值：5）。 | INT | 是 | 4 to 30 |
| `generate_audio` | 是否为输出视频生成音频（默认值：True）。 | BOOLEAN | 否 | True / False |
| `output_format` | 输出视频的容器格式（默认值："mp4"）。 | COMBO | 是 | `"mp4"` |

### Seedance 2.0 输入

当 `model` 设置为 `Seedance 2.0` 时，显示这些输入。

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|------|------|----------|----------|------|
| `prompt` | 视频生成的文本提示词（默认值：空）。 | STRING | 是 | Any text |
| `resolution` | 输出视频的分辨率。 | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | 输出视频的宽高比（默认值："16:9"）。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 输出视频的时长（秒）（默认值：7）。 | INT | 是 | 4 to 15 |
| `generate_audio` | 是否为输出视频生成音频（默认值：True）。 | BOOLEAN | 否 | True / False |

### Seedance 2.0 Fast 和 Seedance 2.0 Mini 输入

当 `model` 设置为 `Seedance 2.0 Fast` 或 `Seedance 2.0 Mini` 时，显示这些输入。

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|------|------|----------|----------|------|
| `prompt` | 视频生成的文本提示词（默认值：空）。 | STRING | 是 | Any text |
| `resolution` | 输出视频的分辨率。 | COMBO | 是 | `"480p"`<br>`"720p"` |
| `ratio` | 输出视频的宽高比（默认值："16:9"）。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 输出视频的时长（秒）（默认值：7）。 | INT | 是 | 4 to 15 |
| `generate_audio` | 是否为输出视频生成音频（默认值：True）。 | BOOLEAN | 否 | True / False |

**注意：** `prompt` 在去除空白后必须至少包含 1 个字符，否则任务将无法通过验证。时长限制取决于模型：Seedance 2.5 支持 4 到 30 秒，而 Seedance 2.0、Seedance 2.0 Fast 和 Seedance 2.0 Mini 支持 4 到 15 秒。分辨率选项也因模型而异：Seedance 2.5 支持 480p 和 720p；Seedance 2.0 支持 480p、720p、1080p 和 4k；Seedance 2.0 Fast 和 Seedance 2.0 Mini 仅支持 480p 和 720p。

## 输出

| 输出名称 | 描述 | 数据类型 |
|----------|------|----------|
| `video` | 生成的视频文件。 | VIDEO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/zh.md)

---
**Source fingerprint (SHA-256):** `66d200f4ddf674b897def63604b0f29dcbf655e00b4e9b9c11e31b671ead94bc`
