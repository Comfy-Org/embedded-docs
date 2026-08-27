# Nano Banana 2

GeminiNanoBanana2 節點使用 Google 的 Vertex AI Gemini 模型生成或編輯圖片。它會將文字提示，以及可選的參考圖片或檔案傳送至 API，並回傳生成的圖片與任何伴隨的文字。此節點已標記為棄用。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述要生成之圖片或要套用之編輯的文字提示。請包含模型應遵循的任何限制、風格或細節。不可為空。（預設：空） | STRING | 是 | N/A |
| `model` | 用於圖片生成的特定 Gemini 模型。 | COMBO | 是 | "Nano Banana 2 (Gemini 3.1 Flash Image)" |
| `seed` | 當種子固定為特定值時，模型會盡力在重複請求時提供相同的回應。但不保證輸出具有確定性。此外，即使使用相同的種子值，變更模型或參數設定（例如溫度）仍可能導致回應有所變化。預設會使用隨機種子值。（預設：42） | INT | 是 | 0 至 18446744073709551615 |
| `aspect_ratio` | 若設為 'auto'，會比對輸入圖片的長寬比；若未提供圖片，通常會生成 16:9 的影像。（預設："auto"） | COMBO | 是 | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"9:16"<br>"16:9"<br>"21:9" |
| `resolution` | 目標輸出解析度。使用 2K/4K 時，會使用原生的 Gemini 升頻器。 | COMBO | 是 | "1K"<br>"2K"<br>"4K" |
| `response_modalities` | 決定模型回傳的內容類型：「IMAGE」僅回傳圖片，「IMAGE+TEXT」則額外回傳文字。（進階） | COMBO | 是 | "IMAGE"<br>"IMAGE+TEXT" |
| `thinking_level` | 控制模型推理過程的深度。 | COMBO | 是 | "MINIMAL"<br>"HIGH" |
| `images` | 可選的參考圖片。若要包含多張圖片，請使用 Batch Images 節點（最多 14 張）。 | IMAGE | 否 | 1 至 14 images |
| `files` | 可選的檔案，作為給模型的上下文。接受來自 Gemini Generate Content Input Files 節點的輸入。 | CUSTOM | 否 | N/A |
| `system_prompt` | 設定 AI 行為的基礎指示。（預設：指示模型一律生成圖片的預設提示）（進階） | STRING | 否 | N/A |

**注意：** `images` 輸入最多支援 14 張圖片。若超過此數量，節點將拋出錯誤。`prompt` 輸入不得為空或僅含空白字元。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 模型生成或編輯的主要圖片。 | IMAGE |
| `string` | 模型回傳的任何文字內容。 | STRING |
| `thought_image` | 模型思考過程中的第一張圖片。僅在 `thinking_level` 為 HIGH 且 `response_modalities` 為 IMAGE+TEXT 時提供。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d781c92f04d420985f8a5a593eb5f28f1f7b2af13abd11f2a7f6f285edcd9900`
