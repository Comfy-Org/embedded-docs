# 获取 IC-LoRA 参数

## 概述

此节点从已加载 LoRA 模型的元数据中提取 IC-LoRA 参数。它读取 safetensors 元数据以查找参考下采样因子等值，并将其输出为结构化的参数对象，该对象可连接到 LTXVAddGuide 节点以进行特殊 guide 处理。如果元数据缺失或无法读取参考下采样因子，则该值默认为 1；找到后，该值会四舍五入并钳制为最小值 1。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 取值范围 |
| --- | --- | --- | --- | --- |
| `iclora_model` | 来自 LoRA Loader 的直接输出，用于指定要提取元数据的 IC-LoRA。 | MODEL | 是 | 不适用 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `iclora_parameters` | 从 LoRA 元数据中提取的 IC-LoRA 参数（例如 reference_downscale_factor）。如果该 LoRA 需要对 guides 进行特殊处理，则连接到 LTXVAddGuide。 | IC_LORA_PARAMETERS |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetICLoRAParameters/zh.md)

---
**Source fingerprint (SHA-256):** `5f6becad0c7673b8cde1e099bd7ba5be7106da958b8967f8e693ba2a704baaef`
