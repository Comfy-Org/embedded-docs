# Nano Banana 2

此節點透過 Gemini 3.1 Flash Image 模型，將文字提示傳送至 Google 的 Vertex AI API，以產生或編輯影像。它可根據描述建立新影像，或使用可選的參考影像修改既有影像。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述要產生的影像或要套用的編輯的文字提示。請包含模型應遵循的任何限制、風格或細節。不得為空。 | STRING | 是 | N/A |
| `model` | 選擇用於影像生成的 Gemini 模型。此參數包含解析度、長寬比、思考層級和參考輸入等額外子參數。 | COMBO | 是 | `"Nano Banana 2 (Gemini 3.1 Flash Image)"`<br>`"Nano Banana 2 Lite"` |
| `seed` | 當種子值固定為特定數值時，模型會盡力在重複請求時提供相同的回應。但不保證結果具有確定性。此外，即使使用相同的種子值，變更模型或參數設定（例如溫度）也可能導致回應產生變化。預設使用隨機種子值。（預設值：42） | INT | 是 | 0 至 18446744073709551615 |
| `response_modalities` | 決定回應格式。IMAGE 僅回傳影像；IMAGE+TEXT 回傳影像與文字回應。（預設值：IMAGE）進階參數。 | COMBO | 是 | `"IMAGE"`<br>`"IMAGE+TEXT"` |
| `system_prompt` | 基礎指令，用於指定 AI 的行為。預設為內建提示，指示模型一律產生影像。進階參數。 | STRING | 否 | N/A |
| `temperature` | 控制生成過程中的隨機性。數值越低越專注／確定。（預設值：1.0）進階參數。 | FLOAT | 否 | 0.0 至 2.0（步進 0.01） |
| `top_p` | 核取樣（nucleus sampling）門檻。數值越低越專注，越高越多樣化。（預設值：0.95）進階參數。 | FLOAT | 否 | 0.0 至 1.0（步進 0.01） |

### Nano Banana 2 (Gemini 3.1 Flash Image) 輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | 若設為 `'auto'`，會比對輸入影像的長寬比；若未提供影像，通常會產生 16:9 的影像。（預設值：auto） | COMBO | 是 | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"`<br>`"1:4"`<br>`"4:1"`<br>`"8:1"`<br>`"1:8"` |
| `resolution` | 目標輸出解析度。 | COMBO | 是 | `"1K"`<br>`"2K"`<br>`"4K"` |
| `thinking_level` | 選擇模型使用的思考層級。 | COMBO | 是 | `"MINIMAL"`<br>`"HIGH"` |

### Nano Banana 2 Lite 輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | 若設為 `'auto'`，會比對輸入影像的長寬比；若未提供影像，通常會產生 16:9 的影像。（預設值：auto） | COMBO | 是 | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"`<br>`"1:4"`<br>`"4:1"`<br>`"8:1"`<br>`"1:8"` |
| `resolution` | 目標輸出解析度。 | COMBO | 是 | `"1K"` |
| `thinking_level` | 選擇模型使用的思考層級。 | COMBO | 是 | `"MINIMAL"`<br>`"HIGH"` |

### 參考輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `images` | 可選的參考影像。總共最多 14 張影像。可擴充插槽：可連接 `image_1` 至 `image_14`。 | IMAGE | 否 | 0 至 14 張影像 |
| `files` | 可選的檔案，作為模型的上下文使用。接受來自 Gemini Generate Content Input Files 節點的輸入。 | GEMINI_INPUT_FILES | 否 | N/A |

**注意：** 最多可將 14 張參考影像連接到 `images` 輸入。

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
|-------------|-------------|-----------|
| `IMAGE` | 產生或編輯後的影像。 | IMAGE |
| `STRING` | 模型產生的文字描述或標題。 | STRING |
| `thought_image` | 模型思考過程中的第一張影像。僅在 `thinking_level` 設為 HIGH 且 `response_modalities` 為 IMAGE+TEXT 時可用。 | IMAGE |

**注意：** 當 `response_modalities` 設定為 `IMAGE` 時，`STRING` 輸出為空。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2V2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `347d28aeb46aa91f7515a31c385a3e3f805a1861116a21dd2ef6575ab7fd4f3e`
