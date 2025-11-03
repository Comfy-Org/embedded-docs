> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage/zh-TW.md)

GeminiImage 節點能從 Google 的 Gemini AI 模型生成文字和圖片回應。它允許您提供包含文字提示、圖片和檔案的多模態輸入，以創建連貫的文字和圖片輸出。此節點負責與最新 Gemini 模型的所有 API 通訊和回應解析。

## 輸入參數

| 參數名稱 | 資料類型 | 輸入類型 | 預設值 | 數值範圍 | 描述 |
|-----------|-----------|------------|---------|-------|-------------|
| `prompt` | STRING | 必填 | "" | - | 用於生成內容的文字提示 |
| `model` | COMBO | 必填 | gemini_2_5_flash_image_preview | 可用的 Gemini 模型<br>選項從 GeminiImageModel 枚舉中提取 | 用於生成回應的 Gemini 模型。 |
| `seed` | INT | 必填 | 42 | 0 至 18446744073709551615 | 當種子固定為特定值時，模型會盡力為重複請求提供相同的回應。不保證輸出具有確定性。此外，即使使用相同的種子值，更改模型或參數設定（例如溫度）也可能導致回應發生變化。預設情況下，會使用隨機種子值。 |
| `images` | IMAGE | 選填 | None | - | 可選的圖片，用作模型的上下文。要包含多張圖片，您可以使用 Batch Images 節點。 |
| `files` | GEMINI_INPUT_FILES | 選填 | None | - | 可選的檔案，用作模型的上下文。接受來自 Gemini Generate Content Input Files 節點的輸入。 |

**注意：** 此節點包含由系統自動處理且無需使用者輸入的隱藏參數（`auth_token`、`comfy_api_key`、`unique_id`）。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | 從 Gemini 模型生成的圖片回應 |
| `STRING` | STRING | 從 Gemini 模型生成的文字回應 |