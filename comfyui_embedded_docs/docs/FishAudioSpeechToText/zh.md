# FishAudioSpeechToText

此节点使用 Fish Audio 语音转文字服务将音频转录为文本。它会自动检测音频的语言，并可选择返回包含单词级时间戳的片段（JSON 格式）。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `audio` | 要转录的音频。 | AUDIO | 是 | — |
| `language` | ISO 639-1 语言提示（如 'en'、'zh'）。无论如何都会自动检测语言。默认：""（空字符串）。 | STRING | 否 | 任何 ISO 639-1 语言代码，如 `en`、`zh`；留空表示自动检测 |
| `precise_timestamps` | 返回包含单词级时间戳的片段。默认：false。 | BOOLEAN | 否 | true or false |

注意：`language` 参数仅作为提示——语言始终会从音频中自动检测。当 `precise_timestamps` 为 false（默认值）时，不会返回单词级时间戳；当为 true 时，输出片段将包含单词级时间戳。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `text` | 转录后的文本。 | STRING |
| `language_code` | 检测到的音频 ISO 639-1 语言代码。 | STRING |
| `segments_json` | 包含转录片段的 JSON 字符串。当启用 `precise_timestamps` 时，包含单词级时间戳。 | STRING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioSpeechToText/zh.md)

---
**Source fingerprint (SHA-256):** `eaf1c9a9d2b90ec962a408615cc417b552864354c3f272144b8e239b23961920`
