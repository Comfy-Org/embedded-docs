此節點會將條件資料結構中的特定元素歸零，從而有效中和它們在後續處理步驟中的影響。它專為進階條件操作而設計，在這些操作中需要直接操控條件的內部表示。

## 輸入

| 參數 | 說明 | Comfy 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 要修改的條件資料結構。此節點會將每個條件條目中的 `pooled_output` 元素（如果存在）歸零。 | CONDITIONING |

## 輸出

| 參數 | 說明 | Comfy 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 修改後的條件資料結構，其中 `pooled_output` 元素已設定為零（如適用）。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningZeroOut/zh-TW.md)
