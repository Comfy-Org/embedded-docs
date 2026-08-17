# 规格化视频Latent

此节点调整视频潜空间的前几帧，使其看起来更像后续帧。它根据视频中较后的一组参考帧计算平均值和方差，并将这些相同的特征应用于起始帧。这有助于在视频开头创建更平滑、更一致的视觉效果过渡。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `latent` | 要处理的视频潜空间表示。 | LATENT | 是 | - |
| `start_frame_count` | 要从开头开始归一化的潜空间帧数（默认：4）。 | INT | 是 | 1 to 16384 (max resolution) |
| `reference_frame_count` | 在起始帧之后用作参考的潜空间帧数（默认：5）。 | INT | 是 | 1 to 16384 (max resolution) |

**注意：** `reference_frame_count` 会自动限制为起始帧之后可用的帧数。如果视频潜空间只有 1 帧，则不执行归一化，并原样返回原始潜空间。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `latent` | 已处理的视频潜空间，起始帧已归一化。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/zh.md)

---
**Source fingerprint (SHA-256):** `383e5a19ee4cd8bdea5983567ddbdc30bb09c373142a1a934cea985f1b9d1b0d`
