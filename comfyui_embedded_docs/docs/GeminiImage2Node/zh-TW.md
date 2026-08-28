# Nano Banana Pro（Google Gemini Image）

GeminiImage2Node 節點使用 Google Vertex AI Gemini 模型生成或編輯圖像。您提供文字提示，並可選擇提供參考圖像或檔案；節點會將它們傳送至 API，並返回生成的圖像，以及（在要求時）文字回應。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述要生成的圖像或要套用的編輯的文字提示。包含模型應遵循的任何約束、樣式或細節。提示在移除空白後必須至少包含一個字元。 | STRING | 是 | N/A |
| `model` | 用於生成的特定 Gemini 模型。「Nano Banana 2 (Gemini 3.1 Flash Image)」選項在內部對應到 `gemini-3.1-flash-image` 模型，「gemini-3-pro-image-preview」對應到 `gemini-3-pro-image`。 | COMBO | 是 | `"gemini-3-pro-image-preview"`<br>`"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | 當種子固定為特定值時，模型會盡力為重複要求提供相同的回應。不保證具有確定性輸出。此外，即使使用相同的種子值，更改模型或參數設定（例如溫度）也可能導致回應產生變化。預設情況下，使用隨機種子值。預設值：42。 | INT | 是 | 0 至 18446744073709551615 |
| `aspect_ratio` | 若設為 'auto'，會比對輸入圖像的長寬比；若未提供圖像，通常會生成 16:9 的方形。預設值："auto"。 | COMBO | 是 | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` |
| `resolution` | 目標輸出解析度。對於 2K/4K，使用 Gemini 原生放大工具。 | COMBO | 是 | `"1K"`<br>`"2K"`<br>`"4K"` |
| `response_modalities` | 選擇 'IMAGE' 僅輸出圖像，或選擇 'IMAGE+TEXT' 同時返回生成的圖像和文字回應。 | COMBO | 是 | `"IMAGE+TEXT"`<br>`"IMAGE"` |
| `images` | 可選的參考圖像。若要包含多個圖像，請使用 Batch Images 節點（最多 14 個）。 | IMAGE | 否 | N/A |
| `files` | 可選的檔案，作為模型的上下文。接受來自 Gemini Generate Content Input Files 節點的輸入。 | GEMINI_INPUT_FILES | 否 | N/A |
| `system_prompt` | 決定 AI 行為的基礎指令。預設值：用於圖像生成的預先定義系統提示。 | STRING | 否 | N/A |

**限制：**

* `images` 輸入最多支援 14 張圖像。如果提供更多，則會引發錯誤。
* 當提供超過 10 張圖像時，前 10 張會以 URL 參考形式上傳，其餘圖像則以內嵌方式傳送於請求中。
* `files` 輸入必須連接到輸出 `GEMINI_INPUT_FILES` 資料型態的節點。
* 當 `response_modalities` 設為 "IMAGE" 時，僅返回圖像，文字輸出為空。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 由 Gemini 模型生成或編輯的圖像。 | IMAGE |
| `string` | 來自模型的文字回應。如果 `response_modalities` 設為 "IMAGE"，此輸出將為空。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/zh-TW.md)

---
**Source fingerprint (SHA-256):** `02293dad786d4b441da3174fa76f6c5847f122d294bd7e1f765ffd72420034a4`
