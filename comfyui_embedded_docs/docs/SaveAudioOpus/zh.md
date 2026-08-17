# 保存音频 (Opus)

SaveAudioOpus 节点将音频数据保存为 Opus 格式文件。它接收音频输入，并以可配置的质量设置将其导出为压缩 Opus 文件。该节点已弃用，可能会在未来版本中移除。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `audio` | 要保存为 Opus 文件的音频数据。如果未提供音频（例如源视频没有音轨），节点将引发错误。 | AUDIO | 是 | - |
| `filename_prefix` | 输出文件名的前缀（默认值："audio/ComfyUI"） | STRING | 否 | - |
| `quality` | Opus 文件的音频质量（比特率）设置（默认值："128k"） | COMBO | 否 | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" |

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `audio` | 输入音频数据，在 Opus 文件保存到磁盘后返回。 | AUDIO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/zh.md)

---
**Source fingerprint (SHA-256):** `a2f585f45299759738fa85f6b73f51680d4e86da57d3fc9c2236e66114fa3d6c`
