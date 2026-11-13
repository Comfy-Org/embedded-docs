# Split Image Channels

将图像拆分为红色、绿色和蓝色通道，并将 Alpha 通道作为掩码返回。每个颜色输出都是三通道灰度图像，因此可以像普通图像一样预览和保存。可用于检查或编辑单个通道，或从图像中提取透明度。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `image` | 要拆分的图像。单通道（灰度）输入会被扩展，使三个颜色输出都携带相同的数据。 | IMAGE | 是 | - |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `red` | 红色通道，表示为三通道灰度图像。 | IMAGE |
| `green` | 绿色通道，表示为三通道灰度图像。 | IMAGE |
| `blue` | 蓝色通道，表示为三通道灰度图像。 | IMAGE |
| `alpha` | 以掩码形式表示的 Alpha，采用与 Load Image 相同的反转方式，因此 1 表示完全透明的像素。没有 Alpha 通道的图像会返回全零掩码。 | MASK |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageChannels/zh.md)

---
**Source fingerprint (SHA-256):** `0f300d2e86c74e856001eb82da26c871c94c1dae5ec73a4504ca258420fbcf52`
