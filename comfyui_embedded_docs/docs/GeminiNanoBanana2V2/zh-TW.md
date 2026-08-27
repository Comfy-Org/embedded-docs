# Nano Banana 2

此節點透過 Gemini 圖片模型將文字提示傳送至 Google 的 Vertex AI API，以生成或編輯圖片。它可以根據描述建立新圖片，或使用可選的參考圖片修改現有圖片。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 選擇要使用的 Gemini 圖片模型。所選模型決定可用的解析度選項和模型專屬輸入。 | DYNAMIC_COMBO | 是 | `"Nano Banana 2 (Gemini 3.1 Flash Image)"`<br>`"Nano Banana 2 Lite"` |
| `提示詞` | 描述要生成的圖片或要套用的編輯的文字提示。請包含模型應遵循的任何限制、風格或細節。不能為空。（預設：空） | STRING | 是 | N/A |
| `種子` | 當種子固定為特定值時，模型會盡力為重複請求提供相同的回應，但不保證輸出具有確定性。此外，即使使用相同的種子值，變更模型或參數設定（例如溫度）也可能導致回應產生變化。預設使用隨機種子值。（預設：42） | INT | 是 | 0 至 18446744073709551615 |
| `回應型態` | 決定回應格式。IMAGE 僅回傳圖片；IMAGE+TEXT 回傳圖片和文字回應。（預設：IMAGE）進階參數。 | COMBO | 是 | `"IMAGE"`<br>`"IMAGE+TEXT"` |
| `系統提示` | 用於決定 AI 行為的基礎指令。預設為內建提示，指示模型一律生成圖片。進階參數。 | STRING | 否 | N/A |
| `temperature` | 控制生成時的隨機性。數值越低越集中／確定性越高。（預設：1.0）進階參數。 | FLOAT | 否 | 0.0 至 2.0 (step 0.01) |
| `top_p` | 核取樣（Nucleus sampling）閾值。數值越低越集中，數值越高越多樣化。（預設：0.95）進階參數。 | FLOAT | 否 | 0.0 至 1.0 (step 0.01) |

### Nano Banana 2 (Gemini 3.1 Flash Image) 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | 若設為 'auto'，會比對輸入圖片的寬高比；若未提供圖片，通常會生成 16:9 的圖片。（預設：auto） | COMBO | 是 | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"`<br>`"1:4"`<br>`"4:1"`<br>`"8:1"`<br>`"1:8"` |
| `resolution` | 目標輸出解析度。 | COMBO | 是 | `"1K"`<br>`"2K"`<br>`"4K"` |
| `thinking_level` | 選擇模型使用的思考等級。 | COMBO | 是 | `"MINIMAL"`<br>`"HIGH"` |

### Nano Banana 2 Lite 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | 若設為 'auto'，會比對輸入圖片的寬高比；若未提供圖片，通常會生成 16:9 的圖片。（預設：auto） | COMBO | 是 | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"`<br>`"1:4"`<br>`"4:1"`<br>`"8:1"`<br>`"1:8"` |
| `resolution` | 目標輸出解析度。 | COMBO | 是 | `"1K"` |
| `thinking_level` | 選擇模型使用的思考等級。 | COMBO | 是 | `"MINIMAL"`<br>`"HIGH"` |

### 參考輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `images` | 可選的參考圖片。總共最多 14 張圖片。可擴充插槽：連接 `image_1` 至 `image_14`。 | IMAGE | 否 | 0 至 14 images |
| `files` | 可選的檔案，供模型作為上下文使用。接受來自 Gemini Generate Content Input Files 節點的輸入。 | GEMINI_INPUT_FILES | 否 | N/A |

**注意：** 最多可將 14 張參考圖片連接到 `images` 輸入；超過此限制會引發錯誤。

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | 生成或編輯後的圖片。 | IMAGE |
| `STRING` | 模型生成的文字描述或說明。當沒有回傳文字時為空，例如 `response_modalities` 設為 `IMAGE` 時。 | STRING |
| `思考影像` | 模型思考過程中的第一張圖片。僅在 `thinking_level` 設為 HIGH 且使用 IMAGE+TEXT 模式時可用。 | IMAGE |

**注意：** 當 `response_modalities` 設為 `IMAGE` 時，`STRING` 輸出為空。若模型在此模式下未生成圖片，節點會引發錯誤，並建議切換至 IMAGE+TEXT 以檢視模型的推理過程。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2V2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `347d28aeb46aa91f7515a31c385a3e3f805a1861116a21dd2ef6575ab7fd4f3e`
