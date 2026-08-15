# ElevenLabs 文字转语音

ElevenLabs Text to Speech 节点使用 ElevenLabs API 将书面文本转换为语音音频。您可以选择音色，并调整稳定性、速度和风格等语音特征，以创建自定义音频输出。

## 输入
### 通用输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用于文本转语音的模型。选择模型后会显示其特定参数。 | DYNAMIC_COMBO | 是 | "eleven_multilingual_v2"<br>"eleven_v3" |
| `voice` | 用于语音合成的音色。从 Voice Selector 或 Instant Voice Clone 连接。 | ELEVENLABS_VOICE | 是 | N/A |
| `text` | 要转换为语音的文本。必须至少包含一个字符。 | STRING | 是 | N/A |
| `stability` | 语音稳定性。数值越低，情感范围越广；数值越高，语音更一致，但也可能更单调（默认值：0.5）。 | FLOAT | 是 | 0.0 - 1.0 |
| `apply_text_normalization` | 文本规范化模式。'auto' 由系统自动决定，'on' 始终应用规范化，'off' 跳过规范化。 | COMBO | 是 | "auto"<br>"on"<br>"off" |
| `language_code` | ISO-639-1 或 ISO-639-3 语言代码（例如 'en'、'es'、'fra'）。留空则自动检测（默认值：""）。 | STRING | 是 | N/A |
| `seed` | 用于可复现性的随机种子（不保证确定性）（默认值：1）。 | INT | 是 | 0 - 2147483647 |
| `output_format` | 音频输出格式。 | COMBO | 是 | "mp3_44100_192"<br>"opus_48000_192" |

### eleven_multilingual_v2 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `speed` | 语速。1.0 为正常速度，<1.0 较慢，>1.0 较快（默认值：1.0）。 | FLOAT | 是 | 0.7 - 1.3 |
| `similarity_boost` | 相似度增强。数值越高，音色与原始声音越相似（默认值：0.75）。 | FLOAT | 是 | 0.0 - 1.0 |
| `use_speaker_boost` | 增强与原始说话人声音的相似度（默认值：False）。 | BOOLEAN | 是 | True<br>False |
| `style` | 风格夸张程度。数值越高，风格化表现越强，但可能降低稳定性（默认值：0.0）。 | FLOAT | 是 | 0.0 - 0.2 |

### eleven_v3 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `speed` | 语速。1.0 为正常速度，<1.0 较慢，>1.0 较快（默认值：1.0）。 | FLOAT | 是 | 0.7 - 1.3 |
| `similarity_boost` | 相似度增强。数值越高，音色与原始声音越相似（默认值：0.75）。 | FLOAT | 是 | 0.0 - 1.0 |

**注意：** `text` 输入必须至少包含一个字符。如果 `language_code` 留空，将自动检测语言。`use_speaker_boost` 和 `style` 参数仅适用于 `eleven_multilingual_v2` 模型。

## 输出
| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `audio` | 文本转语音转换生成的音频。 | AUDIO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSpeech/zh.md)

---
**Source fingerprint (SHA-256):** `78ed1c6af2d0b1cc0293d725492a8b104b6d0c6bc18d9971b75047db946cdd33`
