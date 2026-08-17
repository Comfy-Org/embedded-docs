# LTXV 條件化

LTXVConditioning 節點會為影片生成模型的正向與負向 conditioning 輸入新增幀率資訊。它會接收既有的 conditioning 資料，並將指定的幀率值套用至兩組 conditioning 輸入，使其適用於影片模型的處理。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 將接收幀率資訊的正向 conditioning 輸入 | CONDITIONING | 是 | - |
| `negative` | 將接收幀率資訊的負向 conditioning 輸入 | CONDITIONING | 是 | - |
| `frame_rate` | 要套用至兩組 conditioning 輸入的幀率值（預設值：25.0） | FLOAT | 是 | 0.0 - 1000.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `positive` | 已套用幀率資訊的正向 conditioning | CONDITIONING |
| `negative` | 已套用幀率資訊的負向 conditioning | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c8546b691329f2934995f97a6db2e1393d2928bf1a7438fd079d52f87bee1c35`
