# LTXV 條件化

LTXVConditioning 節點會將幀率資訊加入正向與負向的條件輸入，以供影片生成模型使用。它會取得現有的條件資料，並將指定的幀率值套用至兩組條件，使其適合用於影片模型處理。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向` | 會接收幀率資訊的正向條件輸入 | CONDITIONING | 是 | - |
| `負向` | 會接收幀率資訊的負向條件輸入 | CONDITIONING | 是 | - |
| `影格率` | 套用至兩組條件集的幀率數值（預設：25.0） | FLOAT | 是 | 0.0 - 1000.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `正向` | 已套用幀率資訊的正向條件 | CONDITIONING |
| `負向` | 已套用幀率資訊的負向條件 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c8546b691329f2934995f97a6db2e1393d2928bf1a7438fd079d52f87bee1c35`
