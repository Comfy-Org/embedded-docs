# 加载模型补丁

ModelPatchLoader 节点从 model_patches 文件夹加载专门的模型补丁。它自动检测补丁文件的类型并加载相应的模型架构，然后将其包装在 ModelPatcher 中，以便在工作流中使用。该节点支持不同的补丁类型，包括 controlnet 块、特征嵌入器模型以及其他专门架构。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `name` | 要从 model_patches 目录加载的模型补丁文件名 | STRING | 是 | model_patches 文件夹中所有可用的模型补丁文件 |

注意：此节点在 ComfyUI 中标记为实验性。补丁类型会根据文件内容自动检测，因此单个节点可以处理多种补丁。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| MODEL_PATCH | 加载的模型补丁包装在 ModelPatcher 中，供工作流使用 | MODEL_PATCH |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/zh.md)

---
**Source fingerprint (SHA-256):** `7f5225521b82b39b85183ccc7957fc4172e64aed9289f66d53969ea4a2e81b7f`
