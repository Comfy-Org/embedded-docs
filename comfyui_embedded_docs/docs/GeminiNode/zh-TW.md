# Google Gemini

此節點允許使用者與 Google 的 Gemini AI 模型互動，以產生文字回應。你可以提供多種類型的輸入，包括文字、影像、音訊、影片和檔案，作為模型的上下文，以產生更相關且有意義的回應。此節點會自動處理所有 API 通訊與回應解析。

**注意：** 此節點在原始碼中已標記為已棄用。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `提示詞` | 提供給模型的文字輸入，用於產生回應。你可以包含詳細指示、問題或模型的上下文。預設：空字串。 | STRING | 是 | - |
| `模型` | 用於產生回應的 Gemini 模型。預設：gemini-3-1-pro。 | COMBO | 是 | "gemini-2.5-pro"<br>"gemini-2.5-flash"<br>"gemini-3-pro-preview"<br>"gemini-3-1-pro"<br>"gemini-3-1-flash-lite" |
| `種子值` | 當 `seed` 固定為特定值時，模型會盡最大努力對重複請求提供相同的回應。無法保證輸出具有確定性。此外，即使使用相同的 `seed` 值，變更模型或參數設定（例如 `temperature`）也可能導致回應有所不同。預設會使用隨機 `seed` 值。預設：42。 | INT | 是 | 0 至 18446744073709551615 |
| `圖片` | 可選的影像，用於作為模型的上下文。若要包含多張影像，可以使用 Batch Images 節點。預設：None。 | IMAGE | 否 | - |
| `音訊` | 可選的音訊，用於作為模型的上下文。預設：None。 | AUDIO | 否 | - |
| `影片` | 可選的影片，用於作為模型的上下文。預設：None。 | VIDEO | 否 | - |
| `檔案` | 可選的檔案，用於作為模型的上下文。接受來自 Gemini Generate Content Input Files 節點的輸入。預設：None。 | GEMINI_INPUT_FILES | 否 | - |
| `system_prompt` | 決定 AI 行為的基礎指示。預設：空字串。這是進階參數。 | STRING | 否 | - |

所有已連接的影像都會作為上下文使用。當提供超過 10 張影像時，前 10 張會以檔案參考形式上傳，其餘影像則會內嵌傳送至 API。

此節點會使用清單中提供的所選模型名稱；某些項目會在傳送請求前，於內部對應至其目前的 API 模型識別碼。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `STRING` | 由 Gemini 模型產生的文字回應。如果模型未產生任何文字，節點會傳回「Empty response from Gemini model...」。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d1c53a5d80182085a36302867c8875df696adec6aaea9a9519a21bd6b9543d8f`
