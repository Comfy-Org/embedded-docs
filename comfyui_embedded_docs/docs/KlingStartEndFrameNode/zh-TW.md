> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/zh-TW.md)

Kling 起始-結束影格轉影片節點會建立一個影片序列，在您提供的起始影像和結束影像之間進行過渡。它會生成中間的所有影格，以實現從第一幀到最後一幀的平滑轉換。此節點呼叫影像轉影片 API，但僅支援與 `image_tail` 請求欄位搭配使用的輸入選項。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `start_frame` | IMAGE | 是 | - | 參考影像 - URL 或 Base64 編碼字串，不得超過 10MB，解析度不低於 300*300px，長寬比需在 1:2.5 ~ 2.5:1 之間。Base64 不應包含 data:image 前綴。 |
| `end_frame` | IMAGE | 是 | - | 參考影像 - 結束影格控制。URL 或 Base64 編碼字串，不得超過 10MB，解析度不低於 300*300px。Base64 不應包含 data:image 前綴。 |
| `prompt` | STRING | 是 | - | 正向文字提示詞 |
| `負向提示詞` | STRING | 是 | - | 負向文字提示詞 |
| `cfg_scale` | FLOAT | 否 | 0.0-1.0 | 控制提示詞引導的強度（預設值：0.5） |
| `aspect_ratio` | COMBO | 否 | "16:9"<br>"9:16"<br>"1:1"<br>"21:9"<br>"9:21"<br>"3:4"<br>"4:3" | 生成影片的長寬比（預設值："16:9"） |
| `mode` | COMBO | 否 | 多個可用選項 | 用於影片生成的配置，遵循格式：模式 / 持續時間 / 模型名稱。（預設值：可用模式中的第三個選項） |

**影像限制：**

- `start_frame` 和 `end_frame` 都必須提供，且檔案大小不得超過 10MB
- 兩張影像的最小解析度：300×300 像素
- `start_frame` 的長寬比必須在 1:2.5 和 2.5:1 之間
- Base64 編碼的影像不應包含 "data:image" 前綴

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `video_id` | VIDEO | 生成的影片序列 |
| `時長` | STRING | 生成影片的唯一識別碼 |
| `duration` | STRING | 生成影片的持續時間 |