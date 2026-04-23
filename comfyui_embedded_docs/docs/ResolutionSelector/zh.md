> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionSelector/zh.md)

分辨率选择器节点根据选定的宽高比和目标总分辨率（以百万像素为单位）计算图像的像素宽度和高度。该节点可用于为其他节点（如空潜像节点）生成一致的尺寸。输出尺寸始终四舍五入到最接近的8的倍数。

## 输入参数

| 参数 | 数据类型 | 必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `aspect_ratio` | COMBO | 是 | `"SQUARE"`<br>`"PORTRAIT_2_3"`<br>`"PORTRAIT_3_4"`<br>`"PORTRAIT_9_16"`<br>`"LANDSCAPE_3_2"`<br>`"LANDSCAPE_4_3"`<br>`"LANDSCAPE_16_9"` | 输出尺寸的宽高比（默认：`"SQUARE"`）。 |
| `megapixels` | FLOAT | 是 | 0.1 - 16.0 | 目标总百万像素数。对于正方形宽高比，1.0 MP ≈ 1024×1024（默认：1.0）。 |

## 输出参数

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `width` | INT | 计算出的像素宽度，为8的倍数。 |
| `height` | INT | 计算出的像素高度，为8的倍数。 |