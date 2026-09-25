# ByteDance Seedance 2.5 参考图转视频

ByteDance Seedance 2.5 Reference to Video 使用 ByteDance Seedance 模型（Seedance 2.5、2.5 Draft、2.0、2.0 Fast 和 2.0 Mini），在文本提示词以及可选参考图像、视频、音频或之前上传的库资源的引导下，生成、编辑或延长视频。它会上传参考素材、提交生成任务、等待完成并返回最终视频文件。选择 `Seedance 2.5 Draft` 则改为渲染快速的 480p 预览；将生成的 `draft_task_id` 连接到 ByteDance Seedance 2.5 Draft to Final Video 节点，即可渲染 1080p 最终视频。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 模型选择器。Seedance 2.5 用于最新模型，视频最长 30 秒，输出 mp4/mov；Seedance 2.5 Draft 用于快速 480p 预览，其 `draft_task_id` 输出可在 ByteDance Seedance 2.5 Draft to Final Video 节点中渲染 1080p 最终视频；Seedance 2.0 用于最高画质和 4k；Fast 用于速度优化；Mini 用于最快、成本最低的生成。选择模型会更改下方显示的输入控件。 | DYNAMIC_COMBO | 是 | "Seedance 2.5"<br>"Seedance 2.5 Draft"<br>"Seedance 2.0"<br>"Seedance 2.0 Fast"<br>"Seedance 2.0 Mini" |
| `种子` | 种子控制节点是否应重新运行；无论种子如何，结果都是非确定性的。默认值：0。 | INT | 是 | 0 到 2147483647 |
| `水印` | 是否向视频添加水印。默认值：False。高级设置。 | BOOLEAN | 是 | true<br>false |

### Seedance 2.5 输入

当 `model` 设置为 "Seedance 2.5" 时，会显示这些输入。

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用于视频生成的文本提示词。将台词放在双引号中可以引导生成的对话。默认值：空字符串。 | STRING | 是 | Multiline text |
| `resolution` | 输出视频的分辨率。默认值：720p。 | COMBO | 是 | "480p"<br>"720p"<br>"1080p" |
| `ratio` | 输出视频的宽高比。默认值：16:9。 | COMBO | 是 | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | 输出视频的时长（秒）（4-30）。默认值：5。 | INT | 是 | 4 到 30 |
| `generate_audio` | 为输出视频启用音频生成。默认值：True。 | BOOLEAN | 是 | true<br>false |
| `task_type` | 要对参考媒体执行的操作。除 auto 外，每个值都会在提交任务时进行验证，因此不匹配的设置会在生成开始前失败。<br>auto：模型根据提示词和输入推断任务，与其判断冲突的设置只会在生成开始后失败。<br>reference：在参考图像、视频和音频的引导下生成新视频。<br>edit：修改已连接的参考视频（添加、删除、替换）；输出会保留源片段的自身长度和宽高比，并且忽略 `duration` 和 `ratio` 控件。<br>extend：向前或向后延续已连接的参考视频；提示词应写明 "extend forward"、"extend backward" 或 "continue"，宽高比会跟随源片段，输出只包含你设置时长的新生成片段，不包含源片段。默认值：auto。 | COMBO | 是 | "auto"<br>"reference"<br>"edit"<br>"extend" |
| `output_format` | 输出视频的容器格式。默认值：mp4。 | COMBO | 是 | "mp4" |

### Seedance 2.5 Draft 输入

当 `model` 设置为 "Seedance 2.5 Draft" 时，会显示这些输入。参数集与上方 Seedance 2.5 相同，只是 `resolution` 仅提供 `"480p"`（默认 `"480p"`）。

### Seedance 2.0 输入

当 `model` 设置为 "Seedance 2.0" 时，会显示这些输入。

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用于视频生成的文本提示词。默认值：空字符串。 | STRING | 是 | Multiline text |
| `resolution` | 输出视频的分辨率。 | COMBO | 是 | "480p"<br>"720p"<br>"1080p"<br>"4k" |
| `ratio` | 输出视频的宽高比。默认值：adaptive。 | COMBO | 是 | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | 输出视频的时长（秒）（4-15）。默认值：7。 | INT | 是 | 4 到 15 |
| `generate_audio` | 为输出视频启用音频生成。默认值：True。 | BOOLEAN | 是 | true<br>false |

### Seedance 2.0 Fast 和 Seedance 2.0 Mini 输入

