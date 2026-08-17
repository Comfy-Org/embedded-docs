# 保存音频

SaveAudio 节点将音频数据保存为 FLAC 格式的文件。它接收音频输入，使用指定的文件名前缀将其写入输出目录，并将相同的音频作为输出传递。此节点已弃用，应替换为当前的 Save Audio 节点。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `audio` | 要保存的音频数据 | AUDIO | 是 | - |
| `filename_prefix` | 输出文件名的前缀（默认值："audio/ComfyUI"） | STRING | 否 | - |

如果 `audio` 为 None，节点会引发错误，这可能在源视频没有音轨时发生。

`prompt` 和 `extra_pnginfo` 参数是隐藏的，由系统自动处理。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `audio` | 已保存到文件的相同音频数据 | AUDIO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudio/zh.md)

---
**Source fingerprint (SHA-256):** `6ac62d315f14213091cd179a05f0bbd51f1b1a5056bb5c06ca137d2b574d6017`
