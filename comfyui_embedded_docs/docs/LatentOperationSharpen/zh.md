> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/zh.md)

LatentOperationSharpen 节点使用高斯核对潜在表示应用锐化效果。其工作原理是对潜在数据进行归一化，使用自定义锐化核进行卷积，然后恢复原始亮度。这增强了潜在空间表示中的细节和边缘。

## 输入

| 参数 | 数据类型 | 是否必填 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `sharpen_radius` | INT | 否 | 1-31 | 锐化核的半径（默认值：9） |
| `sigma` | FLOAT | 否 | 0.1-10.0 | 高斯核的标准差（默认值：1.0） |
| `alpha` | FLOAT | 否 | 0.0-5.0 | 锐化强度因子（默认值：0.1） |

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `operation` | LATENT_OPERATION | 返回一个可应用于潜在数据的锐化操作 |

---
**Source fingerprint (SHA-256):** `542754746ab462eb27229ab9b949bb66054ab4c87c77cc59d405b35a2cc27bce`
