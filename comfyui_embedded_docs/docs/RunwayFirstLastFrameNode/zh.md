# Runway首尾帧转视频

Runway 首尾帧转视频（First-Last-Frame to Video）节点通过上传首帧和尾帧以及文本提示词来生成视频。它使用 Runway 的 Gen-3 模型在提供的起始帧和结束帧之间创建平滑过渡。这对于结束帧与起始帧差异较大的复杂转场尤其有用。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用于生成的文本提示词（默认：空字符串） | STRING | 是 | N/A |
| `start_frame` | 用于视频的起始帧 | IMAGE | 是 | N/A |
| `end_frame` | 用于视频的结束帧。仅 gen3a_turbo 支持。 | IMAGE | 是 | N/A |
| `duration` | 视频时长（秒）（默认："5"） | COMBO | 是 | `"5"`<br>`"10"` |
| `ratio` | 生成视频的宽高比（默认："768:1280"） | COMBO | 是 | `"768:1280"`<br>`"1280:768"` |
| `seed` | 用于生成的随机种子。设为 0 以使用随机种子（默认：0）。 | INT | 否 | 0 到 4294967295 |

**参数约束：**

- `prompt` 必须至少包含 1 个字符
- `start_frame` 和 `end_frame` 的最大尺寸必须为 7999x7999 像素
- `start_frame` 和 `end_frame` 的宽高比必须在 0.5 到 2.0 之间
- 仅当使用 gen3a_turbo 模型时才支持 `end_frame` 参数

**注意：** 此节点已标记为弃用。使用前请查阅 Runway 关于在 Gen-3 上使用关键帧进行创作的实践指南：https://help.runwayml.com/hc/en-us/articles/34170748696595-Creating-with-Keyframes-on-Gen-3

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `output` | 在起始帧和结束帧之间过渡的生成视频 | VIDEO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayFirstLastFrameNode/zh.md)

---
**Source fingerprint (SHA-256):** `1d8720aba833348583d2aa37e13a1ad43d9055b0201c9cb6ad9c95dada7e5056`
