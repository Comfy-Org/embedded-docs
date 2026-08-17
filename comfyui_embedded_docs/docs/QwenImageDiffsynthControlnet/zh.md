# QwenImageDiffsynthControlnet

QwenImageDiffsynthControlnet 节点应用扩散合成控制网络补丁来修改基础模型的行为。它使用图像输入和可选掩码，以可调节的强度引导模型生成过程，创建一个融合了控制网络影响的补丁模型，从而实现更可控的图像合成。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要应用控制网络补丁的基础模型 | MODEL | 是 | - |
| `model_patch` | 要应用于基础模型的控制网络补丁模型 | MODEL_PATCH | 是 | - |
| `vae` | 扩散过程中使用的 VAE（变分自编码器） | VAE | 是 | - |
| `image` | 用于引导控制网络的输入图像（仅使用 RGB 通道） | IMAGE | 是 | - |
| `strength` | 控制网络影响的强度（默认值：1.0） | FLOAT | 是 | -10.0 到 10.0（步长：0.01） |
| `mask` | 可选掩码，用于定义控制网络应应用的区域（内部自动反转） | MASK | 否 | - |

**注意：** 当提供掩码时，系统会自动将其反转（1.0 - mask）并重新调整形状，以匹配控制网络处理所期望的尺寸。当模型补丁为 ZImage Control 类型时，补丁会同时应用于噪声精炼器和 double blocks；对于标准的 DiffSynth 控制网络，仅应用 double block 补丁。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 应用了扩散合成控制网络补丁的修改后模型 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageDiffsynthControlnet/zh.md)

---
**Source fingerprint (SHA-256):** `56739c098933cb70d3bcb8d6b251da33e7879b464b2e8a7296da085aefc15698`
