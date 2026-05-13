> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/zh-TW.md)

HunyuanRefinerLatent 節點處理用於精煉操作的條件與潛在輸入。它對正向和負向條件進行噪聲增強，同時納入潛在影像資料，並生成具有特定維度的新潛在輸出以供後續處理。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 待處理的正向條件輸入 |
| `negative` | CONDITIONING | 是 | - | 待處理的負向條件輸入 |
| `latent` | LATENT | 是 | - | 潛在表示輸入 |
| `noise_augmentation` | FLOAT | 是 | 0.0 - 1.0 | 要應用的噪聲增強量（預設值：0.10） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 已處理的正向條件，包含應用的噪聲增強與潛在影像串接 |
| `negative` | CONDITIONING | 已處理的負向條件，包含應用的噪聲增強與潛在影像串接 |
| `latent` | LATENT | 維度為 [batch_size, 32, height, width, channels] 的新潛在輸出 |

---
**Source fingerprint (SHA-256):** `f097b58f1948e5c0801f81b51a5189619695a6afa189368aff4c64b126fc5ce5`
