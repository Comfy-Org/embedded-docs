> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolationModelLoader/zh.md)

## ## 概述

此节点从文件加载帧插值模型，并准备在工作流程中使用。它会自动检测模型类型（FILM 或 RIFE），并为您的硬件配置最佳性能。

## ## 输入

| 参数 | 数据类型 | 是否必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model_name` | STRING | 是 | `frame_interpolation` 文件夹中的模型文件列表 | 选择要加载的帧插值模型。模型必须放置在 `frame_interpolation` 文件夹中。 |

## ## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `FRAME_INTERPOLATION_MODEL` | MODEL | 已加载并配置好的帧插值模型，可直接在其他节点中使用。 |