当 `model` 设置为 "Seedance 2.0 Fast" 或 "Seedance 2.0 Mini" 时，会显示这些输入。两个模型共享相同的输入集。

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用于视频生成的文本提示词。默认值：空字符串。 | STRING | 是 | Multiline text |
| `resolution` | 输出视频的分辨率。 | COMBO | 是 | "480p"<br>"720p" |
| `ratio` | 输出视频的宽高比。默认值：adaptive。 | COMBO | 是 | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | 输出视频的时长（秒）（4-15）。默认值：7。 | INT | 是 | 4 到 15 |
| `generate_audio` | 为输出视频启用音频生成。默认值：True。 | BOOLEAN | 是 | true<br>false |

### 参考输入

这些可增长的参考槽位适用于所有模型。每种模型的最大槽位数不同：Seedance 2.5 最多支持 30 张图像、10 个视频、10 段音频和 30 个资产；Seedance 2.0、2.0 Fast 和 2.0 Mini 最多支持 9 张图像、3 个视频、3 段音频和 9 个资产。

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | 可增长槽位：连接 1..N 张引导输出的参考图像。数量限制因模型而异（参见各模型章节）。图像会验证宽高比（0.4 到 2.5），并自动缩小到最长边 6000 像素。 | IMAGE | 否 | 1..9 slots (Seedance 2.0 family)<br>1..30 slots (Seedance 2.5) |
| `reference_videos` | 可增长槽位：连接 1..N 个参考视频。数量限制因模型而异（参见各模型章节）。每个视频必须至少 1.8 秒，并且必须符合所选模型和分辨率的像素限制。 | VIDEO | 否 | 1..3 slots (Seedance 2.0 family)<br>1..10 slots (Seedance 2.5) |
| `reference_audios` | 可增长槽位：连接 1..N 段参考音轨。数量限制因模型而异（参见各模型章节）。每段音频必须至少 1.8 秒。 | AUDIO | 否 | 1..3 slots (Seedance 2.0 family)<br>1..10 slots (Seedance 2.5) |
| `reference_assets` | 可增长槽位：连接 1..N 个资产 ID 字符串，这些资产是已上传到 Seedance 虚拟库的媒体。每个资产必须处于 Active 状态。你可以在提示词中使用诸如 `asset1` 或 `asset 1` 的标记来引用资产；节点会将其替换为资产的位置标签（例如 "Image 2" 或 "Video 1"）。 | STRING | 否 | 1..9 slots (Seedance 2.0 family)<br>1..30 slots (Seedance 2.5) |
| `auto_downscale` | 自动缩小超过所选分辨率下模型像素预算的参考视频。宽高比保持不变；已在限制内的视频不受影响。默认值：True。 | BOOLEAN | 否 | true<br>false |
| `auto_upscale` | 自动放大低于所选分辨率下模型最低像素数的参考视频。宽高比保持不变；已达到最低要求的视频不受影响。注意：放大低分辨率源不会增加真实细节，并可能产生质量较低的生成结果。默认值：False。高级设置。 | BOOLEAN | 否 | true<br>false |

**注意：** 运行节点至少需要一张参考图像、一个参考视频或一个资产（Seedance 2.5 也接受仅音频参考）。参考视频和音频各自必须至少 1.8 秒，并且所有参考视频的总时长（以及单独计算的所有参考音频总时长）不得超过所选模型的最大总秒数。参考图像的宽高比必须大约在 2:5 到 5:2 之间（0.4 到 2.5），至少为 300x300 像素，并会自动缩小到最长边 6000 像素。`task_type` 的 "edit" 和 "extend" 选项仅适用于 Seedance 2.5，且二者都要求至少一个参考视频；使用 "edit" 时，输出会保留源片段的自身长度和宽高比，并忽略 `duration` 和 `ratio` 控件；使用 "extend" 时，输出只包含按你设置时长新生成的片段。引用的资产必须处于 Active 状态，否则任务会失败。`draft_task_id` 输出仅由 `Seedance 2.5 Draft` 生成，因此使用任何其他模型时必须将其保持未连接，否则运行会失败。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `video` | 生成的视频，在生成任务完成后从提供商处下载。启用音频生成时，包含音频。 | VIDEO |
| `draft_task_id` | 草稿运行的任务 ID。只有 Seedance 2.5 Draft 模型会生成它；将其连接到 ByteDance Seedance 2.5 Draft to Final Video 节点，以渲染 1080p 最终视频。 | STRING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNodeV2/zh.md)

---
**Source fingerprint (SHA-256):** `12fee29b280ff71e29f268f52131d1c15cf3066e0804356b735b61d97c80a6a9`
