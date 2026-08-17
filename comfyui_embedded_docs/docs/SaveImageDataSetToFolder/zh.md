# 保存图像数据集

此节点将图像列表以 PNG 文件格式保存到 ComfyUI 输出目录下的指定文件夹中。该节点已弃用：它与现有的 Save Image 节点功能重复，已被其取代，因为 Save Image 节点可以在文件名前缀中指定目标文件夹。该节点使用可自定义的文件名前缀将接收到的每张图像写入磁盘，并且可以选择覆盖现有文件或生成递增文件名以避免覆盖。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `images` | 要保存的图像列表。 | IMAGE | 是 | N/A |
| `folder_name` | 保存图像的文件夹名称（位于输出目录内）。默认值为 "dataset"。 | STRING | 否 | N/A |
| `filename_prefix` | 保存的图像文件名的前缀。默认值为 "image"。 | STRING | 否 | N/A |
| `mode` | 覆盖现有文件还是递增文件名以避免覆盖。默认值为 "overwrite"。 | COMBO | 否 | "overwrite"<br>"increment" |

**注意：** `images` 输入是一个列表，表示它可以一次接收并处理多张图像。所有输入都作为列表接收；对于 `folder_name`、`filename_prefix` 和 `mode`，仅使用所连接列表中的第一个值。`folder_name` 必须解析为 ComfyUI 输出目录内的文件夹——如果文件夹名称越出该目录（例如使用“..”、绝对路径或盘符），将被拒绝并报错。图像始终以 PNG 格式保存。`filename_prefix` 参数是一个高级选项。

## 输出

此节点没有任何数据输出。它是一个执行文件系统保存操作的输出节点。

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/zh.md)

---
**Source fingerprint (SHA-256):** `ee92340ca1581edcfe1cc1d5659ee705ad53425bed6658161a56e6d130680e50`
