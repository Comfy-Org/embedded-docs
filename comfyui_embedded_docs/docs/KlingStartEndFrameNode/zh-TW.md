# Kling 起始-結束影格轉影片

此節點會建立一段在你的起始圖片與結束圖片之間轉場的影片序列。它會生成介於第一幀與最後一幀之間的所有影格，以產生流暢的轉換效果。此節點呼叫圖片轉影片 API，但僅支援可與 `image_tail` 請求欄位搭配使用的輸入選項。

## 輸入

| 參數 | 說明 | 資料型態 | 必要 | Range |
|-----------|-------------|-----------|----------|-------|
| `start_frame` | 參考圖片 - URL 或 Base64 編碼字串，不得超過 10MB，解析度不低於 300×300 像素，寬高比介於 1:2.5 至 2.5:1 之間。Base64 不應包含 data:image 前綴。 | IMAGE | 是 | - |
| `end_frame` | 參考圖片 - 結束幀控制。URL 或 Base64 編碼字串，不得超過 10MB，解析度不低於 300×300 像素。Base64 不應包含 data:image 前綴。 | IMAGE | 是 | - |
| `prompt` | 正向文字提示詞 | STRING | 是 | - |
| `negative_prompt` | 負向文字提示詞 | STRING | 是 | - |
| `cfg_scale` | 控制提示詞引導的強度（預設值：0.5） | FLOAT | 否 | 0.0-1.0 |
| `aspect_ratio` | 生成影片的寬高比（預設值："16:9"） | COMBO | 否 | "16:9"<br>"9:16"<br>"1:1" |
| `mode` | 用於影片生成的配置，格式如下：mode / duration / model_name。（預設值："pro mode / 5s duration / kling-v2-5-turbo"）。所有可用選項均使用 pro 模式與 kling-v2-5-turbo 模型，僅在影片時長上有所不同。 | COMBO | 否 | "pro mode / 5s duration / kling-v2-5-turbo"<br>"pro mode / 10s duration / kling-v2-5-turbo" |

**圖片限制：**

- `start_frame` 和 `end_frame` 都必須提供，且檔案大小不得超過 10MB
- 最低解析度：兩張圖片皆為 300×300 像素
- `start_frame` 的寬高比必須介於 1:2.5 至 2.5:1 之間
- Base64 編碼的圖片不應包含 "data:image" 前綴

**提示詞限制：**

- 正向提示詞不得為空
- 正向與負向提示詞皆限制為 500 個字元
- 若 `negative_prompt` 留空，則會從請求中省略

**定價：**

- "pro mode / 5s duration / kling-v2-5-turbo"：每次生成 $0.35 美元
- "pro mode / 10s duration / kling-v2-5-turbo"：每次生成 $0.70 美元

## 輸出

| 輸出名稱 | 說明 | 資料型態 |
|-------------|-------------|-----------|
| `output` | 生成的影片序列 | VIDEO |
| `video_id` | 生成影片的唯一識別碼 | STRING |
| `duration` | 生成影片的時長 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a27977226360a425614255f8330ce7fd8ba94b8c3020eb8fdddc01eb74f035c1`
