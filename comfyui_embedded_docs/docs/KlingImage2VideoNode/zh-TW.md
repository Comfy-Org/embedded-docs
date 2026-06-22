# Kling 圖像轉影片

### 概述

Kling 圖像轉影片節點使用文字提示從起始參考圖像生成影片。它將圖像作為第一幀，並根據正面和負面文字描述創建影片序列，提供模型、持續時間、長寬比和生成模式等可配置選項。

### 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `start_frame` | 用於生成影片的參考圖像。 | IMAGE | 是 | - |
| `prompt` | 正面文字提示。 | STRING | 是 | - |
| `負向提示詞` | 負面文字提示。 | STRING | 是 | - |
| `model_name` | 用於影片生成的模型（預設值：`"kling-v2-master"`）。 | COMBO | 是 | `"kling-v2-master"`<br>`"kling-v2-1-master"`<br>`"kling-v2-5-turbo"`<br>`"kling-v2-1"`<br>`"kling-v1-6"`<br>`"kling-v1-5"`<br>`"kling-v1-4"`<br>`"kling-v1-0"` |
| `cfg_scale` | 控制影片遵循提示的程度。數值越高表示遵循度越強（預設值：0.8）。 | FLOAT | 是 | 0.0 至 1.0 |
| `mode` | 生成模式。`"std"` 為標準品質，`"pro"` 為更高品質（預設值：`"std"`）。 | COMBO | 是 | `"std"`<br>`"pro"` |
| `aspect_ratio` | 生成影片的長寬比（預設值：`"16:9"`）。 | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `時長` | 生成影片的持續時間，單位為秒（預設值：`"5"`）。 | COMBO | 是 | `"5"`<br>`"10"` |

### 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 生成的影片輸出。 | VIDEO |
| `video_id` | 生成影片的唯一識別碼。 | STRING |
| `時長` | 生成影片的持續時間資訊。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2f82997307265dba6714733523e265d1e0a25fd7491b043f05d7d000b7b9b2f3`
