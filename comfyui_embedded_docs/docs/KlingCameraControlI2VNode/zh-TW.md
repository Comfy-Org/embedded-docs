> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlI2VNode/zh-TW.md)

{heading_overview}

Kling 圖像轉影片攝影機控制節點可將靜態圖像轉換為具有專業攝影機運鏡效果的電影級影片。此專用的圖像轉影片節點讓您能夠控制虛擬攝影機動作，包括縮放、旋轉、平移、傾斜和第一人稱視角，同時保持對原始圖像的聚焦。攝影機控制目前僅在專業模式下支援，使用 kling-v1-5 模型，影片長度為 5 秒。

{heading_inputs}

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `start_frame` | IMAGE | 是 | - | 參考圖像 - URL 或 Base64 編碼字串，不能超過 10MB，解析度不低於 300*300px，長寬比介於 1:2.5 ~ 2.5:1 之間。Base64 不應包含 data:image 前綴。 |
| `prompt` | STRING | 是 | - | 正面文字提示 |
| `negative_prompt` | STRING | 是 | - | 負面文字提示 |
| `cfg_scale` | FLOAT | 否 | 0.0-1.0 | 控制文字引導的強度（預設值：0.75） |
| `aspect_ratio` | COMBO | 否 | 多個選項可用 | 影片長寬比選擇（預設值：16:9） |
| `camera_control` | CAMERA_CONTROL | 是 | - | 可使用 Kling 攝影機控制節點建立。控制影片生成過程中的攝影機移動和運動。 |

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片輸出 |
| `video_id` | STRING | 生成影片的唯一識別碼 |
| `duration` | STRING | 生成影片的時長 |