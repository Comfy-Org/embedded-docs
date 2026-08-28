# WanMoveTracksFromCoords

WanMoveTracksFromCoords 節點從 JSON 格式的座標字串建立運動軌跡。它將座標資料轉換為可由其他影片處理節點使用的張量格式，並可選擇套用遮罩來控制軌跡隨時間的可見性。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `track_coords` | 包含軌跡座標資料的 JSON 格式字串。預設值為空清單（`"[]"`）。此輸入為強制輸入，因此必須在 UI 中連接。 | STRING | 否 | N/A |
| `track_mask` | 可選遮罩。提供時，節點使用它來決定每幀軌跡的可見性：在遮罩包含任何非零像素的幀中，軌跡可見。未提供時，所有軌跡在所有幀中都可見。 | MASK | 否 | N/A |

**注意：** `track_coords` 輸入需要特定的 JSON 結構。它應為軌跡清單，其中每個軌跡是一個幀清單，每個幀是一個具有 `x` 和 `y` 座標的物件。所有軌跡的幀數必須一致，且至少提供一個軌跡。

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `tracks` | 產生的軌跡資料，包含每個軌跡的路徑座標和可見性資訊。 | TRACKS |
| `track_length` | 產生軌跡中的總幀數。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTracksFromCoords/zh-TW.md)

---
**Source fingerprint (SHA-256):** `125187c96332fa81f0a30bcc4c927f405b56b578638ea565642a2b88dff808b7`
