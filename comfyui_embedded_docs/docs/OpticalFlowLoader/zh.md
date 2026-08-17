# 加载光流模型

## 概述

从 `models/optical_flow/` 文件夹加载光流模型。目前仅支持 torchvision 的 RAFT-large 格式，即 VOIDWarpedNoise 节点所使用的模型。ComfyUI 不会自动下载光流权重；您必须手动将检查点文件放置在 `models/optical_flow/` 目录中。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model_name` | 要加载的光流模型。文件必须放置在 `optical_flow` 文件夹中。目前仅支持 torchvision 的 `raft_large.pth`。 | COMBO | 是 | `models/optical_flow/` 文件夹中的文件列表 |

所选文件必须是 torchvision RAFT-large 检查点。节点会检查文件是否包含预期的 RAFT 键（`feature_encoder.*`、`context_encoder.*` 和 `update_block.*`），如果格式无法识别，则会引发 ValueError。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `OPTICAL_FLOW` | 加载的光流模型，包装在 ModelPatcher 中以供其他节点使用。 | OPTICAL_FLOW |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/zh.md)

---
**Source fingerprint (SHA-256):** `5e79551545ad7ee2fd4856a47da29808a404342d1d5e57da0980058db6b11c3b`
