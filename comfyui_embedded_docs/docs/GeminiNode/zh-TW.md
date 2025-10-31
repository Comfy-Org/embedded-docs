> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/zh-TW.md)

此節點允許使用者與 Google 的 Gemini AI 模型互動以生成文字回應。您可以提供多種類型的輸入，包括文字、圖片、音訊、視訊和檔案作為上下文，讓模型能生成更相關且有意義的回應。此節點會自動處理所有 API 通訊和回應解析。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | - | 提供給模型的文字輸入，用於生成回應。您可以包含詳細的指示、問題或上下文。預設值：空字串。 |
| `model` | COMBO | 是 | `gemini-2.0-flash-exp`<br>`gemini-2.0-flash-thinking-exp`<br>`gemini-2.5-pro-exp`<br>`gemini-2.0-flash`<br>`gemini-2.0-flash-thinking`<br>`gemini-2.5-pro`<br>`gemini-2.0-flash-lite`<br>`gemini-1.5-flash`<br>`gemini-1.5-flash-8b`<br>`gemini-1.5-pro`<br>`gemini-1.0-pro` | 用於生成回應的 Gemini 模型。預設值：gemini-2.5-pro。 |
| `seed` | INT | 是 | 0 至 18446744073709551615 | 當種子固定為特定值時，模型會盡力為重複的請求提供相同的回應。不保證輸出具有確定性。此外，即使使用相同的種子值，更改模型或參數設定（例如溫度）也可能導致回應發生變化。預設情況下，使用隨機種子值。預設值：42。 |
| `images` | IMAGE | 否 | - | 可選的圖片，用作模型的上下文。若要包含多張圖片，您可以使用批次圖片節點。預設值：無。 |
| `audio` | AUDIO | 否 | - | 可選的音訊，用作模型的上下文。預設值：無。 |
| `video` | VIDEO | 否 | - | 可選的視訊，用作模型的上下文。預設值：無。 |
| `files` | GEMINI_INPUT_FILES | 否 | - | 可選的檔案，用作模型的上下文。接受來自 Gemini 生成內容輸入檔案節點的輸入。預設值：無。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `STRING` | STRING | 由 Gemini 模型生成的文字回應。 |