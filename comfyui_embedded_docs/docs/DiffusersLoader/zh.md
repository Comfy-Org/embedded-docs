# Diffusers加载器

DiffusersLoader 节点已弃用。它加载以 Hugging Face diffusers 格式保存的预训练模型，并返回 pipeline 所需的三个标准组件：MODEL、CLIP 和 VAE。该节点会自动扫描配置的 diffusers 文件夹，查找有效的模型目录（包含 `model_index.json` 文件的文件夹），并让你选择要加载的目录。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model_path` | 要加载的 diffusers 模型目录的路径。该节点会扫描配置的 diffusers 文件夹，并列出每个包含 `model_index.json` 文件的目录。 | COMBO | 是 | 自动从配置的 diffusers 文件夹中填充（所有包含 `model_index.json` 文件的子目录） |

注意：所选路径会根据已发现的模型列表进行验证。如果该路径不再存在于列表中，或无法找到模型目录，加载将失败并报错。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `MODEL` | 从 diffusers 格式加载的模型组件 | MODEL |
| `CLIP` | 从 diffusers 格式加载的 CLIP 文本编码模型组件 | CLIP |
| `VAE` | 从 diffusers 格式加载的 VAE（变分自编码器）组件 | VAE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/zh.md)

---
**Source fingerprint (SHA-256):** `75238342d05eac7528f981a2d4544accb6053891cd078a77751cc838054225d4`
