# SaveLatent

SaveLatent 節點將潛在樣本儲存為 .latent 檔案至磁碟，以供後續使用或分享。它使用指定的檔案名稱前綴將潛在張量資料寫入輸出資料夾，並嵌入可選的中繼資料，例如提示詞資訊。該節點也會原封不動地返回原始潛在樣本，因此工作流程可以繼續使用它們。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `samples` | 要儲存至磁碟的潛在樣本 | LATENT | 是 | - |
| `filename_prefix` | 用於產生輸出檔案名稱和子資料夾路徑的前綴（預設值："latents/ComfyUI"） | STRING | 是 | - |
| `prompt` | 工作流程提示詞資料，以 JSON 中繼資料形式儲存在儲存的檔案中（隱藏輸入，自動提供） | PROMPT | 否 | - |
| `extra_pnginfo` | 額外的工作流程中繼資料，以 JSON 形式儲存在儲存的檔案中（隱藏輸入，自動提供） | EXTRA_PNGINFO | 否 | - |

注意：除非使用 `--disable-metadata` 參數啟動 ComfyUI，否則中繼資料會寫入儲存的 .latent 檔案。儲存的檔案命名模式為 `{filename}_{5-digit counter}_.latent`，例如 `ComfyUI_00001_.latent`。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `samples` | 原始潛在樣本，原封不動地返回 | LATENT |
| `ui` | 儲存的潛在檔案之檔案位置詳細資訊（檔案名稱、子資料夾和輸出類型） | UI |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `137d52d589d93d8229940a8572621ab6eeb25a4e13ac05172e9f8609f1af038a`
