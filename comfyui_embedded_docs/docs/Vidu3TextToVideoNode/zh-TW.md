> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3TextToVideoNode/zh-TW.md)

## 概述

Vidu Q3 文字轉影片生成節點可根據文字描述建立影片。它使用 Vidu Q3 Pro 或 Q3 Turbo 模型，根據您的提示詞生成影片內容，讓您能夠控制影片的長度、解析度、長寬比，以及是否包含音訊。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `"viduq3-pro"`<br>`"viduq3-turbo"` | 用於影片生成的模型。選擇模型後會顯示長寬比、解析度、時長和音訊等額外配置參數。 |
| `model.aspect_ratio` | COMBO | 是* | `"16:9"`<br>`"9:16"`<br>`"3:4"`<br>`"4:3"`<br>`"1:1"` | 輸出影片的長寬比。此參數在選擇 `model` 後顯示。 |
| `model.resolution` | COMBO | 是* | `"720p"`<br>`"1080p"` | 輸出影片的解析度。此參數在選擇 `model` 後顯示。 |
| `model.duration` | INT | 是* | 1 至 16 | 輸出影片的時長（秒），預設值：5。此參數在選擇 `model` 後顯示。 |
| `model.audio` | BOOLEAN | 是* | True/False | 啟用後，輸出影片將包含聲音（包括對話和音效），預設值：False。此參數在選擇 `model` 後顯示。 |
| `prompt` | STRING | 是 | 不適用 | 用於影片生成的文字描述，最大長度為 2000 個字元。 |
| `seed` | INT | 否 | 0 至 2147483647 | 用於控制生成隨機性的種子值，預設值：1。 |

*注意：參數 `aspect_ratio`、`resolution`、`duration` 和 `audio` 在選擇 `model` 後為必要參數，因為它們屬於模型配置的一部分。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `video` | VIDEO | 生成的影片檔案。 |

---
**Source fingerprint (SHA-256):** `a98b6c3093d659a5a4344c2c495063acf47a7922bf7d1fc851c3b8d8c0c87c5e`
