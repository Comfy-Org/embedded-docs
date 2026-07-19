# 混元精煉潛空間

HunyuanRefinerLatent 節點處理用於精煉操作的條件與潛在輸入。它對正向和負向條件進行噪聲增強，同時納入潛在影像資料，並生成具有特定維度的新潛在輸出以供後續處理。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向提示` | 待處理的正向條件輸入 | CONDITIONING | 是 | - |
| `負向提示` | 待處理的負向條件輸入 | CONDITIONING | 是 | - |
| `潛空間` | 潛在表示輸入 | LATENT | 是 | - |
| `雜訊增強` | 要應用的噪聲增強量（預設值：0.10） | FLOAT | 是 | 0.0 - 1.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `正向提示` | 已處理的正向條件，包含應用的噪聲增強與潛在影像串接 | CONDITIONING |
| `負向提示` | 已處理的負向條件，包含應用的噪聲增強與潛在影像串接 | CONDITIONING |
| `潛空間` | 維度為 [batch_size, 32, height, width, channels] 的新潛在輸出 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f097b58f1948e5c0801f81b51a5189619695a6afa189368aff4c64b126fc5ce5`
