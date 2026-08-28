# WanMoveConcatTrack

WanMoveConcatTrack 節點將兩組運動追蹤資料合併為單一更長的序列。其運作方式是沿著各自的維度，將輸入的軌跡路徑與可見性遮罩進行串接。如果僅提供一組追蹤輸入，則會直接將該資料原封不動地傳遞出去。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `tracks_1` | 要進行串接的第一組運動追蹤資料。 | TRACKS | 是 |  |
| `tracks_2` | 可選的第二組運動追蹤資料。如果未提供，`tracks_1` 會直接傳遞至輸出。 | TRACKS | 否 |  |

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `tracks` | 串接後的運動追蹤資料，包含來自輸入的合併 `track_path` 與 `track_visibility`。 | TRACKS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0507c42dce5d481fe5dc5aa1116c9df279f236419f548ea3eff5d824d0d22653`
