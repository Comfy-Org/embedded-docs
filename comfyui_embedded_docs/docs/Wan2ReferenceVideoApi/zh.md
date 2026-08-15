# Wan 2.7 参考生成视频

此节点根据提供的参考素材生成包含人物或对象的视频。它使用 Wan 2.7 模型基于文本提示生成视频，支持单角色表演和多角色互动。您必须至少提供一个参考视频或参考图像，才能进行生成。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 用于视频生成的特定模型。 | DYNAMIC_COMBO | 是 | "wan2.7-r2v" |
| `seed` | 用于生成的种子值，有助于控制输出的随机性（默认值：0）。 | INT | 否 | 0 to 2147483647 |
| `watermark` | 是否在结果中添加 AI 生成的水印（默认值：False）。这是一项高级设置。 | BOOLEAN | 否 | True<br>False |

### wan2.7-r2v 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `model.prompt` | 描述视频的提示词。使用如 'character1' 和 'character2' 之类的标识符来指代参考角色。必须至少包含一个角色。 | STRING | 是 | - |
| `model.negative_prompt` | 描述应避免内容的负面提示词（默认值：空）。 | STRING | 否 | - |
| `model.resolution` | 输出视频的分辨率。 | COMBO | 是 | "720P"<br>"1080P" |
| `model.ratio` | 输出视频的长宽比。 | COMBO | 是 | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `model.duration` | 生成视频的时长（秒）（默认值：5）。 | INT | 是 | 2 to 10 |

### 参考输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `model.reference_videos` | 可增长插槽：最多连接 3 个参考视频（插槽 `video1` 至 `video3`）。整体至少需要 1 个参考视频或参考图像。 | VIDEO | 否 | 0 to 3 items |
| `model.reference_images` | 可增长插槽：最多连接 5 个参考图像（插槽 `image1` 至 `image5`）。整体至少需要 1 个参考视频或参考图像。 | IMAGE | 否 | 0 to 5 items |

**重要约束：**

* 您必须在 `model.reference_videos` 或 `model.reference_images` 输入中至少提供一个参考视频或参考图像。
* 参考视频和参考图像的总数不能超过 5 个。
* `model.prompt` 输入必须至少包含一个角色。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `output` | 生成的视频文件。 | VIDEO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ReferenceVideoApi/zh.md)

---
**Source fingerprint (SHA-256):** `52ac550522bf3fe8f57444ce8586fe83be470b893ff8c01292743553cfbd623d`
