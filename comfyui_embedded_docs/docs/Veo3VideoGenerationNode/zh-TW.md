# Google Veo 3 影片生成

使用 Google 的 Veo 3 API 從文字提示生成影片。此節點支援多種 Veo 3 模型，包括快速和輕量版本，並允許您指定影片解析度、持續時間和音訊生成。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `提示詞` | 影片的文字描述（預設值：""） | STRING | 是 | - |
| `長寬比` | 輸出影片的長寬比（預設值："16:9"） | COMBO | 是 | "16:9"<br>"9:16" |
| `解析度` | 輸出影片解析度。veo-3.1-lite 和 veo-3.0 模型不支援 4K。（預設值："720p"） | COMBO | 否 | "720p"<br>"1080p"<br>"4k" |
| `負向提示詞` | 負面文字提示，用於引導影片中應避免的內容（預設值：""） | STRING | 否 | - |
| `持續時間（秒）` | 輸出影片的持續時間（秒），以 2 為步進單位（預設值：8） | INT | 否 | 4-8 |
| `增強提示詞` | 此參數已棄用且被忽略。（預設值：True） | BOOLEAN | 否 | - |
| `人物生成` | 是否允許在影片中生成人物（預設值："ALLOW"） | COMBO | 否 | "ALLOW"<br>"BLOCK" |
| `種子值` | 影片生成的隨機種子（0 表示隨機）（預設值：0） | INT | 否 | 0-4294967295 |
| `圖片` | 可選的參考圖片，用於引導影片生成 | IMAGE | 否 | - |
| `模型` | 用於影片生成的 Veo 3 模型（預設值："veo-3.0-generate-001"） | COMBO | 否 | "veo-3.1-generate"<br>"veo-3.1-fast-generate"<br>"veo-3.1-lite"<br>"veo-3.0-generate-001"<br>"veo-3.0-fast-generate-001" |
| `generate_audio` | 為影片生成音訊。所有 Veo 3 模型均支援。（預設值：False） | BOOLEAN | 否 | - |

**注意：** `enhance_prompt` 參數已棄用，其值會被忽略。節點始終在內部增強提示。此外，`resolution` 參數僅在使用 veo-3.1 模型時生效；對於 veo-3.0 模型則會被忽略。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 生成的影片檔案 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3VideoGenerationNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `36ea9d3f0ea717eb7b8146ca35dfdfbe538fbbf164541ee1d1b19b660543e375`
