# Nano Banana 2

## 概述

GeminiNanoBanana2 節點使用 Google 的 Vertex AI Gemini 模型來生成或編輯圖像。其運作方式是將文字提示，以及可選的參考圖像或檔案，發送給 API，並返回生成的圖像和任何附帶的文字。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `prompt` | 描述要生成的圖像或要套用的編輯的文字提示。請包含模型應遵循的任何限制、風格或細節。 | STRING | 是 | N/A |
| `model` | 用於圖像生成的特定 Gemini 模型。 | COMBO | 是 | `"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | 當種子固定為特定值時，模型會盡最大努力為重複的請求提供相同的回應。不保證輸出具有確定性。此外，即使使用相同的種子值，更改模型或參數設定（例如溫度）也可能導致回應產生變化。預設情況下，使用隨機種子值。（預設值：42） | INT | 是 | 0 到 18446744073709551615 |
| `aspect_ratio` | 若設為 'auto'，則會匹配輸入圖像的長寬比；若未提供圖像，通常會生成 16:9 的方形。（預設值："auto"） | COMBO | 是 | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` |
| `resolution` | 目標輸出解析度。對於 2K/4K，會使用原生的 Gemini 放大工具。 | COMBO | 是 | `"1K"`<br>`"2K"`<br>`"4K"` |
| `response_modalities` | 決定模型將返回的內容類型。（進階） | COMBO | 是 | `"IMAGE"`<br>`"IMAGE+TEXT"` |
| `thinking_level` | 控制模型推理過程的深度。 | COMBO | 是 | `"MINIMAL"`<br>`"HIGH"` |
| `images` | 可選的參考圖像。若要包含多張圖像，請使用批次圖像節點（最多 14 張）。 | IMAGE | 否 | N/A |
| `files` | 可選的檔案，用作模型的上下文。接受來自 Gemini 生成內容輸入檔案節點的輸入。 | CUSTOM | 否 | N/A |
| `system_prompt` | 指示 AI 行為的基本指令。（進階） | STRING | 否 | N/A |

**注意：** `images` 輸入最多支援 14 張圖像。如果提供的數量超過此限制，節點將引發錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `image` | 模型生成或編輯的主要圖像。 | IMAGE |
| `thought_image` | 模型返回的任何文字內容。 | STRING |
| `thought_image` | 來自模型思考過程的第一張圖像。僅在 `thinking_level` 設為 HIGH 且 `response_modalities` 設為 IMAGE+TEXT 時可用。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `bd53363da73ff0db66a872fc04f1af8ce4dfee1191ca01bd813701b5ad5e4f17`
