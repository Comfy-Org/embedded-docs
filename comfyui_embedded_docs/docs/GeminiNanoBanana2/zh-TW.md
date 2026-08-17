# Nano Banana 2

此節點會使用 Google 的 Vertex AI Gemini 模型（Nano Banana 2 / Gemini 3.1 Flash Image）以同步方式產生或編輯圖片。它會將文字提示以及選用的參考圖片或檔案傳送至 API，並回傳產生的圖片、任何伴隨的文字，以及（選用）模型思考過程中的圖片。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述要產生之圖片或要套用之編輯的文字提示。請包含模型應遵循的任何限制、樣式或細節。必須包含至少一個非空白字元。 | STRING | 是 | N/A |
| `model` | 用於圖片產生的特定 Gemini 模型。唯一可用的選項對應至 `gemini-3.1-flash-image-preview` 模型。 | COMBO | 是 | `"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | 當種子固定為特定值時，模型會盡力對重複的請求提供相同的回應。不保證輸出具有確定性。此外，即使使用相同的種子值，變更模型或參數設定（例如溫度）仍可能導致回應產生變化。依預設，會使用隨機種子值。（預設值：42） | INT | 是 | 0 到 18446744073709551615 |
| `aspect_ratio` | 若設為「auto」，會符合您輸入圖片的長寬比；若未提供圖片，通常會產生 16:9 的方形影像。（預設值："auto"） | COMBO | 是 | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` |
| `resolution` | 目標輸出解析度。對於 2K/4K，會使用 Gemini 原生升頻器。 | COMBO | 是 | `"1K"`<br>`"2K"`<br>`"4K"` |
| `response_modalities` | 決定模型回傳的內容類型：`IMAGE` 僅回傳圖片，`IMAGE+TEXT` 亦回傳模型的推理文字。（進階） | COMBO | 是 | `"IMAGE"`<br>`"IMAGE+TEXT"` |
| `thinking_level` | 控制模型推理過程的深度。 | COMBO | 是 | `"MINIMAL"`<br>`"HIGH"` |
| `images` | 選用的參考圖片。若要包含多張圖片，請使用「Batch Images」節點（最多 14 張）。 | IMAGE | 否 | 最多 14 張圖片 |
| `files` | 選用的檔案，可作為模型的上下文。接受來自「Gemini Generate Content Input Files」節點的輸入。 | GEMINI_INPUT_FILES | 否 | N/A |
| `system_prompt` | 決定 AI 行為的基礎指令。（預設值：內建指令，要求模型一律產生圖片）（進階） | STRING | 否 | N/A |

**注意：** `images` 輸入最多接受 14 張圖片；提供更多圖片會引發錯誤。當提供超過 10 張參考圖片時，前 10 張會以檔案 URL 傳送，其餘圖片則以內嵌資料傳送。移除空白字元後，`prompt` 不得為空。此節點已標記為棄用。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 模型所產生或編輯的主要圖片。 | IMAGE |
| `string` | 模型回傳的任何文字內容。 | STRING |
| `thought_image` | 模型思考過程中的第一張圖片。僅在 `thinking_level` 設為 `HIGH` 且模式為 `IMAGE+TEXT` 時可用。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d781c92f04d420985f8a5a593eb5f28f1f7b2af13abd11f2a7f6f285edcd9900`
