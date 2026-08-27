# Kling 起始-結束影格轉影片

此節點會建立一個影片序列，在您提供的開始與結束圖片之間進行轉場。它會生成之間的所有幀，以產生從第一幀到最後一幀的平滑轉換。此節點呼叫影像轉影片 API，但僅支援可與 `image_tail` 請求欄位搭配使用的輸入選項。

## 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `start_frame` | 參考圖片 - URL 或 Base64 編碼字串，不得超過 10MB，解析度不低於 300*300px，長寬比介於 1:2.5 ~ 2.5:1 之間。Base64 不應包含 data:image 前綴。 | IMAGE | 是 | - |
| `end_frame` | 參考圖片 - 結束幀控制。URL 或 Base64 編碼字串，不得超過 10MB，解析度不低於 300*300px。Base64 不應包含 data:image 前綴。 | IMAGE | 是 | - |
| `prompt` | 正向文字提示詞。不得為空，且不得超過 500 個字元。 | STRING | 是 | - |
| `負向提示詞` | 反向文字提示詞。不得超過 500 個字元。若留空，則在請求中省略此欄位。 | STRING | 是 | - |
| `cfg_scale` | 控制提示詞引導的強度（預設值：0.5） | FLOAT | 是 | 0.0-1.0 |
| `aspect_ratio` | 生成影片的長寬比（預設值："16:9"） | COMBO | 是 | "16:9"<br>"9:16"<br>"1:1" |
| `mode` | 用於影片生成的配置，格式為：模式 / 時長 / 模型名稱。（預設值："pro mode / 5s duration / kling-v2-5-turbo"） | COMBO | 是 | "pro mode / 5s duration / kling-v2-5-turbo"<br>"pro mode / 10s duration / kling-v2-5-turbo" |

**圖片約束：**

- `start_frame` 和 `end_frame` 皆為必填，且檔案大小不得超過 10MB。
- 最低解析度：兩張圖片皆需為 300×300 像素。
- `start_frame` 的長寬比必須介於 1:2.5 和 2.5:1 之間。
- Base64 編碼的圖片不應包含 "data:image" 前綴。

**提示詞約束：**

- `prompt` 不得為空，且不得超過 500 個字元。
- `negative_prompt` 不得超過 500 個字元；若為空，則不會隨請求一併發送。

**模式說明：**

- 兩種模式選項皆使用 pro mode 搭配 kling-v2-5-turbo 模型，僅在時長上有所不同（5 秒或 10 秒）。
- 每次生成的價格，如節點價格標籤所示：5 秒模式每次收費 0.35 美元，10 秒模式每次收費 0.70 美元。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `output` | 生成的影片序列 | VIDEO |
| `video_id` | 生成影片的唯一識別碼 | STRING |
| `時長` | 生成影片的時長 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a27977226360a425614255f8330ce7fd8ba94b8c3020eb8fdddc01eb74f035c1`
