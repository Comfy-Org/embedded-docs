# Wan 2.7 参考生成视频

此节点根据提供的参考素材，生成包含人物或物体的视频。它使用 Wan 2.7 模型从文本提示生成视频，支持单角色表演和多角色交互。你必须至少提供一个参考视频或参考图像，生成才能正常工作。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 用于视频生成的特定模型。 | COMBO | 是 | "wan2.7-r2v" |
| `seed` | 用于生成的随机种子，有助于控制输出的随机性（默认值：0）。 | INT | 否 | 0 到 2147483647 |
| `watermark` | 是否在结果中添加 AI 生成的水印（默认值：False）。这是一个高级设置。 | BOOLEAN | 否 | True<br>False |

### wan2.7-r2v 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `prompt` | 描述视频的提示词。使用诸如“character1”和“character2”之类的标识符来引用参考角色。必须至少包含一个角色。 | STRING | 是 | - |
| `negative_prompt` | 描述应避免内容的负面提示词（默认值：空）。 | STRING | 否 | - |
| `resolution` | 输出视频的分辨率。 | COMBO | 是 | "720P"<br>"1080P" |
| `ratio` | 输出视频的宽高比。 | COMBO | 是 | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `duration` | 生成视频的时长（秒）（默认值：5）。 | INT | 是 | 2 到 10 |

### 参考输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model.reference_videos` | 可增长插槽：连接最多 3 个参考视频（插槽 `video1` 到 `video3`）。整体至少需要一个参考视频或参考图像。 | VIDEO | 否 | 0 到 3 项 |
| `model.reference_images` | 可增长插槽：连接最多 5 个参考图像（插槽 `image1` 到 `image5`）。整体至少需要一个参考视频或参考图像。 | IMAGE | 否 | 0 到 5 项 |

**重要限制：**

* 你必须在 `model.reference_videos` 或 `model.reference_images` 输入中至少提供一个参考视频或参考图像。
* 参考视频和参考图像的总数不能超过 5。
* `model.prompt` 输入必须至少包含一个角色。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `output` | 生成的视频文件。 | VIDEO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ReferenceVideoApi/zh.md)

---
**Source fingerprint (SHA-256):** `52ac550522bf3fe8f57444ce8586fe83be470b893ff8c01292743553cfbd623d`
