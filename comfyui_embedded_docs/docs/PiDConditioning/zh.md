# PiD 条件处理

将潜在图像和降级 sigma 值附加到 CONDITIONING 数据。这用于 PiD（像素级细节）解码或放大，允许你在处理前控制潜在图像被降级的程度。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 要附加潜在图像和降级 sigma 的 conditioning 数据。 | CONDITIONING | 是 | - |
| `latent` | 要附加到 conditioning 的潜在图像（来自 VAEEncode 或 KSampler）。 | LATENT | 是 | - |
| `latent_format` | 潜在图像的格式。Flux1（16 通道）和 Flux2（128 通道）潜在图像会根据“flux”下的通道维度自动检测。对于 SD3（16 通道）、SDXL（4 通道）或 QwenImage（16 通道），请手动选择（默认："flux"）。 | COMBO | 是 | `"flux"`<br>`"sd3"`<br>`"sdxl"`<br>`"qwenimage"` |
| `degrade_sigma` | 0 = 干净的潜在图像。增大该值可对损坏的潜在输出进行去噪（默认：0.0）。 | FLOAT | 是 | 0.0 到 1.0（步长：0.01） |

注意：当 `latent_format` 为 "flux" 时，节点会根据通道维度自动检测潜在图像是 Flux1（16 通道）还是 Flux2（128 通道）。如果处理后的潜在图像有 5 个维度，则只使用沿最后一个维度的第一个切片。

## 输出

| 输出名 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `CONDITIONING` | 原始 conditioning 数据，附加了潜在图像和降级 sigma 值。 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/zh.md)

---
**Source fingerprint (SHA-256):** `24f613b33e7872cb35f458aa5794a3cc4d37ceaecd43725039edef75f4a512bc`
