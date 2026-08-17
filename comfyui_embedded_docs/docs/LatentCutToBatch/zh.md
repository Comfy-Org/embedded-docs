# Latent切割

LatentCutToBatch 节点会沿所选维度将潜在表示切割成多个切片，并将它们堆叠成一个新的批次。这样，您可以独立处理潜在样本的不同部分。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `samples` | 要分割并批处理的潜在表示。 | LATENT | 是 | - |
| `dim` | 切割潜在样本所沿的维度。`"t"` 指时间维度，`"x"` 指宽度，`"y"` 指高度。 | COMBO | 是 | `"t"`<br>`"x"`<br>`"y"` |
| `slice_size` | 从指定维度切割的每个切片的大小。如果该维度的大小不能被此值整除，则丢弃余数。（默认值：1） | INT | 是 | 1 to 16384 (max resolution) |

注意：如果所选维度是批次或通道轴，则输入将原样返回。如果 `slice_size` 大于该维度的大小，则整个维度将作为单个切片使用。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `samples` | 生成的潜在批次，包含切割并堆叠后的样本。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCutToBatch/zh.md)

---
**Source fingerprint (SHA-256):** `873c9bc8391971887f1ab636c086cab86f5504a9c653bc80b54120ee53980bdf`
