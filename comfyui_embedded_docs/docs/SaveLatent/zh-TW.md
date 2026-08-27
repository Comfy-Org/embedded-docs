# SaveLatent

SaveLatent 會將潛在張量以 `.latent` 檔案格式儲存至磁碟，以便日後重複使用或分享。此節點接收潛在樣本，將其寫入輸出資料夾，並以自動產生的名稱命名，同時可將工作流程中繼資料（如提示詞）嵌入至已儲存的檔案中。相同的潛在樣本也會原封不動地傳遞出去，供後續處理使用。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `samples` | 要儲存至磁碟的潛在樣本。 | LATENT | 是 | - |
| `檔名前綴` | 用於建立輸出檔案名稱的前綴。可包含子資料夾，例如 "latents/ComfyUI"（預設值："latents/ComfyUI"）。 | STRING | 是 | - |
| `prompt` | 工作流程提示詞，序列化為 JSON 並儲存在檔案中繼資料中（隱藏參數，自動提供）。 | PROMPT | 否 | - |
| `extra_pnginfo` | 額外的工作流程資訊，序列化為 JSON 並儲存在檔案中繼資料中（隱藏參數，自動提供）。 | EXTRA_PNGINFO | 否 | - |

注意：每個已儲存的檔案皆使用前綴與 5 位數計數器命名，例如 `ComfyUI_00001_.latent`，並放置於輸出目錄中。檔案內容包含潛在張量與潛在格式版本標記。僅在啟用中繼資料支援時（亦即 ComfyUI 並非以 `--disable-metadata` 選項啟動時），中繼資料才會嵌入至已儲存的檔案中。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `samples` | 與輸入提供的潛在樣本相同，原封不動地傳遞出去。 | LATENT |
| `ui` | 描述已儲存檔案的使用者介面顯示資料：其檔案名稱、子資料夾與輸出類型（"output"）。 | UI |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `137d52d589d93d8229940a8572621ab6eeb25a4e13ac05172e9f8609f1af038a`
