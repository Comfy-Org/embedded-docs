# SamplingPercentToSigma

SamplingPercentToSigma 節點使用模型的取樣參數，將取樣百分比值轉換為對應的 sigma 值。它接受介於 0.0 和 1.0 之間的百分比值，並將其映射到模型雜訊排程中適當的 sigma 值，同時可選擇在邊界處返回計算出的 sigma 值或實際的最大/最小 sigma 值。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 包含用於轉換之取樣參數的模型 | MODEL | 是 | - |
| `sampling_percent` | 要轉換為 sigma 的取樣百分比（預設值：0.0） | FLOAT | 是 | 0.0 至 1.0（步長：0.0001） |
| `return_actual_sigma` | 返回實際的 sigma 值，而非用於區間檢查的值。這僅影響在 0.0 和 1.0 時的結果（預設值：False） | BOOLEAN | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `sigma_value` | 對應於輸入取樣百分比的已轉換 sigma 值 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplingPercentToSigma/zh-TW.md)

---
**Source fingerprint (SHA-256):** `30decf1d4804accbdf2a70eba1a773b41ef0e09cfb74f2a9388044dadf0a1ac1`
