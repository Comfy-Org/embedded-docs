> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/zh-TW.md)

此節點根據布林條件在兩個可能的輸入值之間進行選擇。當 `switch` 為 true 時，它輸出 `on_true` 輸入的值；當 `switch` 為 false 時，則輸出 `on_false` 輸入的值。此節點設計為惰性求值，意味著它僅根據開關狀態評估所需的輸入。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `switch` | BOOLEAN | 是 | | 決定傳遞哪個輸入的布林條件。為 true 時，選擇 `on_true` 輸入；為 false 時，選擇 `on_false` 輸入。 |
| `on_false` | MATCH_TYPE | 否 | | 當 `switch` 條件為 false 時要輸出的值。此輸入為可選，但 `on_false` 或 `on_true` 中至少必須連接一個。 |
| `on_true` | MATCH_TYPE | 否 | | 當 `switch` 條件為 true 時要輸出的值。此輸入為可選，但 `on_false` 或 `on_true` 中至少必須連接一個。 |

**注意：** `on_false` 和 `on_true` 輸入必須具有相同的資料類型，這由節點的內部模板定義。這兩個輸入中至少必須連接一個，節點才能正常運作。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | MATCH_TYPE | 被選中的值。其資料類型將與所連接的 `on_false` 或 `on_true` 輸入相匹配。 |
