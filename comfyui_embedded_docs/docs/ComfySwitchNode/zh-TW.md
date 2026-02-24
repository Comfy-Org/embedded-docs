> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/zh-TW.md)

Switch 節點根據布林條件在兩個可能的輸入之間進行選擇。當 `switch` 啟用時，它輸出 `on_true` 輸入；當 `switch` 停用時，則輸出 `on_false` 輸入。這讓您可以在工作流程中建立條件邏輯並選擇不同的資料路徑。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `switch` | BOOLEAN | 是 | | 決定要傳遞哪個輸入的布林條件。當啟用（true）時，選擇 `on_true` 輸入。當停用（false）時，選擇 `on_false` 輸入。 |
| `on_false` | MATCH_TYPE | 否 | | 當 `switch` 停用（false）時要傳遞到輸出的資料。僅在 `switch` 為 false 時需要此輸入。 |
| `on_true` | MATCH_TYPE | 否 | | 當 `switch` 啟用（true）時要傳遞到輸出的資料。僅在 `switch` 為 true 時需要此輸入。 |

**關於輸入要求的注意事項：** `on_false` 和 `on_true` 輸入是條件性必填的。節點僅在 `switch` 為 true 時才會要求 `on_true` 輸入，僅在 `switch` 為 false 時才會要求 `on_false` 輸入。兩個輸入必須是相同的資料類型。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | MATCH_TYPE | 被選中的資料。如果 `switch` 為 true，這將是來自 `on_true` 輸入的值；如果 `switch` 為 false，則是來自 `on_false` 輸入的值。 |
