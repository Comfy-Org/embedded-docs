# ByteDance Seedance 2.0 参考生成视频

此节点使用字节跳动的 Seedance 2.5 或 2.0 AI 模型生成、编辑或扩展视频。您可以用文本提示词描述视频，并可添加参考图像、视频和音频来引导生成结果。它支持多模态参考输入、视频编辑和视频扩展。

## 输入
选择 `model` 将决定以下哪些参数可用。`video_editing` 和 `output_format` 仅在选择 Seedance 2.5 时出现。

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用于生成视频的 AI 模型。Seedance 2.5 是最新模型，支持最长 30 秒的视频和 mp4/mov 输出；Seedance 2.0 面向最高质量和 1080p/4k；Fast 用于速度优化；Mini 用于最快、成本最低的生成。选择模型后会显示下方列出的该模型专属输入。 | COMBO | 是 | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | 种子控制节点是否应重新运行；无论种子如何，结果都是非确定性的（默认值：0）。 | INT | 是 | 0 到 2147483647 |
| `watermark` | 是否在视频中添加水印（默认值：False）。 | BOOLEAN | 是 | `True`<br>`False` |
| `prompt` | 用于视频生成的文本提示词。对于 Seedance 2.5，将台词放在双引号中可引导生成的对话。必须包含至少一个非空白字符。 | STRING | 是 | Any text |
| `resolution` | 输出视频的分辨率。Seedance 2.5、2.0 Fast 和 2.0 Mini 提供 480p 和 720p；Seedance 2.0 还提供 1080p 和 4k（Seedance 2.5 默认：720p）。 | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | 输出视频的宽高比（Seedance 2.5 默认：`"16:9"`；Seedance 2.0 系列模型默认：`"adaptive"`）。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 输出视频的时长（秒）（Seedance 2.5：4-30，默认 5；Seedance 2.0 系列模型：4-15，默认 7）。 | INT | 是 | 4 到 30 (Seedance 2.5)<br>4 到 15 (Seedance 2.0)<br>Step: 1 |
| `generate_audio` | 为输出视频启用音频生成（默认值：True）。 | BOOLEAN | 是 | `True`<br>`False` |
| `video_editing` | 仅 Seedance 2.5。当提示词是对已连接的参考视频进行编辑时（例如替换其中的某个物体），请启用此选项。输出将保留源片段自身的长度和宽高比，时长和比例控件将被忽略。保持禁用可生成新视频，或将其扩展到您设置的时长（默认值：False）。 | BOOLEAN | 是 | `True`<br>`False` |
| `output_format` | 仅 Seedance 2.5。输出视频的容器格式（默认值：`"mp4"`）。 | COMBO | 是 | `"mp4"` |
| `reference_images` | 用于引导视频生成的参考图像。图像会自动缩小到最长边不超过 6000 像素，且必须至少为 300x300 像素，宽高比在 0.4 到 2.5 之间。 | IMAGE | 否 | Up 到 30 (Seedance 2.5)<br>Up 到 9 (Seedance 2.0) |
| `reference_videos` | 用于引导视频生成的参考视频；用于视频编辑和扩展。 | VIDEO | 否 | Up 到 10 (Seedance 2.5)<br>Up 到 3 (Seedance 2.0) |
| `reference_audios` | 用于引导视频生成的参考音频片段。 | AUDIO | 否 | Up 到 10 (Seedance 2.5)<br>Up 到 3 (Seedance 2.0) |
| `auto_downscale` | 自动将超过所选分辨率下模型像素预算的参考视频缩小。保持宽高比；已符合限制的视频不会被处理（默认值：True）。 | BOOLEAN | 否 | `True`<br>`False` |
| `auto_upscale` | 自动将低于所选分辨率下模型最低像素数的参考视频放大。保持宽高比；已满足最低要求的视频不会被处理。注意：放大低分辨率源不会增加真实细节，并可能产生较差的生成结果（默认值：False）。 | BOOLEAN | 否 | `True`<br>`False` |
| `reference_assets` | 先前创建的 Seedance 虚拟库资产（图像、视频或音频）的 ID，用作参考。每个资产必须存在且状态为 Active。在提示词中，资产可称为 asset1、asset 2 等；节点会将这些标记替换为类似 Image 2 的标签。 | STRING | 否 | Up 到 30 (Seedance 2.5)<br>Up 到 9 (Seedance 2.0) |

**重要约束：**

* 至少需要一个参考。对于 Seedance 2.0、2.0 Fast 和 2.0 Mini，您必须提供至少一个图像或视频参考（通过 `reference_images`、`reference_videos` 或图像/视频 `reference_assets` 条目）。Seedance 2.5 额外接受仅音频参考。
* 参考数量取决于模型：Seedance 2.5 允许最多 30 个 `reference_images`、10 个 `reference_videos`、10 个 `reference_audios` 和 30 个 `reference_assets`；Seedance 2.0 系列模型允许最多 9 个图像、3 个视频、3 个音频片段和 9 个资产。总计按直接输入和资产引用合并计算，并在生成前进行验证。
* 每个参考视频的时长必须至少为 1.8 秒，每个参考音频片段的时长也必须至少为 1.8 秒。所有参考视频的总时长以及所有参考音频的总时长必须保持在所选模型的限制内（Seedance 2.0 系列模型为 15.1 秒）。
* 参考视频还必须满足所选分辨率下模型的像素数限制。启用 `auto_downscale`（默认）后，超大的视频会自动调整大小；启用 `auto_upscale` 后，过小的视频会被放大。如果任一自动调整被禁用，超出相应限制的视频将引发错误。
* 在 Seedance 2.5 上启用 `video_editing` 时，`duration` 和 `ratio` 输入将被忽略；输出将与参考视频自身的长度和宽高比保持一致。

## 输出
| 输出名 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `video` | 生成的视频文件。 | VIDEO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/zh.md)

---
**Source fingerprint (SHA-256):** `4429306ac40b0f04ce7176cd805b34164de5e4e2b7204b008ea076b57663c200`
