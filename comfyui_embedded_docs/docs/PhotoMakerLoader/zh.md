# PhotoMaker加载器

PhotoMakerLoader 节点用于从可用的模型文件中加载 PhotoMaker 模型。它读取指定的模型文件，并准备 PhotoMaker ID 编码器，以供基于身份的图像生成任务使用。此节点标记为实验性，仅用于测试目的。

## 输入

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `photomaker_model_name` | 要加载的 PhotoMaker 模型文件的名称。可用选项由 `photomaker` 文件夹中存在的模型文件决定。 | COMBO | 是 | Multiple options available |

注意：选定的模型文件必须存在于 `photomaker` 文件夹中。如果找不到指定文件，节点将引发错误。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `photomaker_model` | 已加载的 PhotoMaker 模型，包含 ID 编码器，可用于身份编码操作。 | PHOTOMAKER |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerLoader/zh.md)

---
**Source fingerprint (SHA-256):** `1b26630fadbdc144cd42ca7393f743b079ee7463deb9c8b31b628b5dc7432317`
