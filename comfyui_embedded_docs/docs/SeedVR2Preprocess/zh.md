# 预处理 SeedVR2 输入

此节点对调整大小后的图像进行填充，以准备用于 SeedVR2 模型。它在处理过程中移除 alpha 通道，稍后由配套的 Post-Process SeedVR2 Output 节点使用原始调整大小后的图像恢复该通道。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `resized_images` | 要处理的调整大小后的图像。 | IMAGE | 是 | - |

注意：输入可以是单个图像或帧序列（例如视频的帧）。其较短边至少为 2 像素。在处理过程中，alpha 通道（如果存在）会被移除，像素值被限制在 [0, 1] 范围内，宽度和高度会被填充为 16 的倍数。帧序列会被填充，使其长度遵循 1、5、9、13、... 帧的模式。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `images` | 用于 VAE 编码的填充图像。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Preprocess/zh.md)

---
**Source fingerprint (SHA-256):** `f4fa433d299feba40696f27ff365c59988e5102112f09536724b5db5b09416bb`
