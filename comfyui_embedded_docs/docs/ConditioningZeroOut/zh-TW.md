> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningZeroOut/zh-TW.md)

此節點會將條件資料結構中的特定元素歸零，有效中和它們在後續處理步驟中的影響。它專為需要直接操作條件內部表示的高級條件操作而設計。

## 輸入參數

| 參數名稱 | Comfy 資料類型 | 描述 |
|----------|----------------|------|
| `CONDITIONING` | CONDITIONING | 將被修改的條件資料結構。此節點會將每個條件條目中的 'pooled_output' 元素（如果存在）歸零。 |

## 輸出參數

| 參數名稱 | Comfy 資料類型 | 描述 |
|----------|----------------|------|
| `CONDITIONING` | CONDITIONING | 修改後的條件資料結構，其中適用的 'pooled_output' 元素已被設為零。 |