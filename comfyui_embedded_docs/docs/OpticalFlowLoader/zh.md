> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/zh.md)

## ## 概述

从 `models/optical_flow/` 文件夹加载光流模型。目前仅支持 torchvision 的 RAFT-large 格式，这也是 VOIDWarpedNoise 节点所使用的模型。ComfyUI 不会自动下载光流权重文件，您需要手动将检查点文件放置在 `models/optical_flow/` 目录中。

## ## 输入

| 参数 | 数据类型 | 是否必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model_name` | STRING | 是 | `models/optical_flow/` 文件夹中的文件列表 | 要加载的光流模型。文件必须放置在 `optical_flow` 文件夹中。目前仅支持 torchvision 的 `raft_large.pth`。 |

## ## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `OPTICAL_FLOW` | MODEL | 已加载的光流模型，封装在 ModelPatcher 中，可供其他节点使用。 |