## 概述

Shuffle Dataset（資料集洗牌）節點會接收一組圖像清單，並隨機改變其排列順序。它使用種子值來控制隨機性，確保相同的洗牌順序可以重現。這在處理資料集前隨機化圖像序列時非常有用。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `images` | 需要進行洗牌的圖像清單。 | IMAGE | 是 | - |
| `seed` | 隨機種子。值為 0 時每次都會產生不同的洗牌結果。（預設值：0） | INT | 否 | 0 至 18446744073709551615 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `images` | 相同的圖像清單，但已重新隨機排序。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleDataset/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0b8442029995bdcedf1df0cb8d27d87aa529fb1021d911ed3016a6a7e788b246`
