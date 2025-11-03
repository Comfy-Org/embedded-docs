> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoExtendNode/zh-TW.md)

Kling Video Extend 節點允許您擴展由其他 Kling 節點建立的影片。它會根據現有的影片 ID 識別影片，並根據您的文字提示產生額外內容。此節點透過將您的擴展請求發送到 Kling API 來運作，並返回擴展後的影片及其新的 ID 和持續時間。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 否 | - | 用於引導影片擴展的正面文字提示 |
| `negative_prompt` | STRING | 否 | - | 用於避免在擴展影片中出現特定元素的負面文字提示 |
| `cfg_scale` | FLOAT | 否 | 0.0 - 1.0 | 控制提示引導的強度（預設值：0.5） |
| `video_id` | STRING | 是 | - | 要擴展的影片 ID。支援由文字轉影片、圖片轉影片以及先前影片擴展操作產生的影片。擴展後總持續時間不能超過 3 分鐘。 |

**注意：** `video_id` 必須引用由其他 Kling 節點建立的影片，且擴展後的總持續時間不能超過 3 分鐘。

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 由 Kling API 產生的擴展影片 |
| `video_id` | STRING | 擴展影片的唯一識別碼 |
| `duration` | STRING | 擴展影片的持續時間 |