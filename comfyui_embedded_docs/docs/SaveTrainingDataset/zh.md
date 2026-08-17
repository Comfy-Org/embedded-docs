# 保存训练数据集

此节点将准备好的训练数据集保存到您的计算机硬盘上。它接收编码后的数据（包括图像潜变量及其对应的文本条件），并将其整理为多个更小的文件（称为分片/shards），以便管理。节点会在 `datasets` 目录中自动创建一个文件夹，并同时保存分片数据文件和一个描述数据集的 `metadata.json` 文件。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 取值范围 |
| --- | --- | --- | --- | --- |
| `latents` | 来自 MakeTrainingDataset 的潜变量字典列表。 | LATENT | 是 | N/A |
| `conditioning` | 来自 MakeTrainingDataset 的条件列表（conditioning lists）的列表。 | CONDITIONING | 是 | N/A |
| `folder_name` | 在 `datasets` 目录中用于保存数据集的文件夹名称。允许使用子文件夹，例如 'project/run1'。（默认值："training_dataset"） | STRING | 是 | N/A |
| `shard_size` | 每个分片文件中的样本数量。（默认值：1000） | INT | 是 | 1 到 100000 |

**注意：** `latents` 列表中的项目数量必须与 `conditioning` 列表中的项目数量完全匹配。如果数量不一致，节点会报错。`folder_name` 必须指定 `datasets` 目录下的一个子文件夹：`datasets` 根文件夹本身，以及任何越出该目录的路径（例如 `..` 或绝对路径）都会被拒绝。

## 输出

此节点不产生任何输出数据。它会将数据集保存为带编号的分片文件（例如 `shard_0000.pkl`）和一个 `metadata.json` 文件，存放于 `datasets` 目录中选定的文件夹内。

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/zh.md)

---
**Source fingerprint (SHA-256):** `6d7b63a24ac42907b0f4a1358712cd0ed085982ecd308bce87e5376d9bbc2274`
