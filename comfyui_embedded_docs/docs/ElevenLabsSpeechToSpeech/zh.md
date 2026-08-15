# ElevenLabs 语音转换

ElevenLabs 语音到语音节点可将输入音频文件从一种语音转换为另一种语音。它使用 ElevenLabs API 转换语音，同时保留音频的原始内容和情绪基调。

## 输入
### 通用输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 用于语音到语音转换的模型。每个模型选项都提供一组匹配的语音设置（similarity_boost、style、use_speaker_boost、speed）。 | DYNAMIC_COMBO | 否 | `eleven_multilingual_sts_v2`<br>`eleven_english_sts_v2` |
| `目标语音` | 转换的目标语音。从 Voice Selector 或 Instant Voice Clone 连接。 | CUSTOM | 是 | - |
| `源音频` | 要转换的源音频。 | AUDIO | 是 | - |
| `稳定性` | 语音稳定性。较低的值提供更宽的情感范围，较高的值产生更一致但可能单调的语音（默认值：0.5）。 | FLOAT | 否 | 0.0 - 1.0 |
| `输出格式` | 音频输出格式（默认值："mp3_44100_192"）。 | COMBO | 否 | `"mp3_44100_192"`<br>`"opus_48000_192"` |
| `随机种子` | 用于可重现性的种子（默认值：0）。 | INT | 否 | 0 - 4294967295 |
| `去除背景噪音` | 使用音频隔离从输入音频中移除背景噪音（默认值：False）。 | BOOLEAN | 否 | - |

### 语音设置（由 `eleven_multilingual_sts_v2` 和 `eleven_english_sts_v2` 共享）

当选择某个模型时，这些语音设置可用于转换。

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `speed` | 语速。1.0 为正常，<1.0 较慢，>1.0 较快（默认值：1.0）。 | FLOAT | 否 | 0.7 - 1.3 |
| `similarity_boost` | 相似度增强。较高的值使语音更接近原始语音（默认值：0.75）。 | FLOAT | 否 | 0.0 - 1.0 |
| `use_speaker_boost` | 增强与原始说话人语音的相似度（默认值：False）。 | BOOLEAN | 否 | - |
| `style` | 风格夸张程度。较高的值会增加风格化表达，但可能降低稳定性（默认值：0.0）。 | FLOAT | 否 | 0.0 - 0.2 |

## 输出
| 输出名 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `audio` | 以指定输出格式生成的转换后音频文件。 | AUDIO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToSpeech/zh.md)

---
**Source fingerprint (SHA-256):** `a3cd602181d134b9ab517bfac092ea30b62ef5a9942a905c0c3e6959b34370ca`
