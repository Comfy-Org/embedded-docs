# AlignYourStepsScheduler 節點

AlignYourStepsScheduler 節點根據不同的模型類型生成去噪過程的 sigma 值。它為取樣過程的每個步驟計算適當的噪聲級別，並根據去噪參數調整總步驟數。這有助於將取樣步驟與不同擴散模型的特定需求對齊。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model_type` | 指定用於 sigma 計算的模型類型（預設值："SD1"） | STRING | 是 | `"SD1"`<br>`"SDXL"`<br>`"SVD"` |
| `步驟數` | 要生成的總取樣步驟數（預設值：10） | INT | 是 | 1 到 10000 |
| `去雜訊強度` | 控制圖像的去噪程度，1.0 使用所有步驟，較低的值使用較少的步驟（預設值：1.0） | FLOAT | 是 | 0.0 到 1.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `sigmas` | 返回計算出的去噪過程 sigma 值 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/zh-TW.md)

---
**Source fingerprint (SHA-256):** `112535f9c100ca4e13dcd733e7a371c00c203b38d77bd10beb4355ba3512ec66`
