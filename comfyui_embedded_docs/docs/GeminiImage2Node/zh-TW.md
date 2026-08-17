# Nano Banana Pro（Google Gemini Image）

Nano Banana Pro（Google Gemini Image）使用 Google Vertex AI Gemini 影像模型生成或編輯圖像。它會將文字提示與可選的參考圖像或檔案一起傳送至 Gemini API，並回傳生成的圖像以及可選的文字回應。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述要生成之圖像或要套用編輯的文字提示。請包含模型應遵循的任何限制、風格或細節。預設值：空字串。 | STRING | 是 | N/A |
| `model` | 要使用的 Gemini 影像模型。選項「Nano Banana 2（Gemini 3.1 Flash Image）」會以 `gemini-3.1-flash-image` 傳送至 API；「gemini-3-pro-image-preview」則以 `gemini-3-pro-image` 傳送。 | COMBO | 是 | `"gemini-3-pro-image-preview"`<br>`"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | 當種子值固定為特定數值時，模型會盡力在重複請求時提供相同的回應。但並不保證輸出具有確定性。即使使用相同的種子值，變更模型或其他參數設定也可能導致回應產生變化。預設值：42。 | INT | 是 | 0 到 18446744073709551615 |
| `aspect_ratio` | 輸出圖像的期望長寬比。若設為「auto」，會比對您輸入圖像的長寬比；若未提供圖像，通常會生成 16:9 的方形。預設值：「auto」。 | COMBO | 是 | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` |
| `resolution` | 目標輸出解析度。若為 2K/4K，將使用 Gemini 原生升級器。 | COMBO | 是 | `"1K"`<br>`"2K"`<br>`"4K"` |
| `response_modalities` | 選擇「IMAGE」以僅輸出圖像，或選擇「IMAGE+TEXT」以同時回傳生成的圖像與文字回應。 | COMBO | 是 | `"IMAGE+TEXT"`<br>`"IMAGE"` |
| `images` | 可選的參考圖像，作為視覺上下文使用。若要包含多張圖像，請使用 Batch Images 節點（最多 14 張）。 | IMAGE | 否 | N/A |
| `files` | 可選的檔案，作為模型的上下文使用。接受來自 Gemini Generate Content Input Files 節點的輸入。 | GEMINI_INPUT_FILES | 否 | N/A |
| `system_prompt` | 決定模型行為的基礎指令。預設值：預先定義的系統提示，指示模型一律生成圖像。 | STRING | 否 | N/A |

**約束條件：**

* `prompt` 在移除前後空白後不得為空；否則會引發錯誤。
* `images` 輸入最多接受 14 張圖像。若提供超過 14 張，則會引發錯誤。
* `files` 輸入必須連接到輸出 `GEMINI_INPUT_FILES` 資料類型的節點。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 由 Gemini 模型生成或編輯的圖像。 | IMAGE |
| `string` | 模型產生的文字回應。當 `response_modalities` 設為「IMAGE」時，此輸出為空。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/zh-TW.md)

---
**Source fingerprint (SHA-256):** `02293dad786d4b441da3174fa76f6c5847f122d294bd7e1f765ffd72420034a4`
