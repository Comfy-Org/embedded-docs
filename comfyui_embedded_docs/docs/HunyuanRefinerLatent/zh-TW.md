# 混元精煉潛空間

HunyuanRefinerLatent 節點處理 conditioning 與 latent 輸入以進行細化操作。它會對正向與負向 conditioning 套用雜訊增強，同時納入 latent 影像資料，並產生一個具有特定維度的新 latent 輸出，以供後續處理。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 要處理的正向 conditioning 輸入 | CONDITIONING | 是 | - |
| `negative` | 要處理的負向 conditioning 輸入 | CONDITIONING | 是 | - |
| `latent` | latent 表示輸入 | LATENT | 是 | - |
| `noise_augmentation` | 要套用的雜訊增強量（預設值：0.10，步長：0.01，進階參數） | FLOAT | 是 | 0.0 - 1.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 已套用雜訊增強與 latent 影像串接的處理後正向 conditioning | CONDITIONING |
| `negative` | 已套用雜訊增強與 latent 影像串接的處理後負向 conditioning | CONDITIONING |
| `latent` | 與輸入 `latent` 具有相同批次大小及相同最後三個維度大小，但具有 32 個通道的新零填充 latent | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4c5669cf2ad5ba00e176876741b7d8d3f092cc58d2163871a10fd769ee4ff84c`
