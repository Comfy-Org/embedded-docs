# 潜在空间拼接

LatentConcat 节点通过沿选定维度拼接两个潜在样本来将它们组合。它接收两个潜在输入，并沿 x、y 或 t 轴进行拼接，并可控制哪个样本排在前面。该节点在执行拼接前会自动调整第二个输入的批次大小，使其与第一个输入匹配。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `samples1` | 要拼接的第一个潜在样本 | LATENT | 是 | - |
| `samples2` | 要拼接的第二个潜在样本 | LATENT | 是 | - |
| `dim` | 拼接潜在样本所沿的维度。正值（x、y、t）在结果中将 `samples1` 放在 `samples2` 之前；负值（-x、-y、-t）将 `samples2` 放在 `samples1` 之前。维度映射关系为：x = 宽度，y = 高度，t = 时间/帧 | COMBO | 是 | `"x"`<br>`"-x"`<br>`"y"`<br>`"-y"`<br>`"t"`<br>`"-t"` |

**注意：** 在执行拼接前，第二个潜在样本（`samples2`）会自动调整批次大小，以与第一个潜在样本（`samples1`）匹配。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `output` | 沿指定维度组合两个输入样本后得到的拼接潜在样本 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentConcat/zh.md)

---
**Source fingerprint (SHA-256):** `dfe27f76ad12e16623d62c9e7f0b2772df6ecadb543a4eee430bc38ab04a12f2`
