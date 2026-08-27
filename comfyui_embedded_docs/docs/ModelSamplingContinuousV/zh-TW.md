# 模型取樣連續 V

ModelSamplingContinuousV 節點透過套用連續 V-prediction 取樣來調整模型的行為。它會建立輸入模型的複本，並為其設定自訂的最小與最大 sigma 值，以便對取樣過程進行更精細的控制。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要套用連續 V-prediction 取樣修改的輸入模型 | MODEL | 是 | - |
| `取樣` | 要套用的取樣方法；目前僅提供 V-prediction 選項（預設值：`"v_prediction"`） | COMBO | 是 | `"v_prediction"` |
| `最大 sigma` | 取樣的最大 sigma 值（進階參數，預設值：500.0） | FLOAT | 是 | 0.0 - 1000.0 |
| `最小 sigma` | 取樣的最小 sigma 值（進階參數，預設值：0.03） | FLOAT | 是 | 0.0 - 1000.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model` | 已套用連續 V-prediction 取樣的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8549be9dd2375374c20da7c74a756a90285716db0e52fed8a1a2b753cd6d75fe`
