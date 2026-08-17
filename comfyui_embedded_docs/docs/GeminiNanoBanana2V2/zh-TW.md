# Nano Banana 2

此節點透過 Gemini 影像模型將文字提示傳送至 Google 的 Vertex AI API，藉此產生或編輯影像。它能根據描述建立新影像，或使用選用的參考影像修改現有影像。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 選取要使用的 Gemini 影像模型。所選模型會決定可用的解析度選項與模型專屬輸入。 | DYNAMIC_COMBO | 是 | `"Nano Banana 2 (Gemini 3.1 Flash Image)"`<br>`"Nano Banana 2 Lite"` |
| `prompt` | 描述要產生的影像或要套用編輯的文字提示。請包含模型應遵循的任何限制、樣式或細節。不得為空。（預設：空） | STRING | 是 | N/A |
| `seed` | 當種子值固定為特定數值時，模型會盡力在重複請求時提供相同的回應，但不保證輸出具有確定性。此外，即使使用相同的種子值，變更模型或參數設定（例如 temperature）也可能導致回應產生變化。依預設，會使用隨機種子值。（預設：42） | INT | 是 | 0 至 18446744073709551615 |
| `response_modalities` | 決定回應格式。IMAGE 僅回傳影像；IMAGE+TEXT 回傳影像與文字回應。（預設：IMAGE）進階參數。 | COMBO | 是 | `"IMAGE"`<br>`"IMAGE+TEXT"` |
| `system_prompt` | 規範 AI 行為的基礎指示。若留空，將使用內建提示，指示模型一律產生影像。進階參數。 | STRING | 否 | N/A |
| `temperature` | 控制生成過程的隨機性。數值越低越專注/確定。（預設：1.0）進階參數。 | FLOAT | 否 | 0.0 至 2.0（步長 0.01） |
| `top_p` | 核心取樣（Nucleus sampling）的閾值。數值越低越專注，越高越多樣化。（預設：0.95）進階參數。 | FLOAT | 否 | 0.0 至 1.0（步長 0.01） |

### Nano Banana 2 (Gemini 3.1 Flash Image) 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | 若設為 'auto'，會比對輸入影像的長寬比；若未提供影像，通常會產生 16:9 的影像。（預設：auto） | COMBO | 是 | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"`<br>`"1:4"`<br>`"4:1"`<br>`"8:1"`<br>`"1:8"` |
| `resolution` | 目標輸出解析度。 | COMBO | 是 | `"1K"`<br>`"2K"`<br>`"4K"` |
| `thinking_level` | 選取模型使用的思考等級。 | COMBO | 是 | `"MINIMAL"`<br>`"HIGH"` |

### Nano Banana 2 Lite 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | 若設為 'auto'，會比對輸入影像的長寬比；若未提供影像，通常會產生 16:9 的影像。（預設：auto） | COMBO | 是 | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"`<br>`"1:4"`<br>`"4:1"`<br>`"8:1"`<br>`"1:8"` |
| `resolution` | 目標輸出解析度。 | COMBO | 是 | `"1K"` |
| `thinking_level` | 選取模型使用的思考等級。 | COMBO | 是 | `"MINIMAL"`<br>`"HIGH"` |

### 參考輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `images` | 選用的參考影像，最多總共 14 張。可擴充插槽：連接 `image_1` 至 `image_14`。 | IMAGE | 否 | 0 至 14 張影像 |
| `files` | 選用的檔案，可作為模型的上下文。接受來自 Gemini Generate Content Input Files 節點的輸入。 | GEMINI_INPUT_FILES | 否 | N/A |

**注意：** 最多可將 14 張參考影像連接到 `images` 輸入。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | 產生或編輯後的影像。 | IMAGE |
| `STRING` | 模型產生的文字描述或標題。當未回傳文字時為空，例如當 `response_modalities` 設為 `IMAGE` 時。 | STRING |
| `thought_image` | 模型思考過程中的第一張影像。僅在 `thinking_level` 設為 HIGH 且使用 IMAGE+TEXT 模式時可用。 | IMAGE |

**注意：** 當 `response_modalities` 設為 `IMAGE` 時，`STRING` 輸出為空。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2V2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `347d28aeb46aa91f7515a31c385a3e3f805a1861116a21dd2ef6575ab7fd4f3e`
