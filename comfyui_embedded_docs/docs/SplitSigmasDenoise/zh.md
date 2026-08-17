# 分离Sigma降噪

SplitSigmasDenoise 节点根据去噪强度参数将 sigma 值序列分成两部分。它将输入的 `sigmas` 拆分为高 sigma 序列和低 sigma 序列，拆分点由总步数乘以 denoise 因子确定。这样可以将噪声调度分离到不同强度范围，以便进行专门处理。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `sigmas` | 表示噪声调度的 sigma 值输入序列 | SIGMAS | 是 | - |
| `denoise` | 决定 sigma 序列拆分位置的去噪强度因子（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |

注意：总步数为 sigma 值数量减 1。两个输出序列在拆分点共用一个 sigma 值。当 `denoise` = 0.0 时，`high_sigmas` 为空；当 `denoise` = 1.0 时，`high_sigmas` 仅包含第一个 sigma 值，而 `low_sigmas` 包含完整序列。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `high_sigmas` | sigma 序列的第一部分，包含较高的 sigma 值 | SIGMAS |
| `low_sigmas` | sigma 序列的第二部分，包含较低的 sigma 值 | SIGMAS |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmasDenoise/zh.md)

---
**Source fingerprint (SHA-256):** `6198cdbc07b5c9aacf1137a5d6350e090ffd14050abbcc37ff79ff5e975a8c20`
