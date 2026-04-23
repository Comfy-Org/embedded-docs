> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverImageToSVGNode/zh.md)

此节点使用 Quiver AI 的矢量化模型将栅格图像转换为可缩放矢量图形（SVG）。它会将图像发送到外部 API 进行处理，并返回矢量化结果。

## 输入参数

| 参数 | 数据类型 | 必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | 不适用 | 待矢量化的输入图像。 |
| `auto_crop` | BOOLEAN | 否 | `True`<br>`False` | 自动裁剪至主要主体。这是一个高级参数（默认值：`False`）。 |
| `model` | DYNAMICCOMBO | 是 | 提供多个选项 | 用于 SVG 矢量化的模型。选择模型会显示该模型特有的附加参数：`target_size`（正方形调整目标尺寸，单位：像素，默认值：1024，范围：128-4096）、`temperature`、`top_p` 和 `presence_penalty`。 |
| `seed` | INT | 否 | 0 至 2147483647 | 用于确定节点是否应重新运行的种子值；无论种子值如何，实际结果都是非确定性的。此参数具有"生成后控制"功能（默认值：0）。 |

## 输出结果

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `SVG` | SVG | 矢量化的 SVG 输出。 |