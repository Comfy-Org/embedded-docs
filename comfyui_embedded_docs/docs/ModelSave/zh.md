# 保存模型

ModelSave 节点将训练或修改后的模型保存到计算机存储中。它接收一个模型作为输入，并使用您指定的文件名前缀，将其写入输出文件夹中的 safetensors 检查点文件。工作流提示和元数据信息在可用时会嵌入到保存的文件中。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要保存到磁盘的模型 | MODEL | 是 | - |
| `filename_prefix` | 保存模型文件的文件名和路径前缀（默认值："diffusion_models/ComfyUI"）。保存时会在名称后附加计数器（例如 `ComfyUI_00000_.safetensors`）。 | STRING | 是 | - |
| `prompt` | 工作流提示信息（自动提供） | PROMPT | 否 | - |
| `extra_pnginfo` | 额外的工作流元数据（自动提供） | EXTRA_PNGINFO | 否 | - |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| *None* | 此节点不返回任何输出值 | - |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/zh.md)

---
**Source fingerprint (SHA-256):** `943e60f2c596d9cbcaabe95029fd9d443df5b61c6137736a8b1b81ab78f200ea`
