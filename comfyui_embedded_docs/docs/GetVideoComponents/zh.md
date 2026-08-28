# 获取视频元素

「Get Video Components」节点从视频文件中提取所有主要元素。它将视频分离为单独的帧，提取音轨，并提供视频的帧率、位深度和色彩空间信息。这样，您就可以独立处理每个组件，以进行进一步的处理或分析。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|------|------|----------|------|------|
| `视频` | 要提取组件的视频。 | VIDEO | 是 | - |

## 输出

| 输出名称 | 描述 | 数据类型 |
|----------|------|----------|
| `图像` | 从视频中提取的各个帧，以独立图像的形式呈现。 | IMAGE |
| `音频` | 从视频中提取的音轨。 | AUDIO |
| `帧率` | 视频的帧率，以每秒帧数表示。 | FLOAT |
| `bit_depth` | 视频的位深度。 | INT |
| `color_space` | 视频的色彩空间。 | COMBO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetVideoComponents/zh.md)

---
**Source fingerprint (SHA-256):** `ffe8b6c698cb9a855b8796768f068d403448cf56188ce4c5ead21bff30baff6e`
