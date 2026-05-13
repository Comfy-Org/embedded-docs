> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxGuidance/zh-TW.md)

## 輸入

| 參數 | 資料類型 | 說明 |
|----------------|-----------|-------------|
| `conditioning` | CONDITIONING | 輸入的條件資料，通常來自先前的編碼或處理步驟 |
| `guidance` | FLOAT | 控制文字提示對影像生成的影響程度，可調整範圍為 0.0 至 100.0 |

## 輸出

| 參數 | 資料類型 | 說明 |
|----------------|-----------|-------------|
| CONDITIONING | CONDITIONING | 更新後的條件資料，包含新的引導值 |