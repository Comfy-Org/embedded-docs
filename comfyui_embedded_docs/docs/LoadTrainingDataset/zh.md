# 加载训练数据集

此节点从磁盘加载经过编码的训练数据集（latents 和 conditioning），用于训练。选择先前保存的数据集文件夹后，它会读取其中的所有分片文件，并返回合并后的潜在向量和 conditioning 数据。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `folder_name` | 要加载的已保存数据集，来自数据集目录。 | COMBO | 是 | 动态填充注册数据集目录中找到的所有数据集文件夹。仅列出包含 `metadata.json` 文件或 `.safetensors` 文件的文件夹。 |

**注意：** 所选数据集文件夹必须是已注册数据集目录的子文件夹，并且必须包含至少一个名为 `shard_*.pkl` 的分片文件；否则节点将抛出错误。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `latents` | 从数据集分片加载的潜在字典列表，每个字典包含一个 `samples` 张量。 | LATENT |
| `conditioning` | 从数据集分片加载的 conditioning 列表的列表，每个样本对应一个。 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadTrainingDataset/zh.md)

---
**Source fingerprint (SHA-256):** `9f914b27f067460f6f3b54f3f2a7bb793c65b99c85e8aa14ab64894be26bd816`
