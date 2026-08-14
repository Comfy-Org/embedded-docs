# Kling Omni 文本到视频 (Pro)

此节点使用最新的 Kling AI 模型，根据文本描述生成视频。它将你的提示词发送到远程 API，并返回生成的视频。通过该节点，你可以控制视频的长度、画面比例、质量，甚至创建多镜头故事板。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model_name` | 用于视频生成的特定 Kling 模型（默认：`"kling-v3-omni"`）。 | COMBO | 是 | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | 描述视频内容的文本提示词。可同时包含正面和负面描述。启用故事板时忽略。 | STRING | 是 | 0 到 2500 个字符 |
| `aspect_ratio` | 生成视频的画面比例或尺寸。 | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | 视频时长（秒）（默认：5）。 | INT | 是 | 3 到 15 秒 |
| `resolution` | 视频的质量或像素分辨率（默认：`"1080p"`）。 | COMBO | 否 | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `storyboards` | 生成一系列具有各自提示词和时长的视频片段。对 o1 模型忽略。 | DYNAMIC_COMBO | 否 | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `generate_audio` | 是否为视频生成音频（默认：False）。 | BOOLEAN | 否 | True / False |
| `seed` | 种子控制节点是否应重新运行；无论种子如何，结果都是非确定性的（默认：0）。 | INT | 否 | 0 到 2147483647 |

### 故事板子输入

当 `storyboards` 设置为 `"disabled"` 以外的值时，每个故事板片段都会出现以下输入。在下面的参数名中，`{i}` 是片段编号，从 1 到所选择的故事板数量。

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `storyboard_{i}_prompt` | 故事板片段 {i} 的提示词。最多 512 个字符。 | STRING | 是 | 1 到 512 个字符 |
| `storyboard_{i}_duration` | 故事板片段 {i} 的时长（秒）（默认：4）。 | INT | 是 | 1 到 15 秒 |

### 参数约束与限制

- **模型特定限制：**
  - `kling-video-o1` 模型仅支持 **5 或 10 秒**的时长。
  - `kling-video-o1` 模型**不**支持音频生成。
  - `kling-video-o1` 模型**不**支持 4k 分辨率。
  - `kling-video-o1` 模型**不**支持故事板。
- **故事板约束：**
  - 启用故事板时，`prompt` 字段将被忽略。
  - 每个故事板都需要自己的提示词（1 到 512 个字符）和时长。
  - 所有故事板的总时长必须与全局 `duration` 参数完全相等。
- **提示词要求：**
  - 当故事板**禁用**时，`prompt` 字段为必填（最少 1 个字符）。
  - 当故事板**启用**时，`prompt` 字段可以为空（0 个字符）。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `output` | 根据所提供的文本提示词和设置生成的视频。 | VIDEO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProTextToVideoNode/zh.md)

---
**Source fingerprint (SHA-256):** `d2fbbe7c6aae283eb3fa7f73d788b809098a9a4dd6e8ada54697d43fd5bf10f2`
