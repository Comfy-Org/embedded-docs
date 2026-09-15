# Nano Banana 2

Nano Banana 2 節點透過 Google Vertex API 使用 Gemini 3.1 Flash Image 模型同步產生或編輯影像。它會傳送文字提示詞，以及選用的參考影像或檔案，並傳回產生的影像、任何伴隨的文字，以及選擇性地傳回模型思考過程中的影像。此節點已標記為已棄用。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述要產生之影像或要套用之編輯的文字提示詞。請包含模型應遵循的任何限制、風格或細節。不能為空或僅含空白字元。（預設：空） | STRING | 是 | N/A |
| `model` | 用於影像產生的 Gemini 模型。 | COMBO | 是 | "Nano Banana 2 (Gemini 3.1 Flash Image)" |
| `seed` | 當種子固定為特定值時，模型會盡最大努力為重複請求提供相同的回應。不保證輸出具有確定性。此外，變更模型或參數設定（例如 temperature）可能會導致回應變異，即使您使用相同的種子值也一樣。預設會使用隨機種子值。（預設：42） | INT | 是 | 0 到 18446744073709551615 |
| `aspect_ratio` | 若設為 'auto'，會符合輸入影像的長寬比；若未提供影像，通常會產生 16:9 的方形。（預設："auto"） | COMBO | 是 | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"9:16"<br>"16:9"<br>"21:9" |
| `resolution` | 目標輸出解析度。對於 2K/4K，會使用原生 Gemini 放大器。 | COMBO | 是 | "1K"<br>"2K"<br>"4K" |
| `response_modalities` | 決定模型傳回的內容類型："IMAGE" 僅傳回影像，"IMAGE+TEXT" 也會傳回文字。（進階） | COMBO | 是 | "IMAGE"<br>"IMAGE+TEXT" |
| `thinking_level` | 控制模型推理過程的深度。 | COMBO | 是 | "MINIMAL"<br>"HIGH" |
| `images` | 選用的參考影像。若要包含多張影像，請使用 Batch Images 節點（最多 14 張）。 | IMAGE | 否 | 1 到 14 張影像 |
| `files` | 選用的檔案，用作模型的上下文。接受來自 Gemini Generate Content Input Files 節點的輸入。 | CUSTOM | 否 | N/A |
| `system_prompt` | 決定 AI 行為的基礎指令。（預設：一個預設提示詞，指示模型一律產生影像）（進階） | STRING | 否 | N/A |

**注意：** `images` 輸入支援最多 14 張影像。若提供更多影像，節點會引發錯誤。`prompt` 輸入不得為空或僅含空白字元。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 模型產生或編輯的主要影像。 | IMAGE |
| `string` | 模型傳回的任何文字內容。 | STRING |
| `thought_image` | 模型思考過程中的第一張影像。僅在 `thinking_level` 設為 HIGH 且使用 IMAGE+TEXT 模態時可用。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d781c92f04d420985f8a5a593eb5f28f1f7b2af13abd11f2a7f6f285edcd9900`
