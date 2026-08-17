# 预览音频

PreviewAudio 节点允许您直接在界面中预览音频，而无需将其保存到 ComfyUI 输出目录。它接收音频数据作为输入，并显示一个音频播放器控件，您可以使用它来试听结果。如果输入的音频为 None，节点将引发错误，这种情况可能发生在源视频没有音轨时。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `audio` | 要预览的音频数据。如果音频为 None（可能发生在源视频没有音轨时），节点将引发错误。 | AUDIO | 是 | - |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `audio` | 通过节点的音频数据。界面中会显示一个音频播放器控件，用于预览该音频。 | AUDIO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/zh.md)

---
**Source fingerprint (SHA-256):** `ccbf9873a16bf1578fe25d178454d782f4f9b37ad5721721bef0aee3ff374f9f`
