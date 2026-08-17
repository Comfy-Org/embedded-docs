# 加载背景移除模型

从文件中加载背景移除模型，并使其可供其他节点在从图像中移除背景时使用。模型文件从背景移除文件夹中的可用文件中选择。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `bg_removal_name` | 用于从图像中移除背景的模型。 | COMBO | 是 | 可用模型文件列表（background_removal 文件夹中的文件排序列表） |

**注意：** 如果所选文件不包含有效的背景移除模型，节点将引发错误。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `bg_model` | 已加载的背景移除模型，可供其他节点用于处理图像。 | BACKGROUND_REMOVAL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/zh.md)

---
**Source fingerprint (SHA-256):** `76f6536eae849a8b63f46f11c6afcf8c89774e4e89a5976e051253acc6108bcc`
