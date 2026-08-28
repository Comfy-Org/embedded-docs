# Kling 圖像轉影片

Kling 影像轉影片節點使用起始影像作為第一幀來產生短影片。它將影像與文字提示及生成設定結合，然後傳回產生的影片及其 ID 和持續時間。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `start_frame` | 用於產生影片的參考影像。影像必須至少為 300x300 像素，且長寬比介於 1:2.5 至 2.5:1 之間。 | IMAGE | 是 | - |
| `prompt` | 正向文字提示。不可為空。最多 500 個字元。 | STRING | 是 | - |
| `負向提示詞` | 負向文字提示。最多 500 個字元。若未使用則留空。 | STRING | 是 | - |
| `model_name` | 用於影片生成的模型（預設：`"kling-v2-5-turbo"`）。 | COMBO | 是 | `"kling-v2-5-turbo"` |
| `cfg_scale` | 控制影片遵循提示的程度。數值越高表示遵循程度越強（預設：0.8）。 | FLOAT | 是 | 0.0 至 1.0 |
| `mode` | 生成模式（預設：`"pro"`）。 | COMBO | 是 | `"pro"` |
| `aspect_ratio` | 生成影片的長寬比（預設：`"16:9"`）。 | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `時長` | 生成影片的持續時間（秒）（預設：`"5"`）。 | COMBO | 是 | `"5"`<br>`"10"` |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的影片輸出。 | VIDEO |
| `video_id` | 生成影片的唯一識別碼。 | STRING |
| `時長` | 生成影片的持續時間資訊。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f4a461819bc05f92d867bddcc78a66ad7beaa10707ef8cae3e7eb9e6f72c890a`
