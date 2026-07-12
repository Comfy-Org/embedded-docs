# 创建边界框

在画布上绘制边界框。输出 Ideogram 提示元素、像素空间边界框和预览图像。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `背景` | 在画布和预览中用作背景的可选图像。 | IMAGE | No | - |
| `bboxes` | Bounding boxes, elements, or a JSON string to initialize the canvas. A new upstream value initializes the canvas; edits made on the canvas take priority and are kept until the upstream value changes again. | BOUNDING_BOX, ARRAY, STRING | No | - |
| `宽度` | 画布及边界框像素网格的宽度。 | INT | Yes | 64 to 16384 (step: 16) |
| `高度` | 画布及边界框像素网格的高度。 | INT | Yes | 64 to 16384 (step: 16) |
| `编辑器状态` | 绘制边界框并设置每个框的类型、文本、描述、色板。先添加背景元素，最后添加前景元素。 | BOUNDING_BOXES | Yes | - |
| `last_incoming` | Internal state managed by the canvas: the upstream bboxes value that last initialized it. Leave empty to re-initialize the canvas from the bboxes input on the next run. | BOUNDING_BOXES | No | - |

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `preview` | An RGB image showing the canvas with all bounding boxes rendered, including labels, color palette swatches, and descriptive text. | IMAGE |
| `bboxes` | A list of bounding boxes in pixel coordinates, with each box containing x, y, width, and height values. | BOUNDING_BOX |
| `elements` | A structured array of element objects, each containing type, bounding box coordinates (normalized 0-1000), text (for text type), description, and color palette. | ARRAY |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateBoundingBoxes/zh.md)

---
**Source fingerprint (SHA-256):** `dc5545dffefdccf14f3919ff4d9966dbfd1a497dcd64e1863556d5728659ee94`
