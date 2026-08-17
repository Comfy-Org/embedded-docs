# ByteDance Seedance 2.0 参考生成视频

此节点使用字节跳动的 Seedance 2.5 或 2.0 AI 模型生成、编辑或扩展视频。您可以在文本提示中描述视频，并添加参考图像、视频和音频来引导结果。它支持多模态参考输入、视频编辑和视频扩展。这是字节跳动 Seedance 2.5 Reference to Video 节点的旧版、已弃用版本。

## 输入

选择 `model` 可确定以下哪些参数可用。仅当选择 Seedance 2.5 时，`video_editing` 和 `output_format` 才会出现。可增长的参考槽位和参考视频自动调整大小选项由所有模型共享，并在“参考输入”下进行说明。

### 通用输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用于生成视频的 AI 模型。Seedance 2.5 为最新模型，支持最长 30 秒的视频和 mp4/mov 输出；Seedance 2.0 提供最高质量和 1080p/4k；Fast 用于速度优化；Mini 用于最快、最低成本的生成。选择模型后会显示以下列出的模型特定输入。 | DYNAMIC_COMBO | 是 | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | `seed` 控制节点是否应重新运行；无论 `seed` 为何值，结果都是非确定性的（默认：0）。 | INT | 是 | 0 到 2147483647<br>步长：1 |
| `watermark` | 是否在视频中添加水印（默认：False）。 | BOOLEAN | 是 | `True`<br>`False` |

### Seedance 2.5 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用于视频生成的文本提示。将台词放在双引号中，以引导生成的对话。必须包含至少一个非空白字符（默认：空）。 | STRING | 是 | 任意文本 |
| `resolution` | 输出视频的分辨率（默认：`"720p"`）。 | COMBO | 是 | `"480p"`<br>`"720p"` |
| `ratio` | 输出视频的宽高比（默认：`"16:9"`）。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 输出视频的时长（秒）（默认：5）。 | INT | 是 | 4 到 30<br>步长：1 |
| `generate_audio` | 为输出视频启用音频生成（默认：True）。 | BOOLEAN | 是 | `True`<br>`False` |
| `video_editing` | 当提示修改已连接的参考视频时启用，例如替换其中的对象。随后输出将保持源剪辑自身的长度和宽高比，`duration` 和 `ratio` 控件将被忽略。保持禁用可生成新视频，或将视频扩展到您设置的时长（默认：False）。 | BOOLEAN | 是 | `True`<br>`False` |
| `output_format` | 输出视频的容器格式（默认：`"mp4"`）。 | COMBO | 是 | `"mp4"` |

### Seedance 2.0 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用于视频生成的文本提示。必须包含至少一个非空白字符（默认：空）。 | STRING | 是 | 任意文本 |
| `resolution` | 输出视频的分辨率。 | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | 输出视频的宽高比（默认：`"adaptive"`）。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 输出视频的时长（秒）（默认：7）。 | INT | 是 | 4 到 15<br>步长：1 |
| `generate_audio` | 为输出视频启用音频生成（默认：True）。 | BOOLEAN | 是 | `True`<br>`False` |

### Seedance 2.0 Fast 和 Seedance 2.0 Mini 输入

由 Seedance 2.0 Fast 和 Seedance 2.0 Mini 共享。这两个模型公开的输入集与 Seedance 2.0 相同，只是 `resolution` 仅限于 480p 和 720p。

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用于视频生成的文本提示。必须包含至少一个非空白字符（默认：空）。 | STRING | 是 | 任意文本 |
| `resolution` | 输出视频的分辨率。 | COMBO | 是 | `"480p"`<br>`"720p"` |
| `ratio` | 输出视频的宽高比（默认：`"adaptive"`）。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 输出视频的时长（秒）（默认：7）。 | INT | 是 | 4 到 15<br>步长：1 |
| `generate_audio` | 为输出视频启用音频生成（默认：True）。 | BOOLEAN | 是 | `True`<br>`False` |

### 参考输入

