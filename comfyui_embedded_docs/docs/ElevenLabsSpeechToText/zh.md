# ElevenLabs 语音转文本

ElevenLabs 语音转文本节点使用 ElevenLabs 的语音转文本 API 将音频转录为文本。它支持自动语言检测、识别说话人，以及在转录文本中标注非语音声音，如（笑声）或（音乐）。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `模型` | 用于转录的模型。选择模型会显示其特定参数。 | DYNAMIC_COMBO | 是 | `"scribe_v2"` |
| `音频` | 要转录的音频。 | AUDIO | 是 | - |
| `语言代码` | ISO-639-1 或 ISO-639-3 语言代码（例如 'en'、'es'、'fra'）。留空以进行自动检测。（默认值：""） | STRING | 否 | - |
| `说话人数` | 要预测的最大说话人数量。设置为 0 以进行自动检测。（默认值：0） | INT | 否 | 0 - 32 |
| `种子` | 用于可重现性的随机种子（不保证确定性）。（默认值：1） | INT | 否 | 0 - 2147483647 |

### Scribe v2 输入

当选择了 `"scribe_v2"` 模型时，会出现这些参数。

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `tag_audio_events` | 在转录文本中标注类似（笑声）、（音乐）等声音。（默认值：False） | BOOLEAN | 否 | - |
| `diarize` | 标注正在说话的说话人。（默认值：False） | BOOLEAN | 否 | - |
| `diarization_threshold` | 说话人分离灵敏度。数值越低，对说话人变化越敏感。仅在启用 `diarize` 时使用。（默认值：0.22） | FLOAT | 否 | 0.1 - 0.4 |
| `temperature` | 随机性控制。0.0 使用模型默认值。数值越高，随机性越大。（默认值：0.0） | FLOAT | 否 | 0.0 - 2.0 |
| `timestamps_granularity` | 转录单词的时间戳精度。（默认值："word"） | COMBO | 否 | `"word"`<br>`"character"`<br>`"none"` |

**注意：** 当启用 `diarize` 时，`num_speakers` 不能设置为大于 0 的值。要么禁用 `diarize`，要么将 `num_speakers` 设置为 0；否则会引发错误。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `文本` | 音频转录出的文本。 | STRING |
| `语言代码` | 检测到的音频语言代码。 | STRING |
| `单词 JSON` | 包含详细单词级信息的 JSON 格式字符串，如果启用，还包括时间戳和说话人标签。 | STRING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToText/zh.md)

---
**Source fingerprint (SHA-256):** `7eb5d72615aa8a9e4a8014e45b39cf83dc8d8432d7ce0dccba20489be80a5830`
