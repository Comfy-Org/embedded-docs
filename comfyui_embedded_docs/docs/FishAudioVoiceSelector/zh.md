# FishAudioVoiceSelector

Fish Audio 语音选择节点用于从 Fish Audio 库中选择用于文本转语音生成的语音。您可以选择一个内置预设语音，或选择“custom”以输入 fish.audio 中的任意语音模型 ID。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `voice` | 选择一种语音，或选择“custom”以输入任意 fish.audio 语音模型 ID。 | DYNAMIC_COMBO | 是 | “Energetic Male (en)”<br>“Friendly Women (en)”<br>“Sarah (en)”<br>“Verity (en)”<br>“Polo (en)”<br>“Adrian (en)”<br>“E-girl (en)”<br>“Narrator (en)”<br>“Warm Conversational Voice (en)”<br>“Warm Storyteller (en)”<br>“Dramatic Character Male (en)”<br>“News Narrator (zh)”<br>“Lively Female (zh)”<br>“Gentle Female (zh)”<br>“Energetic Female (ja)”<br>“Calm Female (ja)”<br>“Calm Male (ja)”<br>“custom” |

预设语音选项涵盖英语（en）、中文（zh）和日语（ja）语音，且无需任何额外输入。

### 自定义输入

当 `voice` 设置为“custom”时，会出现以下输入。

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `voice_id` | 来自 fish.audio 的语音模型 ID，例如 https://fish.audio/m/<id>/ 中的 ID。默认值：空字符串。 | STRING | 是 | 任意有效的 Fish Audio 语音模型 ID |

注意：当 `voice` 设置为“custom”时，`voice_id` 在去除首尾空格后不能为空；否则节点会抛出“Custom voice ID is empty.”错误。如果传入了无法识别的语音选项，节点会抛出“Unknown voice”错误。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `voice` | 所选的 Fish Audio 语音模型 ID。对于预设语音，返回 Fish Audio 库中对应的语音 ID；对于“custom”，返回输入的 `voice_id` 值。 | FISHAUDIO_VOICE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioVoiceSelector/zh.md)

---
**Source fingerprint (SHA-256):** `4f99a58aa7e6054f58fe84e61e4e1008b17828bd97d71ef0a4009c4de4052bbd`
