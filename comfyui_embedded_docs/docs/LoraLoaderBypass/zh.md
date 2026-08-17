# 加载LoRA（旁路）（用于调试）

LoraLoaderBypass 节点以特殊的旁路模式将 LoRA（低秩适应）应用于扩散模型和 CLIP 模型。与标准 LoRA 加载器不同，它不会永久修改基础模型权重。相反，它将该 LoRA 的效果添加到模型的正常前向传播中，这在训练或处理权重已卸载的模型时非常有用。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | LoRA 将应用到的扩散模型。 | MODEL | 是 | N/A |
| `clip` | LoRA 将应用到的 CLIP 模型。 | CLIP | 是 | N/A |
| `lora_name` | 要应用的 LoRA 文件名。选项从 `loras` 文件夹中加载。 | COMBO | 是 | 可用 LoRA 文件列表 |
| `strength_model` | 修改扩散模型的强度。此值可以为负（默认值：1.0）。 | FLOAT | 是 | -100.0 to 100.0 |
| `strength_clip` | 修改 CLIP 模型的强度。此值可以为负（默认值：1.0）。 | FLOAT | 是 | -100.0 to 100.0 |

**注意：** 如果 `strength_model` 和 `strength_clip` 均设置为 0，则节点将直接返回原始的、未经修改的 `model` 和 `clip` 输入，而不会进行任何处理。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `MODEL` | 在旁路模式下应用了 LoRA 的扩散模型。 | MODEL |
| `CLIP` | 在旁路模式下应用了 LoRA 的 CLIP 模型。 | CLIP |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/zh.md)

---
**Source fingerprint (SHA-256):** `025f0638a6690a53b1a6c4548dac24fb7e7f26e04ff4b1c88d29b061430037a8`
