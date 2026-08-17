# Kling 圖像轉影片

Kling 影像轉影片節點會使用文字提示，從起始參考影像產生影片。它將該影像作為第一幀，並根據正向與負向文字描述建立影片序列，同時提供可設定的模型、時長、生成模式與長寬比選項。

## 輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `start_frame` | 用於產生影片的參考影像。必須至少為 300x300 像素，且長寬比介於 1:2.5 與 2.5:1 之間。 | IMAGE | 是 | - |
| `prompt` | 正向文字提示。最多 500 個字元。 | STRING | 是 | - |
| `negative_prompt` | 負向文字提示。最多 500 個字元。可留空。 | STRING | 是 | - |
| `model_name` | 用於影片生成的模型（預設值：`"kling-v2-5-turbo"`）。 | COMBO | 是 | `"kling-v2-5-turbo"` |
| `cfg_scale` | 控制影片遵循提示的程度。數值越高表示遵循度越強（預設值：0.8）。 | FLOAT | 是 | 0.0 至 1.0 |
| `mode` | 生成模式（預設值：`"pro"`）。 | COMBO | 是 | `"pro"` |
| `aspect_ratio` | 產生影片的長寬比（預設值：`"16:9"`）。 | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | 產生影片的時長（秒）（預設值：`"5"`）。 | COMBO | 是 | `"5"`<br>`"10"` |

註：正向提示不可為空。正向與負向提示皆限制為 500 個字元。輸入影像必須至少為 300x300 像素，且長寬比介於 1:2.5 與 2.5:1 之間。

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
|-------------|-------------|-----------|
| `output` | 產生的影片。 | VIDEO |
| `video_id` | 產生影片的唯一識別碼。 | STRING |
| `duration` | 產生影片的時長。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f4a461819bc05f92d867bddcc78a66ad7beaa10707ef8cae3e7eb9e6f72c890a`
