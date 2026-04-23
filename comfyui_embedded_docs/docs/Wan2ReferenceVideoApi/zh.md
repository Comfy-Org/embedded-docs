> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ReferenceVideoApi/zh.md)

此节点根据提供的参考素材生成包含人物或对象的视频。它使用 Wan 2.7 模型根据文本提示创建视频，支持单角色表演和多角色互动。您必须提供至少一个参考视频或图像才能使生成工作。

## 输入参数

| 参数 | 数据类型 | 必填 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `"wan2.7-r2v"` | 用于视频生成的具体模型。 |
| `model.prompt` | STRING | 是 | - | 描述视频的提示词。使用诸如 'character1' 和 'character2' 等标识符来指代参考角色。 |
| `model.negative_prompt` | STRING | 否 | - | 描述在生成视频中应避免内容的负面提示词（默认：空）。 |
| `model.resolution` | COMBO | 是 | `"720P"`<br>`"1080P"` | 输出视频的分辨率。 |
| `model.ratio` | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` | 输出视频的宽高比。 |
| `model.duration` | INT | 是 | 2 到 10 | 生成视频的长度，单位为秒（默认：5）。 |
| `model.reference_videos` | VIDEO | 否 | - | 参考视频列表。最多可添加 3 个视频。 |
| `model.reference_images` | IMAGE | 否 | - | 参考图像列表。最多可添加 5 张图像。 |
| `seed` | INT | 否 | 0 到 2147483647 | 用于生成的种子值，有助于控制输出的随机性（默认：0）。 |
| `watermark` | BOOLEAN | 否 | - | 是否在结果中添加 AI 生成的水印（默认：False）。此为高级设置。 |

**重要限制：**
*   您必须在 `model.reference_videos` 或 `model.reference_images` 输入中提供至少一个参考视频或参考图像。
*   参考视频和图像的总数不能超过 5 个。

## 输出参数

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的视频文件。 |