适用于所有模型。槽位最大数量取决于所选模型：Seedance 2.5 支持比 Seedance 2.0 模型更多的参考内容。

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | 可增长槽位：连接一个或多个参考图像（`image_1`、`image_2` ...）以引导视频生成。数量限制因模型而异（参见模型章节）。图像会自动缩小到最长边不超过 6000 像素，且必须至少为 300x300 像素，宽高比在 0.4 到 2.5 之间。 | IMAGE | 否 | 最多 30（Seedance 2.5）<br>最多 9（Seedance 2.0 模型） |
| `reference_videos` | 可增长槽位：连接一个或多个参考视频（`video_1`、`video_2` ...）以引导视频生成；用于视频编辑和扩展。 | VIDEO | 否 | 最多 10（Seedance 2.5）<br>最多 3（Seedance 2.0 模型） |
| `reference_audios` | 可增长槽位：连接一个或多个参考音频片段（`audio_1`、`audio_2` ...）以引导视频生成。 | AUDIO | 否 | 最多 10（Seedance 2.5）<br>最多 3（Seedance 2.0 模型） |
| `auto_downscale` | 自动缩小超过所选分辨率下模型像素预算的参考视频。保留宽高比；已在限制内的视频不受影响（默认：True）。 | BOOLEAN | 否 | `True`<br>`False` |
| `auto_upscale` | 自动放大低于所选分辨率下模型最小像素数的参考视频。保留宽高比；已满足最小值的视频不受影响。注意：放大低分辨率源不会增加真实细节，可能会生成质量较低的图像（默认：False）。 | BOOLEAN | 否 | `True`<br>`False` |
| `reference_assets` | 可增长槽位：先前创建的 Seedance 虚拟库资产（Image、Video 或 Audio）的 ID，用作参考（`asset_1`、`asset_2` ...）。每个资产必须存在且状态为 Active。在提示中，资产可称为 `asset1`、`asset 1` 等；节点会将这些标记替换为诸如“Image 2”之类的标签。 | STRING | 否 | 最多 30（Seedance 2.5）<br>最多 9（Seedance 2.0 模型） |

**重要约束：**

* 至少需要一个参考。对于 Seedance 2.0、2.0 Fast 和 2.0 Mini，您必须提供至少一个图像或视频参考（通过 `reference_images`、`reference_videos`，或 `reference_assets` 中的图像或视频条目）。Seedance 2.5 还接受纯音频参考（通过 `reference_audios` 或 `reference_assets` 中的音频条目）。
* 参考数量因模型而异，并且会结合直接输入和资产引用进行验证：Seedance 2.5 允许最多 30 个 `reference_images`、10 个 `reference_videos`、10 个 `reference_audios` 和 30 个 `reference_assets`；Seedance 2.0 模型允许最多 9 个图像、3 个视频、3 个音频片段和 9 个资产。
* 每个参考视频的长度必须至少为 1.8 秒，每个参考音频片段的长度也必须至少为 1.8 秒。所有参考视频和所有参考音频的总时长必须保持在所选模型的限制内（Seedance 2.0 模型为 15.1 秒）。
* 参考视频还必须满足所选分辨率下模型的像素数限制。启用 `auto_downscale`（默认）时，过大的视频会自动调整大小；启用 `auto_upscale` 时，过小的视频会被放大。如果任一自动调整被禁用，超出相应限制的视频将引发错误。
* 当在 Seedance 2.5 上启用 `video_editing` 时，`duration` 和 `ratio` 输入将被忽略；输出与参考视频自身的长度和宽高比一致。如果提供方将提示理解为编辑参考视频，则除非启用 `video_editing` 或重新措辞提示以描述新视频，否则生成将失败。
* 如果提供方拒绝为视频生成的音轨（例如可能存在版权匹配），任务将失败；禁用 `generate_audio` 将生成无声视频。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `video` | 生成的视频文件。 | VIDEO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/zh.md)

---
**Source fingerprint (SHA-256):** `4a1b62f65ff3515cdb749c9b3916e631e53523fe144e8cdf71ca020825196ae6`
