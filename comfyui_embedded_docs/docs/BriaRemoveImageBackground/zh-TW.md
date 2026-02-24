> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/zh-TW.md)

此節點使用 Bria RMBG 2.0 服務移除圖像背景。它會將圖像發送到外部 API 進行處理，並返回移除背景後的結果。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 將要移除背景的輸入圖像。 |
| `moderation` | COMBO | 否 | `"false"`<br>`"true"` | 內容審核設定。設定為 `"true"` 時，將啟用額外的審核選項。 |
| `visual_input_moderation` | BOOLEAN | 否 | - | 對輸入圖像啟用視覺內容審核。此參數僅在 `moderation` 設定為 `"true"` 時可用。預設值：`False`。 |
| `visual_output_moderation` | BOOLEAN | 否 | - | 對輸出圖像啟用視覺內容審核。此參數僅在 `moderation` 設定為 `"true"` 時可用。預設值：`True`。 |
| `seed` | INT | 否 | 0 至 2147483647 | 控制節點是否應重新執行的種子值。無論種子值為何，結果都是非確定性的。預設值：`0`。 |

**注意：** `visual_input_moderation` 和 `visual_output_moderation` 參數依賴於 `moderation` 參數。它們僅在 `moderation` 設定為 `"true"` 時才處於啟用狀態且為必需。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `image` | IMAGE | 經過處理、背景已被移除的圖像。 |
