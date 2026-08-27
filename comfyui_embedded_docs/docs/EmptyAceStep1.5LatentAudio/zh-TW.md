# EmptyAceStep1.5LatentAudio

Empty Ace Step 1.5 Latent Audio 節點建立一個專為音訊處理設計的空潛在張量。它會產生指定持續時間和批次大小的靜音音訊潛在表示，可作為 ComfyUI 中音訊生成工作流程的起點。此節點根據輸入的秒數和固定取樣率計算潛在長度。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `seconds` | 要生成的音訊持續時間，以秒為單位（預設值：120.0）。 | FLOAT | 是 | 1.0 - 1000.0 |
| `batch_size` | 批次中的潛在圖像數量（預設值：1）。 | INT | 是 | 1 - 4096 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 一個表示靜音音訊的空潛在張量，帶有「audio」類型識別碼。輸出還包含一個 `downscale_ratio_temporal` 值，該值為 1764，用於音訊處理中的時間維度下取樣。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStep1.5LatentAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `bb7120c91ce5d779147cb8553d6f96fa160d87468d4d87550fb6dd4ec89b1557`
