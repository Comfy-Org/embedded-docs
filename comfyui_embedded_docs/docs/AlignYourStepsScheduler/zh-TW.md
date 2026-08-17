# AlignYourStepsScheduler

AlignYourStepsScheduler 節點會建立不同擴散模型類型在去噪過程中所使用的 sigma 值。它會為所選模型挑選基礎雜訊層級，根據 `denoise` 設定調整步驟數，並回傳一個結尾為 0 的 sigma 張量。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model_type` | 用於選擇基礎雜訊層級的模型類型（預設："SD1"） | COMBO | 是 | `"SD1"`<br>`"SDXL"`<br>`"SVD"` |
| `steps` | 要產生的取樣步驟總數（預設：10） | INT | 是 | 1 至 10000 |
| `denoise` | 控制取樣過程的使用量：1.0 使用所有步驟，較低的值使用較少步驟，0.0 會回傳空的 sigma 張量（預設：1.0） | FLOAT | 是 | 0.0 至 1.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `sigmas` | 去噪過程計算出的 sigma 值。若 `denoise` 為 0.0，則回傳空的張量。 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3adbe1016c1ff4b9b7ad3737f50b168f54444d4ca355488e60537d1136f85d3f`
