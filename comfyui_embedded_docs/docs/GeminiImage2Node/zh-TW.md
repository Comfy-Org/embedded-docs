# GeminiImage2Node

GeminiImage2Node 節點使用 Google 的 Vertex AI Gemini 模型生成或編輯圖像。它將文字提示和可選的參考圖像或檔案發送到 API，並返回生成的圖像和/或文字描述。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `prompt` | 描述要生成的圖像或要套用的編輯的文字提示。包含模型應遵循的任何限制、樣式或細節。 | STRING | 是 | N/A |
| `model` | 用於生成的特定 Gemini 模型。"Nano Banana 2" 選項在內部映射到 `gemini-3.1-flash-image-preview` 模型。 | COMBO | 是 | `"gemini-3-pro-image-preview"`<br>`"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | 當固定為特定值時，模型會盡最大努力為重複請求提供相同的回應。不保證確定性輸出。即使使用相同的種子值，更改模型或其他設定也可能導致變化。預設值：42。 | INT | 是 | 0 到 18446744073709551615 |
| `aspect_ratio` | 輸出圖像的所需長寬比。如果設定為 'auto'，則會匹配輸入圖像的長寬比；如果未提供圖像，通常會生成 16:9 的方形。預設值："auto"。 | COMBO | 是 | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` |
| `resolution` | 目標輸出解析度。對於 2K/4K，會使用原生的 Gemini 放大功能。 | COMBO | 是 | `"1K"`<br>`"2K"`<br>`"4K"` |
| `response_modalities` | 選擇 'IMAGE' 僅輸出圖像，或選擇 'IMAGE+TEXT' 同時返回生成的圖像和文字回應。 | COMBO | 是 | `"IMAGE+TEXT"`<br>`"IMAGE"` |
| `images` | 可選的參考圖像。若要包含多個圖像，請使用批次圖像節點（最多 14 個）。 | IMAGE | 否 | N/A |
| `files` | 可選的檔案，用作模型的上下文。接受來自 Gemini 生成內容輸入檔案節點的輸入。 | CUSTOM | 否 | N/A |
| `system_prompt` | 指示 AI 行為的基礎指令。預設值：用於圖像生成的預定義系統提示。 | STRING | 否 | N/A |

**限制條件：**

* `images` 輸入最多支援 14 個圖像。如果提供更多圖像，將會引發錯誤。
* `files` 輸入必須連接到輸出 `GEMINI_INPUT_FILES` 資料類型的節點。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `image` | Gemini 模型生成或編輯的圖像。 | IMAGE |
| `string` | 來自模型的文字回應。如果 `response_modalities` 設定為 "IMAGE"，則此輸出將為空。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/zh-TW.md)

---
**Source fingerprint (SHA-256):** `20a937a635f883a42e22582ae415f6d2a9a6ecc50f147c9090431877e5461144`
