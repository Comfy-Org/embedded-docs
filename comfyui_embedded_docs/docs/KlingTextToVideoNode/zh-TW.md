# Kling 文字轉影片

Kling 文字轉影片節點使用 Kling 影片生成 API 從文字描述生成影片。它會將提示詞與設定（長寬比、生成模式與 CFG 縮放）傳送至 API，等待生成任務完成，然後回傳生成的影片及其 ID 與時長。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 正向文字提示詞 | STRING | 是 | 最多 2500 個字元 |
| `負向提示詞` | 負向文字提示詞 | STRING | 否 | 最多 2500 個字元 |
| `cfg_scale` | 控制影片遵循提示詞程度的組態縮放值（預設：1.0） | FLOAT | 否 | 0.0 至 1.0 |
| `aspect_ratio` | 影片長寬比設定（預設："16:9"） | COMBO | 否 | "16:9"<br>"9:16"<br>"1:1" |
| `mode` | 用於影片生成的設定，格式為：mode / duration / model_name（預設："pro mode / 5s duration / kling-v2-5-turbo"） | COMBO | 否 | "pro mode / 5s duration / kling-v2-5-turbo"<br>"pro mode / 10s duration / kling-v2-5-turbo" |

注意：`prompt` 為必填且不得為空。`prompt` 與 `negative_prompt` 均限制最多 2500 個字元。10 秒的 `mode` 選項費用高於 5 秒選項。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的影片輸出 | VIDEO |
| `video_id` | 生成影片的唯一識別碼 | STRING |
| `duration` | 生成影片的時長資訊 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6a63b0b8bc45dc5a6300cdfe7a373399eeead36de6727f7aae2c026ba0deaea8`
