# Kling 文字轉影片

Kling 文字轉影片節點透過 Kling 影片生成 API，從文字描述產生影片。它會將提示詞與設定（畫面比例、生成模式與 CFG scale）傳送至 API，等待生成任務完成，然後回傳產生的影片及其 ID 與時長。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述期望影片內容的正面文字提示詞 | STRING | 是 | 最多 2500 個字元 |
| `負向提示詞` | 描述影片中應避免內容的負面文字提示詞 | STRING | 否 | 最多 2500 個字元 |
| `cfg_scale` | 控制影片遵循提示詞程度的配置比例（預設值：1.0） | FLOAT | 否 | 0.0 至 1.0 |
| `aspect_ratio` | 影片畫面比例設定（預設值："16:9"） | COMBO | 否 | "16:9"<br>"9:16"<br>"1:1" |
| `mode` | 用於影片生成的配置，格式如下：mode / duration / model_name（預設值："pro mode / 5s duration / kling-v2-5-turbo"） | COMBO | 否 | "pro mode / 5s duration / kling-v2-5-turbo"<br>"pro mode / 10s duration / kling-v2-5-turbo" |

注意：`prompt` 參數為必填，且不得為空。`prompt` 與 `negative_prompt` 皆限制為最多 2500 個字元。

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 產生的影片輸出 | VIDEO |
| `video_id` | 所產生影片的唯一識別碼 | STRING |
| `時長` | 所產生影片的時長資訊 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6a63b0b8bc45dc5a6300cdfe7a373399eeead36de6727f7aae2c026ba0deaea8`
