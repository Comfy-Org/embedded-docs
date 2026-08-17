# Latent应用操作

LatentApplyOperation 节点会对潜在样本应用指定操作。它接收潜在数据和操作作为输入，复制输入的潜在样本，对潜在张量应用该操作，并返回修改后的潜在数据。通过此节点，你可以转换或处理工作流中的潜在表示。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `samples` | 要由该操作处理的潜在样本 | LATENT | 是 | - |
| `operation` | 要应用于潜在样本的操作 | LATENT_OPERATION | 是 | - |

注意：此节点标记为实验性。该操作会应用于存储在潜在结构 `samples` 键下的潜在张量。输入潜在样本会在应用操作前被复制，因此原始输入潜在数据不会被修改。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `output` | 应用操作后修改的潜在样本 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperation/zh.md)

---
**Source fingerprint (SHA-256):** `cba55d019793fde8dcc0d4aeb4eb6020b6149f523c6bffc65d73c533aa2e2c6c`
