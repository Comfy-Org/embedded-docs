# SamplingPercentToSigma

SamplingPercentToSigma 節點使用模型的取樣參數，將取樣百分比值轉換為對應的 sigma 值。它接受介於 0.0 與 1.0 之間的百分比值，並將其映射至模型雜訊排程中的適當 sigma 值，且可選擇回傳計算出的 sigma 值，或在邊界處回傳實際的最大/最小 sigma 值。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 包含用於轉換之取樣參數的模型 | MODEL | 是 | - |
| `sampling_percent` | 要轉換為 sigma 的取樣百分比（預設值：0.0） | FLOAT | 是 | 0.0 至 1.0 (step: 0.0001) |
| `return_actual_sigma` | 回傳實際 sigma 值，而非用於區間檢查的值。這只會影響 0.0 與 1.0 的結果。（預設值：False） | BOOLEAN | 是 | - |

啟用 `return_actual_sigma` 時，`sampling_percent` 為 0.0 會回傳模型的最大 sigma 值（sigma_max），而 `sampling_percent` 為 1.0 會回傳最小 sigma 值（sigma_min）。至於其他所有百分比，無論是否啟用此選項，結果都相同。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `sigma 值` | 對應於輸入取樣百分比的轉換後 sigma 值 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplingPercentToSigma/zh-TW.md)

---
**Source fingerprint (SHA-256):** `30decf1d4804accbdf2a70eba1a773b41ef0e09cfb74f2a9388044dadf0a1ac1`
