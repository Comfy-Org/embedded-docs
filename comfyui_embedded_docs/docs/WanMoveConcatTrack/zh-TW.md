> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/zh-TW.md)

WanMoveConcatTrack 節點將兩組運動追蹤資料合併為一個更長的序列。其運作方式是沿著各自的維度連接輸入追蹤資料的軌跡路徑和可見性遮罩。如果只提供一組追蹤輸入，它會直接將該資料原封不動地傳遞出去。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `tracks_1` | TRACKS | 是 | | 要進行串接的第一組運動追蹤資料。 |
| `tracks_2` | TRACKS | 否 | | 可選的第二組運動追蹤資料。如果未提供，則 `tracks_1` 將直接傳遞到輸出。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `tracks` | TRACKS | 串接後的運動追蹤資料，包含來自輸入的合併 `track_path` 和 `track_visibility`。 |
