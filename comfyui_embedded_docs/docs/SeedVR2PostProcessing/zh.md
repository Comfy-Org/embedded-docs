# 后处理 SeedVR2 输出

此节点将生成的图像与原始调整大小后的图像对齐，并应用可选的色彩校正。它接收 SeedVR2 放大过程的输出，并调整其以匹配原始参考图像的颜色和尺寸。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `images` | 要处理的生成图像。 | IMAGE | 是 | - |
| `original_resized_images` | 预处理前原始调整大小后的图像，用作参考。 | IMAGE | 是 | - |
| `color_correction_method` | 将生成图像颜色与原始图像匹配的方法。lab：在 CIELAB 色彩空间中传递颜色，保留细节（最忠实）。wavelet：传递低频颜色，保留放大后的高频细节。adain：按通道匹配均值/标准差（最快，全局色调）。none：跳过颜色传递（仅几何对齐）。（默认：`"lab"`） | COMBO | 是 | `"lab"`<br>`"wavelet"`<br>`"adain"`<br>`"none"` |

**注意：** 输出将裁剪为生成图像和参考图像的较小高度和宽度，最终尺寸向下取整为偶数。如果参考图像具有 Alpha 通道（4 通道），则该通道会被保留并应用到输出。两个输入都可以是 4D 或 5D 图像张量，输出使用与生成图像输入相同的维度。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `images` | 对齐并色彩校正后的图像。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2PostProcessing/zh.md)

---
**Source fingerprint (SHA-256):** `00a3a3ef06edc7e0eca8f67a96095920a3e0e885dac3fb676d081e4c4c30bec5`
