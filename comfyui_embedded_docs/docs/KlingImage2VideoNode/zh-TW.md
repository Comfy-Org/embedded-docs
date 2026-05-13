> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/zh-TW.md)

### 概述

Kling 圖像轉影片節點使用文字提示從起始參考圖像生成影片。它將圖像作為第一幀，並根據正面和負面文字描述創建影片序列，提供模型、持續時間、長寬比和生成模式等可配置選項。

### 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `start_frame` | IMAGE | 是 | - | 用於生成影片的參考圖像。 |
| `prompt` | STRING | 是 | - | 正面文字提示。 |
| `negative_prompt` | STRING | 是 | - | 負面文字提示。 |
| `model_name` | COMBO | 是 | `"kling-v2-master"`<br>`"kling-v2-1-master"`<br>`"kling-v2-5-turbo"`<br>`"kling-v2-1"`<br>`"kling-v1-6"`<br>`"kling-v1-5"`<br>`"kling-v1-4"`<br>`"kling-v1-0"` | 用於影片生成的模型（預設值：`"kling-v2-master"`）。 |
| `cfg_scale` | FLOAT | 是 | 0.0 至 1.0 | 控制影片遵循提示的程度。數值越高表示遵循度越強（預設值：0.8）。 |
| `mode` | COMBO | 是 | `"std"`<br>`"pro"` | 生成模式。`"std"` 為標準品質，`"pro"` 為更高品質（預設值：`"std"`）。 |
| `aspect_ratio` | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"` | 生成影片的長寬比（預設值：`"16:9"`）。 |
| `duration` | COMBO | 是 | `"5"`<br>`"10"` | 生成影片的持續時間，單位為秒（預設值：`"5"`）。 |

### 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片輸出。 |
| `video_id` | STRING | 生成影片的唯一識別碼。 |
| `duration` | STRING | 生成影片的持續時間資訊。 |

---
**Source fingerprint (SHA-256):** `2f82997307265dba6714733523e265d1e0a25fd7491b043f05d7d000b7b9b2f3`
