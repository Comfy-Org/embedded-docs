> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/zh-TW.md)

Kling Image to Video 節點使用文字提示從起始影像生成影片內容。它接收參考影像並根據提供的正向和負向文字描述創建影片序列，提供多種配置選項用於模型選擇、持續時間和長寬比。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `start_frame` | IMAGE | 是 | - | 用於生成影片的參考影像。 |
| `prompt` | STRING | 是 | - | 正向文字提示。 |
| `negative_prompt` | STRING | 是 | - | 負向文字提示。 |
| `model_name` | COMBO | 是 | 多個選項可用 | 影片生成的模型選擇（預設："kling-v2-master"）。 |
| `cfg_scale` | FLOAT | 是 | 0.0-1.0 | 配置縮放參數（預設：0.8）。 |
| `mode` | COMBO | 是 | 多個選項可用 | 影片生成模式選擇（預設：std）。 |
| `aspect_ratio` | COMBO | 是 | 多個選項可用 | 生成影片的長寬比（預設：field_16_9）。 |
| `duration` | COMBO | 是 | 多個選項可用 | 生成影片的持續時間（預設：field_5）。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片輸出。 |
| `video_id` | STRING | 生成影片的唯一識別碼。 |
| `duration` | STRING | 生成影片的持續時間資訊。 |