# LCM缩放采样器

SamplerLCMUpscale 节点提供了一种专门的采样方法，将潜在一致性模型（LCM）采样与图像放大功能相结合。它允许您在采样过程中使用多种插值方法对图像进行放大，从而在保持图像质量的同时生成更高分辨率的输出。放大处理会在采样步骤中逐步应用，直到达到目标 `scale_ratio`。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `scale_ratio` | 放大过程中应用的缩放因子（默认值：1.0） | FLOAT | 否 | 0.1 - 20.0 |
| `scale_steps` | 用于放大过程的步数。设为 -1 可自动计算（默认值：-1） | INT | 否 | -1 - 1000 |
| `upscale_method` | 用于放大图像的插值方法（默认值：bislerp） | COMBO | 是 | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" |

注意：当 `scale_steps` 设置为正值时，有效的放大步数受采样器总采样步数的限制。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `sampler` | 返回一个配置好的采样器对象，可用于采样流程中 | SAMPLER |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/zh.md)

---
**Source fingerprint (SHA-256):** `5d6f6472fbb4d2c66a8a8b9d6dc34dcc52ac8272589fd6c29e4084d6cab3141b`
