# WanMoveTracksFromCoords

WanMoveTracksFromCoords 節點會從 JSON 格式的座標字串建立運動軌跡。它會將座標資料轉換為其他影片處理節點可使用的軌跡格式，並且可以選擇性套用遮罩，以控制軌跡隨時間變化的可見性。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `track_coords` | 包含軌跡座標資料的 JSON 格式字串。預設值為空列表（`"[]"`）。此輸入是強制輸入，因此必須在 UI 中連接。 | STRING | 否 | N/A |
| `track_mask` | 選用遮罩。提供時，節點會用它來判斷每一幀中軌跡的可見性：在遮罩包含任何非零像素的幀中，軌跡會可見。未提供時，所有軌跡在所有幀中皆可見。 | MASK | 否 | N/A |

**備註：** `track_coords` 輸入預期特定的 JSON 結構。它應該是一個軌跡列表，其中每個軌跡是幀的列表，而每個幀是具有 `x` 和 `y` 座標的物件。所有軌跡的幀數必須一致，且必須至少提供一個軌跡。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `tracks` | 產生的軌跡資料，包含每個軌跡的路徑座標與可見性資訊。 | TRACKS |
| `track_length` | 產生的軌跡中總幀數。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTracksFromCoords/zh-TW.md)

---
**Source fingerprint (SHA-256):** `125187c96332fa81f0a30bcc4c927f405b56b578638ea565642a2b88dff808b7`
