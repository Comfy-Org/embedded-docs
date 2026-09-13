# Nano Banana Pro（Google Gemini Image）

透過 Google Vertex AI Gemini API 同步生成或編輯影像。您提供文字提示，並可選擇附加參考影像或 Gemini 輸入檔案。此節點會回傳生成的影像，並視所選的回應模式而定，也可能回傳文字回應。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述要生成之影像或要套用之編輯的文字提示。請包含模型應遵循的任何限制、風格或細節。移除空白後，提示必須至少包含一個字元。 | STRING | 是 | N/A |
| `model` | 用於生成的 Gemini 模型。「Nano Banana 2 (Gemini 3.1 Flash Image)」選項會以 `gemini-3.1-flash-image` 傳送；「gemini-3-pro-image-preview」會以 `gemini-3-pro-image` 傳送。 | COMBO | 是 | "gemini-3-pro-image-preview"<br>"Nano Banana 2 (Gemini 3.1 Flash Image)" |
| `seed` | 當 `seed` 固定為特定值時，模型會盡最大努力對重複請求提供相同回應。不保證輸出具有確定性。此外，即使使用相同的 `seed` 值，變更模型或參數設定（例如 temperature）也可能導致回應出現變化。預設會使用隨機 `seed` 值。預設值：42。 | INT | 是 | 0 至 18446744073709551615 |
| `aspect_ratio` | 若設為 `"auto"`，會符合輸入影像的長寬比；若未提供影像，通常會生成 16:9 的影像。預設值：`"auto"`。 | COMBO | 是 | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"9:16"<br>"16:9"<br>"21:9" |
| `resolution` | 目標輸出解析度。2K/4K 會使用 Gemini 原生升頻器。 | COMBO | 是 | "1K"<br>"2K"<br>"4K" |
| `response_modalities` | 選擇 `"IMAGE"` 只輸出影像，或選擇 `"IMAGE+TEXT"` 同時回傳生成的影像與文字回應。進階設定。 | COMBO | 是 | "IMAGE+TEXT"<br>"IMAGE" |
| `images` | 可選的參考影像。若要包含多張影像，請使用 Batch Images 節點（最多 14 張）。 | IMAGE | 否 | N/A |
| `files` | 可選的檔案，用於作為模型的上下文。接受來自 Gemini Generate Content Input Files 節點的輸入。 | GEMINI_INPUT_FILES | 否 | N/A |
| `system_prompt` | 決定 AI 行為的基礎指示。預設值：用於影像生成的預先定義系統提示。進階設定。 | STRING | 否 | N/A |

**限制條件：**

* `images` 輸入最多支援 14 張影像。若提供更多影像，會引發錯誤。
* 當提供超過 10 張影像時，前 10 張會以 URL 參考形式上傳，其餘影像則在請求中以內嵌方式傳送。
* `files` 輸入必須連接到輸出 `GEMINI_INPUT_FILES` 資料類型的節點。
* 當 `response_modalities` 設為 `"IMAGE"` 時，只會回傳影像，文字輸出會是空的。
* `prompt` 輸入會經過驗證，且在移除空白後必須至少包含一個字元。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 由 Gemini 模型生成或編輯的影像。 | IMAGE |
| `string` | 來自模型的文字回應。若 `response_modalities` 設為 `"IMAGE"`，此輸出會是空的。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/zh-TW.md)

---
**Source fingerprint (SHA-256):** `02293dad786d4b441da3174fa76f6c5847f122d294bd7e1f765ffd72420034a4`
