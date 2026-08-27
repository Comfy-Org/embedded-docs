# ByteDance2ReferenceNodeV2

ByteDance Seedance 2.5 Reference to Video 节点利用 ByteDance Seedance 模型（Seedance 2.5、2.0、2.0 Fast 和 2.0 Mini）来生成、编辑或扩展视频，通过文本提示以及可选的参考图像、视频、音频或先前上传的库资源进行引导。它会上传参考内容，提交生成任务，等待完成，然后返回最终视频文件。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 模型选择器。选择 Seedance 2.5 可使用最新模型，视频最长 30 秒且输出 mp4/mov；Seedance 2.0 用于最高质量和 4k；Fast 用于速度优化；Mini 用于最快、最低成本的生成。选择模型会更改下方显示的输入控件。 | DYNAMIC_COMBO | 是 | "Seedance 2.5"<br>"Seedance 2.0"<br>"Seedance 2.0 Fast"<br>"Seedance 2.0 Mini" |
| `seed` | 种子控制节点是否应重新运行；无论种子如何，结果都是非确定性的。默认值：0。 | INT | 是 | 0 to 2147483647 |
| `watermark` | 是否在视频中添加水印。默认值：False。高级设置。 | BOOLEAN | 是 | true<br>false |

### Seedance 2.5 输入

这些输入在 `model` 设置为 "Seedance 2.5" 时显示。

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用于视频生成的文本提示。将口语台词放在双引号中，以引导生成的对话。默认值：空字符串。 | STRING | 是 | Multiline text |
| `resolution` | 输出视频的分辨率。默认值：720p。 | COMBO | 是 | "480p"<br>"720p"<br>"1080p" |
| `ratio` | 输出视频的宽高比。默认值：16:9。 | COMBO | 是 | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | 输出视频的持续时间（秒）（4-30）。默认值：5。 | INT | 是 | 4 to 30 |
| `generate_audio` | 为输出视频启用音频生成。默认值：True。 | BOOLEAN | 是 | true<br>false |
| `task_type` | 如何处理参考媒体。除 auto 以外的每个值都会在提交任务时进行验证，因此不匹配的设置会在生成开始前失败。<br>auto：模型根据提示和输入推断任务，与其推断相冲突的设置仅在生成开始后失败。<br>reference：根据参考图像、视频和音频生成新视频。<br>edit：更改已连接的参考视频（添加、删除、替换）；输出保持源剪辑自身的长度和宽高比，`duration` 和 `ratio` 控件会被忽略。<br>extend：向前或向后延续已连接的参考视频；提示应包含 "extend forward"、"extend backward" 或 "continue"，宽高比遵循源剪辑，输出仅包含您设置的持续时间内新生成的片段，而不包含源剪辑。默认值：auto。 | COMBO | 是 | "auto"<br>"reference"<br>"edit"<br>"extend" |
| `output_format` | 输出视频的容器格式。默认值：mp4。 | COMBO | 是 | "mp4" |

### Seedance 2.0 输入

这些输入在 `model` 设置为 "Seedance 2.0" 时显示。

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用于视频生成的文本提示。默认值：空字符串。 | STRING | 是 | Multiline text |
| `resolution` | 输出视频的分辨率。 | COMBO | 是 | "480p"<br>"720p"<br>"1080p"<br>"4k" |
| `ratio` | 输出视频的宽高比。默认值：adaptive。 | COMBO | 是 | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | 输出视频的持续时间（秒）（4-15）。默认值：7。 | INT | 是 | 4 to 15 |
| `generate_audio` | 为输出视频启用音频生成。默认值：True。 | BOOLEAN | 是 | true<br>false |

### Seedance 2.0 Fast 和 Seedance 2.0 Mini 输入

