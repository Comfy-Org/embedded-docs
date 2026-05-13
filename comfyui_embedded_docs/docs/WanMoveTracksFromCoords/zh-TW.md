> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTracksFromCoords/zh-TW.md)

# WanMoveTracksFromCoords 節點

WanMoveTracksFromCoords 節點可從 JSON 格式的座標字串建立運動軌跡。它將座標資料轉換為張量格式，供其他影片處理節點使用，並可選擇性地套用遮罩來控制軌跡隨時間的可見度。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `track_coords` | STRING | 否 | N/A | 包含軌跡座標資料的 JSON 格式字串。預設值為空列表（`"[]"`）。 |
| `track_mask` | MASK | 否 | N/A | 可選的遮罩。當提供時，節點會使用它來決定每個軌跡在每一幀的可見度。 |

**注意：** `track_coords` 輸入需要特定的 JSON 結構。它應該是一個軌跡列表，其中每個軌跡是一個幀列表，而每個幀是一個包含 `x` 和 `y` 座標的物件。所有軌跡的幀數必須一致。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `tracks` | TRACKS | 生成的軌跡資料，包含每個軌跡的路徑座標和可見度資訊。 |
| `track_length` | INT | 生成的軌跡中的總幀數。 |

---
**Source fingerprint (SHA-256):** `106b05b3bdb5ede6e31216b9f3c14160630df0eee1f4e8a645c2b6cf9fbecf8c`
