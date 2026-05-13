> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeAndPadImage/zh.md)

ResizeAndPadImage 节点用于将图像调整至指定尺寸范围内，同时保持原始宽高比。它会按比例缩小图像以适配目标宽度和高度，然后在边缘添加填充以填补剩余空间。填充颜色和插值方法可自定义，以控制填充区域的外观和缩放质量。

## 输入

| 参数 | 数据类型 | 是否必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 待调整大小并填充的输入图像 |
| `target_width` | INT | 是 | 1 至 MAX_RESOLUTION | 输出图像的期望宽度（默认值：512） |
| `target_height` | INT | 是 | 1 至 MAX_RESOLUTION | 输出图像的期望高度（默认值：512） |
| `padding_color` | COMBO | 是 | "white"<br>"black" | 用于填充缩放后图像周围区域的颜色（默认值："white"） |
| `interpolation` | COMBO | 是 | "area"<br>"bicubic"<br>"nearest-exact"<br>"bilinear"<br>"lanczos" | 用于调整图像大小的插值方法（默认值："area"） |

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `image` | IMAGE | 调整大小并填充后的输出图像 |

---
**Source fingerprint (SHA-256):** `01566327d46043d1ff9ce404b4df8f49e853d0b01d07cc189fb843157dac1cac`
