# AlignYourStepsScheduler

AlignYourStepsScheduler 節點會根據不同的模型類型，為去雜訊流程產生 sigma 值（雜訊等級）。它會計算取樣流程每個步驟合適的雜訊等級，並根據 `denoise` 參數調整總步數，協助讓取樣步驟符合不同擴散模型的特定需求。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model_type` | 指定用於計算 sigma 的模型類型（預設值："SD1"） | COMBO | 是 | `"SD1"`<br>`"SDXL"`<br>`"SVD"` |
| `步驟數` | 要產生的取樣總步數（預設值：10） | INT | 是 | 1 至 10000 |
| `去雜訊強度` | 控制影像去雜訊的程度，其中 1.0 會使用所有步驟，較低的值則使用較少步驟（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 （步進值：0.01） |

注意：每種模型類型都有內建的雜訊等級排程，包含 11 個 sigma 值（對應 10 步）。當 `denoise` 為 0.0 時，節點會傳回空的 sigma 張量。當 `denoise` 介於 0.0 與 1.0 之間時，有效步數會以 `round(steps × denoise)` 計算，且只會使用 sigma 排程中對應的最後一部分。若要求的 `steps` 值與內建排程長度不符，雜訊等級會以對數線性插值方式調整，以符合要求的步數。最終 sigma 值一律設為 0。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `sigmas` | 傳回去雜訊流程所計算出的 sigma 值 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3adbe1016c1ff4b9b7ad3737f50b168f54444d4ca355488e60537d1136f85d3f`