这些输入在 `model` 设置为 "Seedance 2.0 Fast" 或 "Seedance 2.0 Mini" 时显示。两个模型共享相同的输入集。

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用于视频生成的文本提示。默认值：空字符串。 | STRING | 是 | Multiline text |
| `resolution` | 输出视频的分辨率。 | COMBO | 是 | "480p"<br>"720p" |
| `ratio` | 输出视频的宽高比。默认值：adaptive。 | COMBO | 是 | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | 输出视频的持续时间（秒）（4-15）。默认值：7。 | INT | 是 | 4 to 15 |
| `generate_audio` | 为输出视频启用音频生成。默认值：True。 | BOOLEAN | 是 | true<br>false |

### 参考输入

以下可扩展的参考槽位适用于所有模型。最大槽位数因模型而异：Seedance 2.5 最多支持 30 个图像、10 个视频、10 个音频和 30 个资源；Seedance 2.0、2.0 Fast 和 2.0 Mini 最多支持 9 个图像、3 个视频、3 个音频和 9 个资源。

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | 可扩展槽位：连接 1..N 个参考图像以引导输出。数量限制因模型而异（参见各模型部分）。图像会针对宽高比（0.4 至 2.5）进行验证，并自动缩小至最大边长为 6000 像素。 | IMAGE | 否 | 1..9 个槽位（Seedance 2.0 系列）<br>1..30 个槽位（Seedance 2.5） |
| `reference_videos` | 可扩展槽位：连接 1..N 个参考视频。数量限制因模型而异（参见各模型部分）。每个视频必须至少 1.8 秒长，并且必须符合所选模型和分辨率的像素限制。 | VIDEO | 否 | 1..3 个槽位（Seedance 2.0 系列）<br>1..10 个槽位（Seedance 2.5） |
| `reference_audios` | 可扩展槽位：连接 1..N 个参考音轨。数量限制因模型而异（参见各模型部分）。每个音频必须至少 1.8 秒长。 | AUDIO | 否 | 1..3 个槽位（Seedance 2.0 系列）<br>1..10 个槽位（Seedance 2.5） |
| `reference_assets` | 可扩展槽位：连接 1..N 个资源 ID 字符串，用于已上传到 Seedance 虚拟库的媒体。每个资源必须处于 Active 状态。您可以在提示中使用 `asset1` 或 `asset 1` 等令牌引用资源；节点会将其替换为资产的位置标签（例如 "Image 2" 或 "Video 1"）。 | STRING | 否 | 1..9 个槽位（Seedance 2.0 系列）<br>1..30 个槽位（Seedance 2.5） |
| `auto_downscale` | 自动将超出所选分辨率下模型像素预算的参考视频缩小。保持宽高比；已处于限制内的视频保持不变。默认值：True。 | BOOLEAN | 否 | true<br>false |
| `auto_upscale` | 自动将低于所选分辨率下模型最小像素数的参考视频放大。保持宽高比；已满足最小值的视频保持不变。注意：放大低分辨率源不会增加真实细节，并可能产生较低质量的生成结果。默认值：False。高级设置。 | BOOLEAN | 否 | true<br>false |

**注意：** 运行节点至少需要一个参考图像、视频或资源（Seedance 2.5 还接受仅音频参考）。参考视频和音频必须各至少 1.8 秒长，且所有参考视频的总时长（以及所有参考音频的总时长，分别计算）不得超过所选模型的最大总秒数。参考图像的宽高比必须介于约 2:5 和 5:2（0.4 至 2.5）之间，至少为 300x300 像素，并会自动缩小至最大边长为 6000 像素。`task_type` 的 "edit" 和 "extend" 选项仅在 Seedance 2.5 下可用，且两者都至少需要一个参考视频；使用 "edit" 时，输出保持源剪辑自身的长度和宽高比，`duration` 和 `ratio` 控件会被忽略；使用 "extend" 时，输出仅包含您设置的持续时间内新生成的片段。引用的资产必须处于 Active 状态，否则任务失败。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `video` | 生成的视频，在生成任务完成后从提供方下载。启用音频生成时包含音频。 | VIDEO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNodeV2/zh.md)

---
**Source fingerprint (SHA-256):** `3a6bba12e719204ba5dba9d7d5f2b4c5285ed68974ee015b6e4a7892a1cf0933`
