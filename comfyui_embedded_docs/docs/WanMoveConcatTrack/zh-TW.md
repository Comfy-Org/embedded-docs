## 概述

WanMoveConcatTrack 節點將兩組運動追蹤資料合併為一個更長的序列。其運作方式是沿著各自的維度連接輸入軌跡中的路徑與可見性遮罩。如果僅提供一組軌跡輸入，則會直接將該資料傳遞至輸出，不做任何變更。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `tracks_1` | 要進行串接的第一組運動追蹤資料。 | TRACKS | 是 |  |
| `tracks_2` | 可選的第二組運動追蹤資料。若未提供，`tracks_1` 將直接傳遞至輸出。 | TRACKS | 否 |  |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `tracks` | 串接後的運動追蹤資料，包含來自輸入的合併 `track_path` 與 `track_visibility`。 | TRACKS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d9b4c00291c6fa8e17bf54ecdcd16f7f6874159fe8cebebe66568dc2a744868f`
