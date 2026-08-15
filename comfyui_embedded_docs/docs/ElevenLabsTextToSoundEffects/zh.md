# ElevenLabs 文本转音效

ElevenLabs Text to Sound Effects 节点使用 ElevenLabs API 根据文本描述生成音效音频。它会将您编写的提示词发送到 ElevenLabs 声音生成服务，并返回生成的音频，同时提供对持续时间、循环行为以及声音与文本匹配程度的控制。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 用于音效生成的模型。所选模型决定了下文列出的可用生成参数。 | DYNAMIC_COMBO | 是 | `"eleven_sfx_v2"` |
| `文本` | 要生成的音效的文本描述。必须包含至少 1 个字符。（默认值：空） | STRING | 是 | N/A |
| `输出格式` | 音频输出格式。 | COMBO | 是 | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### Eleven SFX v2 输入

当 `model` 设置为 `"eleven_sfx_v2"` 时显示的子参数。

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `duration` | 生成声音的持续时间（秒）。（默认值：5.0） | FLOAT | 是 | 0.5 到 30.0 (步长: 0.1) |
| `loop` | 创建平滑循环播放的音效。（默认值：False） | BOOLEAN | 否 | True or False |
| `prompt_influence` | 生成结果遵循提示词的程度。数值越高，声音与文本的匹配度越高。（默认值：0.3） | FLOAT | 是 | 0.0 到 1.0 (步长: 0.01) |

## 输出

| 输出名 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `audio` | 生成的音效音频文件。 | AUDIO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSoundEffects/zh.md)

---
**Source fingerprint (SHA-256):** `218ff617256cea33f310c1bcfc6407c46aaadc59201a0324b0ec64583166ce58`
