# 加载图像数据集

此节点从所选文件夹加载图像数据集，并以列表形式返回。该文件夹必须是 ComfyUI 主输入目录内的子文件夹。支持的图像格式包括 PNG、JPG、JPEG 和 WEBP。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `folder` | 要从中加载图像的文件夹。可用选项为 ComfyUI 主输入目录中存在的子文件夹。解析到该目录之外的值（例如使用“..”）将被拒绝。 | COMBO | 是 | *多个可用选项* — ComfyUI 输入目录中存在的子文件夹 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `images` | 已加载图像的列表。该节点加载所选文件夹中找到的所有有效图像文件（PNG、JPG、JPEG、WEBP）并以列表形式返回。如果文件夹中不包含受支持的图像文件，则会引发错误。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/zh.md)

---
**Source fingerprint (SHA-256):** `cdee4e372890c126dd5f09654a7dd4103bba97a7901b6f5df8e02f29c4064ed2`
