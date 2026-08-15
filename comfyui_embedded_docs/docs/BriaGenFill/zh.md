# BriaGenFill

此节点使用 Bria API 在图像的遮罩区域内生成物体或场景。它会上传图像和遮罩，将提示词发送至 Bria 生成式填充服务，等待操作完成，然后返回编辑后的图像。这是一项付费 API 操作（每次请求 0.0429 美元）。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要编辑的输入图像。 | IMAGE | 是 | - |
| `mask` | 白色区域将被生成的内容填充，黑色区域将被保留。遮罩在发送前会进行二值化处理，因此部分绘制的区域会被视为白色。遮罩必须与图像具有相同的宽高比。 | MASK | 是 | - |
| `prompt` | 对遮罩区域内要生成内容的描述。必须至少包含 1 个字符。 | STRING | 是 | - |
| `negative_prompt` | 描述生成结果中应避免的内容的提示词。如果留空，则不会发送到 API。 | STRING | 是 | - |
| `refine_prompt` | 自动调整提示词以获得更好的结果；禁用后则完全按照原样使用提示词。（默认值：true） | BOOLEAN | 是 | true<br>false |
| `seed` | 生成过程的随机种子。（默认值：42） | INT | 是 | 1 到 2147483647 |
| `moderation` | 请求的审核设置。设置为“true”时，将应用下文所述的嵌套审核选项。（默认值：“false”） | COMBO | 是 | “false”<br>“true” |

注意：`prompt` 不能为空，且 `mask` 必须与 `image` 具有相同的宽高比。遮罩会在 50% 不透明度下进行二值化处理，因此不透明度低于一半的绘制区域将被忽略；如果二值化后遮罩中不含任何白色区域，节点将抛出错误。

当 `moderation` 设置为“true”时，以下嵌套布尔选项可用：
- `prompt_content_moderation`（默认值：false）：对提示词应用内容审核。
- `visual_input_moderation`（默认值：false）：对输入图像应用内容审核。
- `visual_output_moderation`（默认值：false）：对输出图像应用内容审核。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `image` | 遮罩区域已被生成内容填充的结果图像。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaGenFill/zh.md)

---
**Source fingerprint (SHA-256):** `0d9babfa5e14c03f73d2b5befbd1c5cd1f5ffc685a0d7ccb3db09cfec51ba4fa`
