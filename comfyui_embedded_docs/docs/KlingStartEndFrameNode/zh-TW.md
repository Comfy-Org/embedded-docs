# Kling 起始-結束影格轉影片

此節點會建立一段影片序列，可在您提供的起始影像與結束影像之間進行轉場。它會產生介於兩者之間的所有影格，以形成從第一幀到最後一幀的平滑轉換。此節點會呼叫 image-to-video API，但僅支援可與 `image_tail` 請求欄位搭配使用的輸入選項。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `start_frame` | 參考影像 - URL 或 Base64 編碼字串，不可超過 10MB，解析度不得小於 300*300px，長寬比介於 1:2.5 ~ 2.5:1 之間。Base64 不應包含 data:image 前綴。 | IMAGE | 是 | - |
| `end_frame` | 參考影像 - 結束影格控制。URL 或 Base64 編碼字串，不可超過 10MB，解析度不得小於 300*300px。Base64 不應包含 data:image 前綴。 | IMAGE | 是 | - |
| `prompt` | 正向文字提示。不可為空，且不可超過 500 個字元。 | STRING | 是 | - |
| `負向提示詞` | 負向文字提示。不可超過 500 個字元。若留空，則會從請求中省略。 | STRING | 是 | - |
| `cfg_scale` | 控制提示引導的強度（預設：0.5）。 | FLOAT | 是 | 0.0-1.0 |
| `aspect_ratio` | 生成影片的長寬比（預設："16:9"）。 | COMBO | 是 | "16:9"<br>"9:16"<br>"1:1" |
| `mode` | 用於影片生成的配置，格式為：mode / duration / model_name。（預設："pro mode / 5s duration / kling-v2-5-turbo"） | COMBO | 是 | "pro mode / 5s duration / kling-v2-5-turbo"<br>"pro mode / 10s duration / kling-v2-5-turbo" |

**影像限制：**

- `start_frame` 與 `end_frame` 皆為必填，且檔案大小不可超過 10MB。
- 兩張影像的最低解析度：300×300 像素。
- `start_frame` 的長寬比必須介於 1:2.5 與 2.5:1 之間。
- Base64 編碼影像不應包含 "data:image" 前綴。

**提示限制：**

- `prompt` 不可為空，且不可超過 500 個字元。
- `negative_prompt` 不可超過 500 個字元；留空時不會隨請求送出。

**模式說明：**

- 兩個模式選項皆使用 pro mode 與 kling-v2-5-turbo 模型，差別僅在於時長（5 秒或 10 秒）。
- 每次生成的價格，如節點價格徽章所示：5s 模式為 $0.35 USD，10s 模式為 $0.70 USD。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的影片序列。 | VIDEO |
| `video_id` | 生成影片的唯一識別碼。 | STRING |
| `duration` | 生成影片的時長。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a27977226360a425614255f8330ce7fd8ba94b8c3020eb8fdddc01eb74f035c1`
