> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2V2/zh-TW.md)

## 概述

此節點透過將文字提示傳送至 Google 的 Vertex AI API 來生成或編輯圖像。它使用特定的 Gemini 模型，根據您的指示建立新圖像或修改現有圖像。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | N/A | 描述要生成的圖像或要套用的編輯的文字提示。請包含模型應遵循的任何限制、風格或細節。 |
| `model` | COMBO | 是 | `"Nano Banana 2 (Gemini 3.1 Flash Image)"` | 選擇用於圖像生成的 Gemini 模型。目前僅提供一個選項。 |
| `seed` | INT | 是 | 0 到 18446744073709551615 | 當種子值固定為特定數值時，模型會盡最大努力為重複請求提供相同的回應。不保證輸出具有確定性。此外，即使使用相同的種子值，更改模型或參數設定（例如溫度）也可能導致回應產生變化。預設情況下，會使用隨機種子值。（預設值：42） |
| `response_modalities` | COMBO | 是 | `"IMAGE"`<br>`"IMAGE+TEXT"` | 決定回應的格式。選擇 "IMAGE" 僅接收圖像，或選擇 "IMAGE+TEXT" 同時接收圖像和文字描述。（預設值："IMAGE"） |
| `system_prompt` | STRING | 否 | N/A | 指示 AI 行為的基礎指令。這是一個進階參數。 |

**關於 `model` 參數的說明：** `model` 參數是一個動態組合，包含用於解析度、長寬比和思考層級的附加子參數。這些子參數定義在模型選擇中，並未在此表格中列為單獨的輸入。

**關於圖像輸入的說明：** 您可以提供最多 14 張圖像作為模型的輸入。這些圖像透過 `model` 參數的圖像子欄位傳遞，並用於編輯或作為生成的視覺上下文。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | 生成或編輯後的圖像。 |
| `STRING` | STRING | 模型生成的文字描述或標題。 |
| `thought_image` | IMAGE | 模型思考過程中的第一張圖像。僅在思考層級為 HIGH 且回應模式為 IMAGE+TEXT 時可用。 |

---
**Source fingerprint (SHA-256):** `6b91afcdd12e08ff0e3afdbb5596bfd63463cda4d2b031019dedf03bd122fa87`
