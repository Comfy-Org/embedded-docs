> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlT2VNode/zh-TW.md)

Kling Text to Video Camera Control 節點可將文字轉換為具有專業攝影機運鏡效果的電影級影片，模擬真實世界的電影攝影技術。此節點支援控制虛擬攝影機動作，包括縮放、旋轉、平移、傾斜和第一人稱視角，同時保持對原始文字描述的專注。由於攝影機控制功能僅在專業模式下支援，使用 kling-v1-5 模型且影片長度固定為 5 秒，因此持續時間、模式和模型名稱均為硬編碼設定。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | - | 正向文字提示詞 |
| `負向提示詞` | STRING | 是 | - | 負向文字提示詞 |
| `cfg_scale` | FLOAT | 否 | 0.0-1.0 | 控制輸出結果與提示詞的貼合程度（預設值：0.75） |
| `aspect_ratio` | COMBO | 否 | "16:9"<br>"9:16"<br>"1:1"<br>"21:9"<br>"3:4"<br>"4:3" | 生成影片的長寬比（預設值："16:9"） |
| `camera_control` | CAMERA_CONTROL | 否 | - | 可透過 Kling Camera Controls 節點建立。用於控制影片生成過程中的攝影機移動和運動效果。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `video_id` | VIDEO | 帶有攝影機控制效果生成的影片 |
| `時長` | STRING | 生成影片的唯一識別碼 |
| `duration` | STRING | 生成影片的持續時間 |