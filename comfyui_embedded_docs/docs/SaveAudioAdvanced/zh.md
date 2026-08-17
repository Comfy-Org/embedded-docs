# 保存音频（高级）

保存音频（高级）

将输入音频保存到您的 ComfyUI 输出目录。您可以导出 FLAC、MP3 或 Opus 格式的音频，并可针对 MP3 和 Opus 文件选择质量设置。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `format` | 用于保存音频的文件格式。 | DYNAMIC_COMBO | 是 | "flac"<br>"mp3"<br>"opus" |
| `audio` | 要保存的音频。 | AUDIO | 是 | - |
| `filename_prefix` | 保存文件的前缀。可包含格式化标记，如 %date:yyyy-MM-dd%。 （默认值："audio/ComfyUI"） | STRING | 是 | - |

### flac 输入

`flac` 格式不需要任何额外设置。

### mp3 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `quality` | MP3 文件的编码质量。 （默认值："V0"） | COMBO | 是 | "V0"<br>"128k"<br>"320k" |

### opus 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `quality` | Opus 文件的编码质量。 （默认值："128k"） | COMBO | 是 | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" |

**注意：** 仅当 `format` 为 `mp3` 或 `opus` 时才会显示 `quality` 设置。如果未提供 `quality` 值，则使用所选格式的默认质量保存音频。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `audio` | 音频输入，保存后原样输出。 | AUDIO |
| `ui` | 包含已保存音频文件信息的 UI 输出。 | UI |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioAdvanced/zh.md)

---
**Source fingerprint (SHA-256):** `5f3af49670b485bbd31f0ed0c5667c12e9b9b23014cadcf64442a486255d0e6d`
