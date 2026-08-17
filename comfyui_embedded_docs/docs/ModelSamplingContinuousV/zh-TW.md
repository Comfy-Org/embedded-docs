# 模型取樣連續 V

ModelSamplingContinuousV 節點透過套用連續 V-prediction 取樣參數來修改模型的取樣行為。它會建立輸入模型的複本，並以自訂 sigma 範圍設定進行配置，以實現進階取樣控制。這讓使用者能夠使用特定的最小和最大 sigma 值來微調取樣過程。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要透過連續 V-prediction 取樣修改的輸入模型 | MODEL | 是 | - |
| `sampling` | 要套用的取樣方法。目前僅支援 V-prediction。 | COMBO | 是 | `"v_prediction"` |
| `sigma_max` | 取樣的最大 sigma 值（預設值：500.0） | FLOAT | 是 | 0.0 – 1000.0（步長 0.001） |
| `sigma_min` | 取樣的最小 sigma 值（預設值：0.03） | FLOAT | 是 | 0.0 – 1000.0（步長 0.001） |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用連續 V-prediction 取樣的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8549be9dd2375374c20da7c74a756a90285716db0e52fed8a1a2b753cd6d75fe`
