> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/zh-TW.md)

Kling 文字轉影片節點可將文字描述轉換為影片內容。它接收文字提示並根據指定的配置設定生成對應的影片序列。此節點支援不同的長寬比和生成模式，可產生不同時長和品質的影片。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | - | 正向文字提示（預設：無） |
| `negative_prompt` | STRING | 是 | - | 負向文字提示（預設：無） |
| `cfg_scale` | FLOAT | 否 | 0.0-1.0 | 配置縮放值（預設：1.0） |
| `aspect_ratio` | COMBO | 否 | 來自 KlingVideoGenAspectRatio 的選項 | 影片長寬比設定（預設："16:9"） |
| `mode` | COMBO | 否 | 多個可用選項 | 用於影片生成的配置，遵循格式：模式 / 時長 / 模型名稱（預設：modes[4]） |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片輸出 |
| `video_id` | STRING | 生成影片的唯一識別碼 |
| `duration` | STRING | 生成影片的時長資訊 |