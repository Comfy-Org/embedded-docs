# Google Gemini

使用 Google 的 Gemini 模型生成文字回應。提供文字提示，並可選擇性地提供一張或多張圖片、音訊片段、影片或檔案作為多模態上下文。

## ## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 輸入給模型的文字。包含詳細的指示、問題或上下文。 | STRING | 是 |  |
| `model` | 用於生成回應的 Gemini 模型。 | COMBO | 是 | `"Gemini 3.1 Pro"`<br>`"Gemini 3.1 Flash-Lite"` |
| `seed` | 用於取樣的種子。設定為 0 則使用隨機種子。不保證輸出具有確定性。（預設值：42） | INT | 是 | 0 到 2147483647 |
| `system_prompt` | 決定模型行為的基礎指示。（預設值：""） | STRING | 否 |  |

**注意：** 當提供圖片、音訊或影片作為多模態上下文時，此節點會將前 10 個輸入的媒體上傳為 URL。任何額外的媒體將以 base64 資料內聯發送，最大內聯承載量為 18 MB。如果內聯承載量超過此限制，將會引發錯誤。

## ## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 從 Gemini 模型生成的文字回應。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNodeV2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ec9921f218a726082eb8987cf94b3575f61a3c6cf55fb33aeb81d42fad35d302`
