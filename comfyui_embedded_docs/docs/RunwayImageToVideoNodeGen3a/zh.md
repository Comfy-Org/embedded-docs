# Runway图像转视频（Gen3a Turbo）

Runway Image to Video（Gen3a Turbo）节点使用 Runway 的 Gen3a Turbo 模型，从单个起始帧生成视频。它接收文本提示和初始图像帧，然后根据指定的时长和宽高比创建视频序列。此节点连接到 Runway 的 API 以远程处理生成任务。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用于生成的文本提示（默认：""） | STRING | 是 | N/A |
| `start_frame` | 用于视频的起始帧 | IMAGE | 是 | N/A |
| `duration` | 视频时长（秒）（默认："5"） | COMBO | 是 | `"5"`<br>`"10"` |
| `ratio` | 生成视频的宽高比（默认："768:1280"） | COMBO | 是 | `"768:1280"`<br>`"1280:768"` |
| `seed` | 生成的随机种子（默认：0） | INT | 否 | 0 to 4294967295 |

**参数约束：**

- `start_frame` 的尺寸不得超过 7999x7999 像素。
- `start_frame` 的宽高比必须在 0.5 到 2.0 之间。
- `prompt` 必须至少包含一个字符（不能为空）。

**注意：**

- 此节点已弃用。
- 在生成之前，Runway 建议查阅其最佳实践指南：https://help.runwayml.com/hc/en-us/articles/33927968552339-Creating-with-Act-One-on-Gen-3-Alpha-and-Turbo

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `output` | 生成的视频序列 | VIDEO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/zh.md)

---
**Source fingerprint (SHA-256):** `ff66cbdfa80aabeaf96d43e7822dd0c700ee027d13fb430a9dc2079e1a23f38e`
