# HiDream-O1 参考图像

## 概述

将参考图像附加到正向和负向条件上。此节点允许您提供一个或多个参考图像，这些图像将用于指导图像生成过程，可用于基于指令的编辑，也可用于主体驱动的个性化。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 要附加参考图像的正向条件。 | CONDITIONING | 是 | - |
| `negative` | 要附加参考图像的负向条件。 | CONDITIONING | 是 | - |
| `images` | 参考图像。1 张图像 = 指令编辑；2-10 张图像 = 多参考。 | IMAGE | 是 | 1 to 10 images |

**关于 `images` 参数的说明：** 这是一个自动扩展输入，可接受 1 到 10 张图像。图像标记为 `image_1` 到 `image_10`。您必须至少提供 1 张图像。图像数量决定了操作模式：单张图像用于编辑指令，而多张图像（2-10）用于主体驱动的个性化。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 已附加参考图像的正向条件。 | CONDITIONING |
| `negative` | 已附加参考图像的负向条件。 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1ReferenceImages/zh.md)

---
**Source fingerprint (SHA-256):** `f05f6be19df8b8697a98507163e8f60fd0cf2048c81f92597d2ae0a3395b8c6d`
