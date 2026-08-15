# Luma Ray 3.2 关键帧

此节点将引导图像锚定到 Luma Ray 3.2 输出视频时间线上的特定位置。将此节点连接到 Luma Ray 3.2 Keyframes to Video 节点的 `keyframes` 输入，并通过连接可选的 `keyframes` 输入将多个关键帧链接在一起。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要放置在输出视频选定时刻的引导图像。 | IMAGE | 是 | - |
| `position` | 如何将此图像放置在输出视频的时间线上。 | COMBO | 是 | "Fraction of duration (0.0-1.0)"<br>"Absolute time (seconds)" |
| `keyframes` | 可选的更早关键帧，用于与此关键帧链接。 | LUMA_RAY32_KEYFRAME | 否 | - |

当为 `position` 参数选择"Fraction of duration (0.0-1.0)"时，您可以指定一个 `fraction` 值（默认值：0.0，范围：0.0 到 1.0，步长：0.01），该值决定此图像应用于输出视频的哪一位置（0.0 = 开始，1.0 = 结束）。

当为 `position` 参数选择"Absolute time (seconds)"时，您可以指定一个 `seconds` 值（默认值：0.0，范围：0.0 到 10.0，步长：0.1），该值决定此图像在输出视频中应用的时间点（距视频开始的秒数）。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `keyframes` | 一个关键帧链，包含新关键帧与任何可选早期关键帧的组合。 | LUMA_RAY32_KEYFRAME |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32KeyframeNode/zh.md)

---
**Source fingerprint (SHA-256):** `b49d879888e6e83d6937068e799ea583ed5c90284e829ac496821eea330fe9c7`
