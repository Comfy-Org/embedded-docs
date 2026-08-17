# WanMoveConcatTrack

WanMoveConcatTrack 節點將兩組動作追蹤數據合併為單一且更長的序列。其運作方式是沿著各自維度連接輸入追蹤中的追蹤路徑與可見性遮罩。如果只提供一個追蹤輸入，則會直接傳遞該數據而不做變更。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `tracks_1` | 要串接的第一組動作追蹤數據。 | TRACKS | 是 |  |
| `tracks_2` | 可選的第二組動作追蹤數據。如果未提供，`tracks_1` 會直接傳遞到輸出。 | TRACKS | 否 |  |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `tracks` | 串接後的動作追蹤數據，包含來自輸入的合併 `track_path` 與 `track_visibility`。 | TRACKS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0507c42dce5d481fe5dc5aa1116c9df279f236419f548ea3eff5d824d0d22653`
