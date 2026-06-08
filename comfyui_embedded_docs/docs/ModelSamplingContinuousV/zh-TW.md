## 概述

ModelSamplingContinuousV 節點透過應用連續 V 預測取樣參數來修改模型的取樣行為。它會建立輸入模型的複本，並使用自訂的 sigma 範圍設定進行配置，以實現進階的取樣控制。這讓使用者能夠透過特定的最小和最大 sigma 值來微調取樣過程。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要使用連續 V 預測取樣進行修改的輸入模型 | MODEL | 是 | - |
| `取樣` | 要套用的取樣方法（目前僅支援 V 預測） | STRING | 是 | `"v_prediction"` |
| `最大 sigma` | 取樣的最大 sigma 值（預設值：500.0） | FLOAT | 是 | 0.0 - 1000.0 |
| `最小 sigma` | 取樣的最小 sigma 值（預設值：0.03） | FLOAT | 是 | 0.0 - 1000.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用連續 V 預測取樣的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8095b5024c0d33011f6a81ed496cf1711981701e0f35f9527646b150f5033d45`
