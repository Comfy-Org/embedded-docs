> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncTextToVideoNode/zh-TW.md)

Kling Lip Sync Text to Video 節點可將影片檔案中的嘴部動作與文字提示同步。它接收輸入影片並生成一個新影片，其中角色的唇部動作與提供的文字對齊。該節點使用語音合成技術來創建自然逼真的語音同步效果。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | 是 | - | 用於唇部同步的輸入影片檔案 |
| `text` | STRING | 是 | - | 用於唇語同步影片生成的文字內容。在模式為 text2video 時為必填項。最大長度為 120 個字元。 |
| `voice` | COMBO | 否 | "Melody"<br>"Bella"<br>"Aria"<br>"Ethan"<br>"Ryan"<br>"Dorothy"<br>"Nathan"<br>"Lily"<br>"Aaron"<br>"Emma"<br>"Grace"<br>"Henry"<br>"Isabella"<br>"James"<br>"Katherine"<br>"Liam"<br>"Mia"<br>"Noah"<br>"Olivia"<br>"Sophia" | 唇語同步音訊的語音選擇（預設值："Melody"） |
| `voice_speed` | FLOAT | 否 | 0.8-2.0 | 語速。有效範圍：0.8~2.0，精確到小數點後一位（預設值：1） |

**影片要求：**

- 影片檔案大小不應超過 100MB
- 高度/寬度應在 720px 至 1920px 之間
- 持續時間應在 2 秒至 10 秒之間

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 帶有唇語同步音訊的生成影片 |
| `video_id` | STRING | 生成影片的唯一識別碼 |
| `duration` | STRING | 生成影片的持續時間資訊 |