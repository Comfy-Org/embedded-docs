# 加载图像和文本数据集

此节点从指定文件夹加载由图像和文本描述组成的数据集，并将它们作为列表返回。支持的格式：PNG、JPG、JPEG、WEBP。对于每个图像文件，节点会自动查找具有相同基本名称的匹配 `.txt` 文件，并将其用作文本描述。该节点还支持一种文件夹结构，其中子文件夹名称以数字前缀开头（例如 `10_folder_name`），这会导致该子文件夹内的图像在输出中重复该次数。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `folder` | 要从中加载图像和文本描述的文件夹。可用选项为 ComfyUI 输入目录下的子目录。 | COMBO | 是 | *从 `folder_paths.get_input_subfolders()` 动态加载* |

**注意：** 该节点需要特定的文件结构。对于每个图像文件（`.png`、`.jpg`、`.jpeg`、`.webp`），它会查找同名的 `.txt` 文件作为其文本描述。如果未找到文本描述文件，则使用空字符串。该节点还支持一种特殊结构：子文件夹名称以数字和下划线开头（例如 `5_cats`），这将导致该子文件夹内的所有图像在最终输出列表中重复该次数。所选文件夹必须位于 ComfyUI 的输入目录内；解析到该目录之外的文件夹名称将被拒绝。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `images` | 已加载图像张量的列表。 | IMAGE |
| `texts` | 与每个已加载图像对应的文本描述列表。 | STRING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextDataSetFromFolder/zh.md)

---
**Source fingerprint (SHA-256):** `d34494d59a65edb38d7e6a5f12c241fb0093371db0b0bf1e52789e84209ad3f5`
