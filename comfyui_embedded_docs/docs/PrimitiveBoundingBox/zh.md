# 边界框

PrimitiveBoundingBox 节点创建一个由其位置和大小定义的简单矩形区域。它接收左上角的 X 和 Y 坐标以及宽度和高度值，并输出一个边界框数据结构，可供工作流中的其他节点使用。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `x` | 边界框左上角的 X 坐标（默认值：0）。 | INT | 是 | 0 至 8192 |
| `y` | 边界框左上角的 Y 坐标（默认值：0）。 | INT | 是 | 0 至 8192 |
| `width` | 边界框的宽度（默认值：512）。 | INT | 是 | 1 至 8192 |
| `height` | 边界框的高度（默认值：512）。 | INT | 是 | 1 至 8192 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `bounding_box` | 包含该矩形 `x`、`y`、`width` 和 `height` 属性的数据结构。 | BOUNDING_BOX |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveBoundingBox/zh.md)

---
**Source fingerprint (SHA-256):** `dc50286b09b8aaf7ff21eb699b9a04317f099b3deedb6cb7d4a1ec7668edeb97`
