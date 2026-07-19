# 隨機重排影像-文字資料集

## 概述

此節點會將圖片列表與文字列表一起隨機打亂，同時保持它們原有的配對關係。它使用隨機種子來決定打亂順序，確保相同的輸入列表在使用相同種子時會以相同方式被打亂。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `images` | 要打亂的圖片列表。 | IMAGE | 是 | - |
| `texts` | 要打亂的文字列表。 | STRING | 是 | - |
| `seed` | 隨機種子。打亂順序由此值決定（預設值：0）。 | INT | 否 | 0 至 18446744073709551615 |

**注意：** `images` 和 `texts` 輸入必須是長度相同的列表。此節點會先將第一張圖片與第一個文字配對、第二張圖片與第二個文字配對，依此類推，然後再將這些配對一起打亂。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `images` | 打亂後的圖片列表。 | IMAGE |
| `texts` | 打亂後的文字列表，保持與圖片原有的配對關係。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleImageTextDataset/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c87cef780c98b1cf2a58a7d5faf4399c85edd647a9fdba693d008152e43d9c99`
