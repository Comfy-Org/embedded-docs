# LTXV 图像到视频

LTXV 图像转视频节点可根据单个起始图像生成专业质量的视频。它使用外部 API，根据您的文本提示创建视频序列，允许您自定义时长、分辨率和帧率。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `image` | 用于视频的第一帧。 | IMAGE | 是 | - |
| `model` | 用于视频生成的 AI 模型。“Pro”模型针对质量进行了优化，而“Fast”模型针对速度进行了优化。 | COMBO | 是 | `"LTX-2 (Pro)"`<br>`"LTX-2 (Fast)"` |
| `prompt` | 指导生成视频内容和运动的文本描述。 | STRING | 是 | - |
| `duration` | 视频时长（以秒为单位，默认值：8）。 | COMBO | 是 | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` |
| `resolution` | 生成视频的输出分辨率。 | COMBO | 是 | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` |
| `fps` | 视频帧率（每秒帧数，默认值：25）。 | COMBO | 是 | `25`<br>`50` |
| `generate_audio` | 为 true 时，生成的视频将包含与场景匹配的 AI 生成音频（默认值：False）。 | BOOLEAN | 否 | - |

**重要约束：**

* `image` 输入必须只包含一张图像。
* `prompt` 的长度必须在 1 到 10,000 个字符之间。
* 如果您选择的 `duration` 超过 10 秒，则必须使用 **“LTX-2 (Fast)”** 模型、**“1920x1080”** 分辨率和 **25** FPS。较长的视频需要此组合。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `video` | 生成的视频文件。 | VIDEO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiImageToVideo/zh.md)

---
**Source fingerprint (SHA-256):** `fa3928262e59105718b6ed97ddc8d2801e540b6b0c142541d92525dd75540cc7`
