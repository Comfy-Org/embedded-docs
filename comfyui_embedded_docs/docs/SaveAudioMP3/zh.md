# 保存音频 (MP3)

SaveAudioMP3 节点将音频数据保存为 MP3 文件。它接收音频输入，并使用可自定义的文件名前缀和质量设置将其写入输出目录。此节点已弃用，可能在未来的版本中移除。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `audio` | 要保存为 MP3 文件的音频数据 | AUDIO | 是 | - |
| `filename_prefix` | 输出文件名的前缀（默认值：`"audio/ComfyUI"`） | STRING | 否 | - |
| `quality` | MP3 编码质量设置（默认值：`"V0"`）。V0 使用可变比特率以获得高质量；128k 和 320k 使用 128 和 320 kbps 的固定比特率 | COMBO | 否 | `"V0"`<br>`"128k"`<br>`"320k"` |
| `prompt` | 内部提示数据，由系统自动提供 | PROMPT | 否 | - |
| `extra_pnginfo` | 附加 PNG 信息，由系统自动提供 | EXTRA_PNGINFO | 否 | - |

**注意：** 如果 `audio` 输入为 None（例如，当源视频没有音轨时），该节点会引发 ValueError。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `audio` | 已保存为 MP3 文件的音频数据 | AUDIO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioMP3/zh.md)

---
**Source fingerprint (SHA-256):** `7d3b439dfd7cb211dd6568f6b5124bb225909dcf0ae150addc4ca226d947a4f0`
