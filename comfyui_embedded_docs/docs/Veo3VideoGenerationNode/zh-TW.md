# Google Veo 3 影片生成

此節點使用 Google 的 Veo 3 API 從文字提示生成影片。此節點支援多種 Veo 3 模型，包括 fast 和 lite 變體，並允許您指定影片解析度、時長和音訊生成。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `提示詞` | 影片的文字描述（預設：""） | STRING | 是 | - |
| `長寬比` | 輸出影片的長寬比（預設："16:9"） | COMBO | 是 | "16:9"<br>"9:16" |
| `解析度` | 輸出影片解析度。4K 不適用於 veo-3.1-lite 模型。（預設："720p"） | COMBO | 否 | "720p"<br>"1080p"<br>"4k" |
| `負向提示詞` | 引導影片中應避免內容的負面文字提示（預設：""） | STRING | 否 | - |
| `持續時間（秒）` | 輸出影片的時長（秒）（預設：8） | INT | 否 | 4 - 8 (step 2) |
| `增強提示詞` | 此參數已棄用並被忽略。（預設：True） | BOOLEAN | 否 | - |
| `人物生成` | 是否允許在影片中生成人物（預設："ALLOW"） | COMBO | 否 | "ALLOW"<br>"BLOCK" |
| `種子值` | 影片生成的種子（0 表示隨機）（預設：0） | INT | 否 | 0 - 4294967295 |
| `圖片` | 可選的參考圖片，用於引導影片生成 | IMAGE | 否 | - |
| `模型` | 用於影片生成的 Veo 3 模型（預設："veo-3.1-generate"） | COMBO | 否 | "veo-3.1-generate"<br>"veo-3.1-fast-generate"<br>"veo-3.1-lite" |
| `generate_audio` | 為影片生成音訊。所有 Veo 3 模型均支援。（預設：False） | BOOLEAN | 否 | - |

**注意：** `enhance_prompt` 參數已棄用，其值會被忽略。此節點始終在內部增強提示。如果您在 veo-3.1-lite 模型中選擇「4k」解析度，此節點將拋出錯誤。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的影片檔案 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3VideoGenerationNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5320736448ad854e2f93e08ccaa870e977e06497666cb305f314bc76ff917740`
