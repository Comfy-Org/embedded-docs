# 加载 LoRA 模型

The LoraModelLoader node applies trained LoRA (Low-Rank Adaptation) weights to a diffusion model. It modifies the base model by loading LoRA weights from a trained LoRA model and adjusting their influence strength. This allows you to customize the behavior of diffusion models without retraining them from scratch.

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 将应用 LoRA 的扩散模型。 | MODEL | 是 | - |
| `lora` | 要应用于扩散模型的 LoRA 模型。 | LORA_MODEL | 是 | - |
| `strength_model` | 修改扩散模型的强度。该值可以为负数（默认值：1.0）。 | FLOAT | 是 | -100.0 到 100.0 |
| `bypass` | 启用后，以旁路模式应用 LoRA，不修改基础模型权重。适用于训练以及模型权重已卸载的情况（默认值：False）。 | BOOLEAN | 是 | True 或 False |

**注意：** 当 `strength_model` 设置为 0 时，节点返回原始模型，不应用任何 LoRA 修改。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `model` | 修改后的扩散模型。 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraModelLoader/zh.md)

---
**Source fingerprint (SHA-256):** `81eb2a9b0376fe7453f6e7e422414472e80a3d1b92bb6874b91df6de8aed0d9a`
