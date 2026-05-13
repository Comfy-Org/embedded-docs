> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraSave/zh.md)

# 概述

LoraSave 节点可从模型差异中提取并保存 LoRA（低秩适应）文件。它可以处理扩散模型差异、文本编码器差异或两者同时处理，将其转换为指定秩和类型的 LoRA 格式。生成的 LoRA 文件将保存到输出目录中供后续使用。

## 输入

| 参数 | 数据类型 | 必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `filename_prefix` | STRING | 是 | - | 输出文件名的前缀（默认值："loras/ComfyUI_extracted_lora"） |
| `rank` | INT | 是 | 1-4096 | LoRA 的秩值，控制大小和复杂度（默认值：8） |
| `lora_type` | COMBO | 是 | `"standard"`<br>`"locon"`<br>`"loha"`<br>`"lokr"`<br>`"dylora"` | 要创建的 LoRA 类型（默认值："standard"） |
| `bias_diff` | BOOLEAN | 是 | - | 是否在 LoRA 计算中包含偏置差异（默认值：True） |
| `model_diff` | MODEL | 否 | - | 要转换为 LoRA 的 ModelSubtract 输出 |
| `text_encoder_diff` | CLIP | 否 | - | 要转换为 LoRA 的 CLIPSubtract 输出 |

**注意：** 节点运行时，必须至少提供 `model_diff` 或 `text_encoder_diff` 中的一个。如果两者都省略，节点将不会产生任何输出。

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| - | - | 此节点将 LoRA 文件保存到输出目录，但不会通过工作流返回任何数据 |

---
**Source fingerprint (SHA-256):** `fdf020915ee233cf68250dcdcf87e7862d13ccc4fa73d8da8245727fdac46015`
