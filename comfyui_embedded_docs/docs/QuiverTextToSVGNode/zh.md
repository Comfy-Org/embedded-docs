> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverTextToSVGNode/zh.md)

Quiver Text to SVG 节点使用 Quiver AI 的模型，根据文本描述生成可缩放矢量图形（SVG）图像。您可以选择性地提供参考图像和风格指令来引导生成过程。

## 输入参数

| 参数 | 数据类型 | 必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | 不适用 | 期望 SVG 输出的文本描述。这是生成内容的主要指令。 |
| `instructions` | STRING | 否 | 不适用 | 额外的风格或格式指导。这是一个可选的高级参数。 |
| `reference_images` | IMAGE | 否 | 不适用 | 最多 4 张用于引导生成的参考图像。这是一个可选输入。 |
| `model` | COMBO | 是 | 提供多个选项 | 用于 SVG 生成的模型。可用选项由 Quiver API 决定。 |
| `seed` | INT | 是 | 0 到 2147483647 | 用于确定节点是否应重新运行的种子；无论种子如何，实际结果都是非确定性的。默认值：0。 |

**注意：** `reference_images` 输入最多接受 4 张图像。如果提供更多，节点将引发错误。

## 输出结果

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `SVG` | SVG | 生成的可缩放矢量图形（SVG）图像。 |