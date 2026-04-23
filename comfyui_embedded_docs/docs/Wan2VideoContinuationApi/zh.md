> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoContinuationApi/zh.md)

Wan 2.7 视频延续节点用于生成一段新的视频片段，该片段能够与输入视频片段的末尾实现无缝衔接。它利用 Wan 2.7 模型，根据文本提示来合成延续部分，并可以选择性地引导视频结尾朝向特定的目标帧。

## 输入参数

| 参数 | 数据类型 | 必填 | 范围 | 描述 |
| :--- | :--- | :--- | :--- | :--- |
| `model` | COMBO | 是 | `"wan2.7-i2v"` | 要使用的视频生成模型。 |
| `model.prompt` | STRING | 是 | - | 描述元素和视觉特征的提示词。支持英文和中文。（默认：空字符串） |
| `model.negative_prompt` | STRING | 是 | - | 描述需要避免内容的负面提示词。（默认：空字符串） |
| `model.resolution` | COMBO | 是 | `"720P"`<br>`"1080P"` | 输出视频的分辨率。 |
| `model.duration` | INT | 是 | 2 到 15 | 输出的总时长（秒）。模型将生成延续部分以填补输入片段之后的剩余时间。（默认：5） |
| `first_clip` | VIDEO | 是 | - | 要从中延续的输入视频。时长：2秒至10秒。输出视频的宽高比将由此视频决定。 |
| `last_frame` | IMAGE | 否 | - | 最后一帧图像。视频延续部分将向此帧过渡。 |
| `seed` | INT | 是 | 0 到 2147483647 | 用于生成的随机种子。（默认：0） |
| `prompt_extend` | BOOLEAN | 是 | - | 是否通过 AI 辅助增强提示词。（默认：True） |
| `watermark` | BOOLEAN | 是 | - | 是否在结果中添加 AI 生成的水印。（默认：False） |

**注意：** `first_clip` 输入视频的时长必须在 2 到 10 秒之间。

## 输出

| 输出名称 | 数据类型 | 描述 |
| :--- | :--- | :--- |
| `output` | VIDEO | 生成的视频延续片段。 |