> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3VideoGenerationNode/zh-TW.md)

使用 Google 的 Veo 3 API 從文字提示生成影片。此節點支援多種 Veo 3 模型，包括快速和輕量版本，並允許您指定影片解析度、持續時間和音訊生成。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | - | 影片的文字描述（預設值：""） |
| `aspect_ratio` | COMBO | 是 | "16:9"<br>"9:16" | 輸出影片的長寬比（預設值："16:9"） |
| `resolution` | COMBO | 否 | "720p"<br>"1080p"<br>"4k" | 輸出影片解析度。veo-3.1-lite 和 veo-3.0 模型不支援 4K。（預設值："720p"） |
| `negative_prompt` | STRING | 否 | - | 負面文字提示，用於引導影片中應避免的內容（預設值：""） |
| `duration_seconds` | INT | 否 | 4-8 | 輸出影片的持續時間（秒），以 2 為步進單位（預設值：8） |
| `enhance_prompt` | BOOLEAN | 否 | - | 此參數已棄用且被忽略。（預設值：True） |
| `person_generation` | COMBO | 否 | "ALLOW"<br>"BLOCK" | 是否允許在影片中生成人物（預設值："ALLOW"） |
| `seed` | INT | 否 | 0-4294967295 | 影片生成的隨機種子（0 表示隨機）（預設值：0） |
| `image` | IMAGE | 否 | - | 可選的參考圖片，用於引導影片生成 |
| `model` | COMBO | 否 | "veo-3.1-generate"<br>"veo-3.1-fast-generate"<br>"veo-3.1-lite"<br>"veo-3.0-generate-001"<br>"veo-3.0-fast-generate-001" | 用於影片生成的 Veo 3 模型（預設值："veo-3.0-generate-001"） |
| `generate_audio` | BOOLEAN | 否 | - | 為影片生成音訊。所有 Veo 3 模型均支援。（預設值：False） |

**注意：** `enhance_prompt` 參數已棄用，其值會被忽略。節點始終在內部增強提示。此外，`resolution` 參數僅在使用 veo-3.1 模型時生效；對於 veo-3.0 模型則會被忽略。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片檔案 |

---
**Source fingerprint (SHA-256):** `36ea9d3f0ea717eb7b8146ca35dfdfbe538fbbf164541ee1d1b19b660543e375`
