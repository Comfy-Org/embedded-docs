> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2/zh-TW.md)

GeminiNanoBanana2 節點使用 Google 的 Vertex AI Gemini 模型來生成或編輯圖像。其運作方式是將文字提示以及可選的參考圖像或檔案發送至 API，並返回生成的圖像和任何伴隨的文字。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | N/A | 描述要生成圖像或應用編輯的文字提示。包含模型應遵循的任何約束、風格或細節。 |
| `model` | COMBO | 是 | `"Nano Banana 2 (Gemini 3.1 Flash Image)"` | 用於圖像生成的特定 Gemini 模型。 |
| `seed` | INT | 是 | 0 至 18446744073709551615 | 當種子固定為特定值時，模型會盡力為重複請求提供相同的回應。不保證輸出具有確定性。此外，即使使用相同的種子值，更改模型或參數設定（例如溫度）也可能導致回應發生變化。預設使用隨機種子值。(預設值: 42) |
| `aspect_ratio` | COMBO | 是 | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` | 若設為 'auto'，則匹配輸入圖像的長寬比；若未提供圖像，通常會生成 16:9 的正方形。(預設值: "auto") |
| `resolution` | COMBO | 是 | `"1K"`<br>`"2K"`<br>`"4K"` | 目標輸出解析度。對於 2K/4K，會使用 Gemini 原生升頻器。 |
| `response_modalities` | COMBO | 是 | `"IMAGE"`<br>`"IMAGE+TEXT"` | 決定模型將返回的內容類型。(進階設定) |
| `thinking_level` | COMBO | 是 | `"MINIMAL"`<br>`"HIGH"` | 控制模型推理過程的深度。 |
| `images` | IMAGE | 否 | N/A | 可選的參考圖像。若要包含多張圖像，請使用 Batch Images 節點（最多 14 張）。 |
| `files` | CUSTOM | 否 | N/A | 可選的檔案，用作模型的上下文。接受來自 Gemini Generate Content Input Files 節點的輸入。 |
| `system_prompt` | STRING | 否 | N/A | 決定 AI 行為的基礎指令。(進階設定) |

**注意：** `images` 輸入最多支援 14 張圖像。如果提供更多，節點將引發錯誤。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `image` | IMAGE | 模型生成或編輯的主要圖像。 |
| `string` | STRING | 模型返回的任何文字內容。 |
| `thought_image` | IMAGE | 模型思考過程中的第一張圖像。僅在 thinking_level 設為 HIGH 且 response_modalities 設為 IMAGE+TEXT 時可用。 |