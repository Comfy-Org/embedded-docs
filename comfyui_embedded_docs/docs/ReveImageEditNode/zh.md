> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageEditNode/zh.md)

Reve Image Edit 节点允许您基于文本描述修改现有图像。它使用 Reve API 来解读您的指令，并将请求的更改应用到您提供的图像上。

## 输入参数

| 参数 | 数据类型 | 必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 待编辑的图像。 |
| `edit_instruction` | STRING | 是 | - | 描述如何编辑图像的文本。最多 2560 个字符。 |
| `model` | MODEL | 是 | `"reve-edit@20250915"`<br>`"reve-edit-fast@20251030"`<br>`"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` | 用于编辑的模型版本。选项包括特定的模型版本和宽高比设置。 |
| `upscale` | COMBO | 否 | `"disabled"`<br>`"enabled"` | 控制是否对生成的图像进行放大。 |
| `upscale_factor` | FLOAT | 否 | - | 当启用放大时，图像放大的倍数。 |
| `remove_background` | BOOLEAN | 否 | - | 控制是否从生成的图像中移除背景。 |
| `seed` | INT | 否 | 0 到 2147483647 | 种子控制节点是否应重新运行；无论种子如何，结果都是非确定性的。（默认值：0） |

**注意：** 仅当 `upscale` 参数设置为 `"enabled"` 时，`upscale_factor` 参数才相关。

## 输出参数

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `image` | IMAGE | 根据指令生成的已编辑图像。 |