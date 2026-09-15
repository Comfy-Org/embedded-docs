# WanMoveConcatTrack

WanMoveConcatTrack 節點會將兩組運動追蹤資料合併成單一且更長的序列。其運作方式是沿著各自維度，將輸入軌跡中的軌跡路徑與可見性遮罩連接起來。若僅提供一個軌跡輸入，則會原樣傳遞該資料。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `tracks_1` | 第一組要串接的運動追蹤資料。 | TRACKS | 是 |  |
| `tracks_2` | 可選的第二組運動追蹤資料。若未提供，`tracks_1` 會直接傳遞至輸出。 | TRACKS | 否 |  |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `tracks` | 串接後的運動追蹤資料，包含來自輸入的合併 `track_path` 與 `track_visibility`。當 `tracks_2` 未連接時，會原樣傳回 `tracks_1`。 | TRACKS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0507c42dce5d481fe5dc5aa1116c9df279f236419f548ea3eff5d824d0d22653`
