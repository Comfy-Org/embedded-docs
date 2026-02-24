> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/zh-TW.md)

GeminiImage2Node 使用 Google 的 Vertex AI Gemini 模型來生成或編輯圖像。它將文字提示和可選的參考圖像或檔案發送到 API，並返回生成的圖像和/或文字描述。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | N/A | 描述要生成或應用編輯的圖像的文字提示。包含模型應遵循的任何約束、風格或細節。 |
| `model` | COMBO | 是 | `"gemini-3-pro-image-preview"` | 用於生成的特定 Gemini 模型。 |
| `seed` | INT | 是 | 0 至 18446744073709551615 | 當固定為特定值時，模型會盡力為重複的請求提供相同的回應。不保證輸出具有確定性。即使使用相同的種子，更改模型或其他設定也可能導致變化。預設值：42。 |
| `aspect_ratio` | COMBO | 是 | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` | 輸出圖像所需的長寬比。如果設為 'auto'，則匹配輸入圖像的長寬比；如果未提供圖像，通常會生成 16:9 的方形圖像。預設值："auto"。 |
| `resolution` | COMBO | 是 | `"1K"`<br>`"2K"`<br>`"4K"` | 目標輸出解析度。對於 2K/4K，將使用 Gemini 的原生升頻器。 |
| `response_modalities` | COMBO | 是 | `"IMAGE+TEXT"`<br>`"IMAGE"` | 選擇 'IMAGE' 僅輸出圖像，或選擇 'IMAGE+TEXT' 同時返回生成的圖像和文字回應。 |
| `images` | IMAGE | 否 | N/A | 可選的參考圖像。要包含多個圖像，請使用批次圖像節點（最多 14 個）。 |
| `files` | CUSTOM | 否 | N/A | 可選的檔案，用作模型的上下文。接受來自 Gemini Generate Content Input Files 節點的輸入。 |
| `system_prompt` | STRING | 否 | N/A | 決定 AI 行為的基礎指令。預設值：一個預定義的用於圖像生成的系統提示。 |

**限制條件：**

* `images` 輸入最多支援 14 個圖像。如果提供更多，將會引發錯誤。
* `files` 輸入必須連接到輸出 `GEMINI_INPUT_FILES` 資料類型的節點。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `image` | IMAGE | 由 Gemini 模型生成或編輯的圖像。 |
| `string` | STRING | 來自模型的文字回應。如果 `response_modalities` 設為 "IMAGE"，此輸出將為空。 |
