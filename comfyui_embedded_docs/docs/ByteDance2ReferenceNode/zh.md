> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/zh.md)

该节点使用 Seedance 2.0 AI 模型，根据您的文本提示和提供的参考材料来创建、编辑或扩展视频。它可以使用图像、视频和音频作为参考来引导生成过程，支持视频编辑和扩展等任务。

## 输入参数

| 参数名 | 数据类型 | 必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` | 要使用的 AI 模型。Seedance 2.0 用于最高质量，而 Seedance 2.0 Fast 则针对速度进行了优化。选择模型后，会显示 `prompt`、`resolution`、`duration`、`ratio`、`generate_audio` 等额外必填输入，以及 `reference_images`、`reference_videos`、`reference_audios`、`reference_assets` 和 `auto_downscale` 等可选输入。 |
| `seed` | INT | 否 | 0 到 2147483647 | 用于控制节点是否应重新运行的数字。无论种子值如何，结果都是非确定性的（默认值：0）。 |
| `watermark` | BOOLEAN | 否 | `True` / `False` | 是否在生成的视频上添加水印（默认值：False）。 |

**重要限制：**
*   节点正常工作至少需要一个参考图像或视频（通过 `reference_images`、`reference_videos` 或 `reference_assets` 输入提供）。
*   每个参考视频的时长必须至少为 1.8 秒。所有参考视频的总时长不能超过 15.1 秒。
*   每个参考音频片段的时长必须至少为 1.8 秒。所有参考音频的总时长不能超过 15.1 秒。

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `video` | VIDEO | 生成的视频文件。 |