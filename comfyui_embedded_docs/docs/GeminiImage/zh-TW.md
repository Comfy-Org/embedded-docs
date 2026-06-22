# GeminiImage

GeminiImage 節點可從 Google 的 Gemini AI 模型生成文字和圖像回應。它允許您提供多模態輸入，包括文字提示、圖像和檔案，以建立連貫的文字和圖像輸出。此節點處理與最新 Gemini 模型的所有 API 通訊和回應解析。

## 輸入

| 參數 | 說明 | 資料類型 | 輸入類型 | 預設值 | 範圍 |
| --- | --- | --- | --- | --- | --- |
| `prompt` | 用於生成的文字提示 | STRING | 必要 | "" | - |
| `model` | 用於生成回應的 Gemini 模型。 | COMBO | 必要 | gemini_2_5_flash_image_preview | `gemini_2_5_flash_image_preview`<br>`gemini_2_5_pro_exp_03_25`<br>`gemini_2_0_flash_exp_image_generation` |
| `seed` | 當種子值固定為特定數值時，模型會盡最大努力為重複請求提供相同的回應。不保證輸出具有確定性。此外，即使使用相同的種子值，更改模型或參數設定（如溫度）也可能導致回應產生變化。預設情況下，會使用隨機種子值。 | INT | 必要 | 42 | 0 到 18446744073709551615 |
| `images` | 可選的圖像，用作模型的上下文。若要包含多個圖像，可以使用批次圖像節點。 | IMAGE | 可選 | None | - |
| `files` | 可選的檔案，用作模型的上下文。接受來自 Gemini 生成內容輸入檔案節點的輸入。 | GEMINI_INPUT_FILES | 可選 | None | - |

**注意：** 此節點包含隱藏參數（`auth_token`、`comfy_api_key`、`unique_id`），這些參數由系統自動處理，無需使用者輸入。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `IMAGE` | 來自 Gemini 模型的生成圖像回應 | IMAGE |
| `STRING` | 來自 Gemini 模型的生成文字回應 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `bf55ec4f5a869a6bc5a15366f55f86ad25f9498c14056acc80951d3637bf08f2`
