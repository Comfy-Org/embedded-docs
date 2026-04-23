> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoReferenceNode/zh.md)

Grok Reference-to-Video 节点基于文本提示生成视频，最多可使用七张参考图像来引导输出视频的风格和内容。它通过连接外部 API 来创建视频，随后下载并返回该视频。

## 输入参数

| 参数 | 数据类型 | 必填 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | N/A | 期望视频的文本描述。 |
| `model` | COMBO | 是 | `"grok-imagine-video"` | 用于视频生成的模型。 |
| `model.reference_images` | IMAGE | 是 | 1 到 7 张图像 | 最多 7 张用于引导视频生成的参考图像。 |
| `model.resolution` | COMBO | 是 | `"480p"`<br>`"720p"` | 输出视频的分辨率。 |
| `model.aspect_ratio` | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` | 输出视频的宽高比。 |
| `model.duration` | INT | 是 | 2 到 10 | 输出视频的时长（单位：秒，默认值：6）。 |
| `seed` | INT | 否 | 0 到 2147483647 | 用于决定节点是否应重新运行的种子；无论种子值如何，实际结果都是非确定性的（默认值：0）。 |

**注意：** `model` 参数是一个包含 `reference_images`、`resolution`、`aspect_ratio` 和 `duration` 的组。您必须提供至少一张参考图像，最多可提供七张。

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `video` | VIDEO | 生成的视频文件。 |