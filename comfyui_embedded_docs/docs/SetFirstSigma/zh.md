# 设置第一个Sigma

SetFirstSigma 节点通过将序列中的第一个 sigma 值替换为自定义值来修改 sigma 值序列。它接收现有的 sigma 序列和一个新的 sigma 值作为输入，然后返回一个新的 sigma 序列，其中仅第一个元素被更改，其余所有 sigma 值保持不变。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `sigmas` | 要修改的 sigma 值输入序列 | SIGMAS | 是 | - |
| `sigma` | 要设置为序列中第一个元素的新 sigma 值（默认：136.0） | FLOAT | 是 | 0.0 to 20000.0 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `sigmas` | 已修改的 sigma 序列，其中第一个元素已被替换为自定义 sigma 值 | SIGMAS |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetFirstSigma/zh.md)

---
**Source fingerprint (SHA-256):** `5302bc61a7ca094fee9ee2ad8c9dc32997ef0bbf27c9945acd7287e7df6b6db3`
