# 混元精煉潛空間

HunyuanRefinerLatent 節點為 Hunyuan 視頻精煉流程準備 conditioning 和 latent 資料。它將輸入的 latent 圖像資料附加到正向和負向 conditioning，對其套用雜訊增強值，並建立一個新的、以零填充且具有 32 個通道的 latent，以供後續處理。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向提示` | 要處理的正向條件輸入 | CONDITIONING | 是 | - |
| `負向提示` | 要處理的負向條件輸入 | CONDITIONING | 是 | - |
| `潛空間` | 潛在表示輸入，用作條件的潛在圖像資料，並用於定義輸出潛在的維度 | LATENT | 是 | - |
| `雜訊增強` | 要套用的雜訊增強量（預設值：0.10）。此參數顯示在節點的進階區段中。 | FLOAT | 是 | 0.0 - 1.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `正向提示` | 已處理的正向條件，附加了潛在圖像資料並套用了雜訊增強 | CONDITIONING |
| `負向提示` | 已處理的負向條件，附加了潛在圖像資料並套用了雜訊增強 | CONDITIONING |
| `潛空間` | 一個以零填充的新潛在，批次大小與輸入潛在相同，最後三個維度也相同，並具有 32 個通道 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4c5669cf2ad5ba00e176876741b7d8d3f092cc58d2163871a10fd769ee4ff84c`
