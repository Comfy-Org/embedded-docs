> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/zh-TW.md)

此節點允許使用者與 Google 的 Gemini AI 模型互動，以生成文字回覆。您可以提供多種類型的輸入，包括文字、圖片、音訊、影片和檔案，作為模型的上下文，以產生更具關聯性和有意義的回覆。該節點會自動處理所有 API 通訊和回覆解析。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | - | 提供給模型的文字輸入，用於生成回覆。您可以包含詳細的指示、問題或上下文資訊。預設值：空字串。 |
| `model` | COMBO | 是 | `gemini-2.5-pro-preview-05-06`<br>`gemini-2.5-flash-preview-04-17`<br>`gemini-2.5-pro`<br>`gemini-2.5-flash`<br>`gemini-3-pro-preview`<br>`gemini-3-1-pro`<br>`gemini-3-1-flash-lite` | 用於生成回覆的 Gemini 模型。預設值：gemini-3-1-pro。 |
| `seed` | INT | 是 | 0 到 18446744073709551615 | 當種子值固定為特定數值時，模型會盡最大努力為重複請求提供相同的回覆。但無法保證結果的確定性。此外，即使使用相同的種子值，變更模型或參數設定（例如溫度）也可能導致回覆產生變化。預設情況下，會使用隨機種子值。預設值：42。 |
| `images` | IMAGE | 否 | - | 可選的圖片，作為模型的上下文。若要包含多張圖片，您可以使用批次圖片節點。預設值：無。 |
| `audio` | AUDIO | 否 | - | 可選的音訊，作為模型的上下文。預設值：無。 |
| `video` | VIDEO | 否 | - | 可選的影片，作為模型的上下文。預設值：無。 |
| `files` | GEMINI_INPUT_FILES | 否 | - | 可選的檔案，作為模型的上下文。接受來自 Gemini 生成內容輸入檔案節點的輸入。預設值：無。 |
| `system_prompt` | STRING | 否 | - | 用於指示 AI 行為的基礎指令。預設值：空字串。這是一個進階參數。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `STRING` | STRING | 由 Gemini 模型生成的文字回覆。 |

---
**Source fingerprint (SHA-256):** `6addc7c0bc0c5889ddd6dbcb72b0b608ab738189990c591eb7160f849f6b5374`
