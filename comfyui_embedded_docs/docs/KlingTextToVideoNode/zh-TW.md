# Kling 文字轉影片

Kling 文字轉影片節點使用 Kling 影片生成服務，將文字提示轉換為短影片片段。您提供正面與負面提示，以及寬高比、設定比例、生成模式等設定，節點將回傳生成的影片及其識別碼與持續時間。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述所需影片內容的正面文字提示。支援多行輸入。不可為空。 | STRING | 是 | Maximum 2500 characters |
| `negative_prompt` | 描述影片中應避免內容的負面文字提示。支援多行輸入。可留空。 | STRING | 是 | Maximum 2500 characters |
| `cfg_scale` | 控制影片遵循提示程度的設定比例值（預設值：1.0）。 | FLOAT | 否 | 0.0 to 1.0 |
| `aspect_ratio` | 影片寬高比設定（預設值："16:9"）。 | COMBO | 否 | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `mode` | 依照以下格式用於影片生成的設定：mode / duration / model_name（預設值："pro mode / 5s duration / kling-v2-5-turbo"）。5 秒模式費用為 0.35 美元，10 秒模式費用為 0.70 美元。 | COMBO | 否 | `"pro mode / 5s duration / kling-v2-5-turbo"`<br>`"pro mode / 10s duration / kling-v2-5-turbo"` |

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的影片輸出。 | VIDEO |
| `video_id` | 生成影片的唯一識別碼。 | STRING |
| `duration` | 生成影片的持續時間資訊。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6a63b0b8bc45dc5a6300cdfe7a373399eeead36de6727f7aae2c026ba0deaea8`
