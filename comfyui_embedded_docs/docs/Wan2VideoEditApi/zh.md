> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoEditApi/zh.md)

Wan2VideoEditApi 节点使用 Wan 2.7 模型，根据文本指令、参考图像或风格迁移来编辑视频。它处理输入视频，并根据指定的分辨率、时长和宽高比等参数生成新视频。

## 输入参数

| 参数 | 数据类型 | 必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `"wan2.7-videoedit"` | 用于视频编辑的模型。 |
| `model.prompt` | STRING | 是 | - | 编辑指令或风格迁移要求。（默认值：空字符串） |
| `model.resolution` | COMBO | 是 | `"720P"`<br>`"1080P"` | 输出视频的分辨率。 |
| `model.ratio` | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` | 输出视频的宽高比。如果未更改，则近似于输入视频的宽高比。 |
| `model.duration` | COMBO | 是 | `"auto"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` | 输出视频的时长（秒）。'auto' 表示与输入视频时长一致。指定具体数值将从视频开头截取相应时长。（默认值："auto"） |
| `model.reference_images` | IMAGE | 否 | - | 用于指导编辑的参考图像列表，最多 4 张。 |
| `video` | VIDEO | 是 | - | 待编辑的视频。 |
| `seed` | INT | 否 | 0 到 2147483647 | 用于生成的随机种子。（默认值：0） |
| `audio_setting` | COMBO | 否 | `"auto"`<br>`"origin"` | 'auto'：模型根据提示词决定是否重新生成音频。'origin'：保留输入视频的原始音频。（默认值："auto"） |
| `watermark` | BOOLEAN | 否 | - | 是否在结果中添加 AI 生成的水印。（默认值：False） |

**约束条件：**
*   `model.prompt` 的长度必须至少为 1 个字符。
*   输入的 `video` 时长必须在 2 到 10 秒之间。
*   `model.reference_images` 输入最多可接受 4 张图像。

## 输出结果

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 由模型生成的编辑后的视频。 |