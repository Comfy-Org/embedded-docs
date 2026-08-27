# 模型取樣 AuraFlow

ModelSamplingAuraFlow 節點將專門的採樣配置應用於擴散模型，此配置特別針對 AuraFlow 模型架構設計。它透過應用 shift 值來調整採樣分佈，從而修改模型的採樣行為。此節點繼承自 SD3 模型採樣框架，並提供對採樣過程的精細控制。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用 AuraFlow 採樣配置的擴散模型 | MODEL | 是 | - |
| `偏移` | 要套用於採樣分佈的 shift 值（預設值：1.73，步長：0.01） | FLOAT | 是 | 0.0 - 100.0 |

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用 AuraFlow 採樣配置的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingAuraFlow/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7ca35632ae73517c78aa31a528492427c9af37862322ff7335f895c597ee1709`
