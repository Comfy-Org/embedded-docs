# Bria 视频更换背景

使用 Bria 将视频的背景替换为提供的图像或视频。输出保持前景的分辨率和帧率；不同宽高比的背景会被拉伸以适应，因此请匹配宽高比，以免失真。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `video` | 前景视频，其背景将被替换。 | VIDEO | 是 | - |
| `background_image` | 用于合成到前景后面的背景图像。提供背景图像或背景视频，但不要同时提供两者。 | IMAGE | 否 | - |
| `background_video` | 用于合成到前景后面的背景视频。提供背景图像或背景视频，但不要同时提供两者。 | VIDEO | 否 | - |
| `seed` | 种子控制节点是否重新运行；无论种子如何，结果都是非确定性的。（默认值：0） | INT | 是 | 0 to 2147483647 |

**注意：** 您必须且只能提供 `background_image` 或 `background_video` 之一——不能同时提供两者，也不能两者都不提供。前景视频和背景视频都必须不超过 60 秒。如果提供了背景图像，其 alpha（透明度）通道将在上传前被移除。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `video` | 替换背景后的结果视频。 | VIDEO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoReplaceBackground/zh.md)

---
**Source fingerprint (SHA-256):** `c487cf7dd434b8523ce64f241c2171c82bb5e0abdc5c3ca3e8b1a1259aeab490`
