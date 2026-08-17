# WanMoveTracksFromCoords

WanMoveTracksFromCoords 節點會從 JSON 格式的座標字串建立運動軌跡。它會將座標資料轉換為可供其他影片處理節點使用的張量格式，並可選擇性地套用遮罩，以控制軌跡隨時間變化的可見性。

## 輸入

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `track_coords` | 包含軌跡座標資料的 JSON 格式字串。預設值為空清單（`"[]"`）。 | STRING | 否 | N/A |
| `track_mask` | 選用遮罩。提供時，節點會用它來判斷每個影格中各軌跡的可見性。未提供時，所有軌跡在每個影格中皆視為可見。 | MASK | 否 | N/A |

**注意：** `track_coords` 輸入預期為特定的 JSON 結構。它應該是軌跡的清單，其中每個軌跡是影格的清單，而每個影格是包含 `x` 與 `y` 座標的物件。所有軌跡的影格數必須一致。

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
| --- | --- | --- |
| `tracks` | 產生的軌跡資料，包含每個軌跡的路徑座標與可見性資訊。 | TRACKS |
| `track_length` | 產生之軌跡的總影格數。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTracksFromCoords/zh-TW.md)

---
**Source fingerprint (SHA-256):** `125187c96332fa81f0a30bcc4c927f405b56b578638ea565642a2b88dff808b7`
