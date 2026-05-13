> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/zh.md)

此文档由 AI 生成。如发现任何错误或有改进建议，欢迎随时贡献！[在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/en.md)

Topaz Video Enhance 节点使用外部 API 来提升视频质量。它可以对视频进行分辨率放大、通过插值提高帧率以及应用压缩。该节点处理输入的 MP4 视频，并根据所选设置返回增强后的版本。

## 输入

| 参数 | 数据类型 | 是否必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | 是 | - | 待增强的输入视频文件。 |
| `upscaler_enabled` | BOOLEAN | 是 | - | 启用或禁用视频放大功能（默认值：True）。 |
| `upscaler_model` | COMBO | 是 | `"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"` | 用于放大视频的 AI 模型。 |
| `upscaler_resolution` | COMBO | 是 | `"FullHD (1080p)"`<br>`"4K (2160p)"` | 放大视频的目标分辨率。 |
| `upscaler_creativity` | COMBO | 否 | `"low"`<br>`"middle"`<br>`"high"` | 创意级别（仅适用于 Starlight (Astra) Creative 模型，默认值："low"）。 |
| `interpolation_enabled` | BOOLEAN | 否 | - | 启用或禁用帧插值功能（默认值：False）。 |
| `interpolation_model` | COMBO | 否 | `"apo-8"` | 用于帧插值的模型（默认值："apo-8"）。 |
| `interpolation_slowmo` | INT | 否 | 1 到 16 | 应用于输入视频的慢动作倍率。例如，设为 2 时，输出视频速度减半，时长加倍（默认值：1）。 |
| `interpolation_frame_rate` | INT | 否 | 15 到 240 | 输出帧率（默认值：60）。 |
| `interpolation_duplicate` | BOOLEAN | 否 | - | 分析输入视频中的重复帧并将其移除（默认值：False）。 |
| `interpolation_duplicate_threshold` | FLOAT | 否 | 0.001 到 0.1 | 重复帧检测灵敏度（默认值：0.01）。 |
| `dynamic_compression_level` | COMBO | 否 | `"Low"`<br>`"Mid"`<br>`"High"` | CQP 级别（默认值："Low"）。 |

**注意：** 必须至少启用一项增强功能。如果 `upscaler_enabled` 和 `interpolation_enabled` 均设为 `False`，节点将报错。输入视频必须为 MP4 格式。

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `video` | VIDEO | 增强后的输出视频文件。 |

---
**Source fingerprint (SHA-256):** `70e1a6e0d7bd250f58c43beefe070fd83af19d11ac08cb9a6ac9655a9bfa839f`
