# 儲存文字

Save Text 節點會將文字內容寫入輸出目錄中的檔案。它支援儲存為 .txt、.csv、.md 或 .json 格式，並在提供有效 JSON 時自動進行美化排版（pretty-printing）。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `text` | 要儲存到檔案中的文字內容。此輸入必須由其他節點連接。 | STRING | 是 | - |
| `filename_prefix` | 輸出檔名的前置字串。會附加一個 5 位數計數器，以避免覆寫既有檔案（預設值："ComfyUI"）。 | STRING | 否 | - |
| `format` | 將文字儲存為的檔案格式（預設值："txt"）。當選取 "json" 時，有效的 JSON 文字會以 2 個空格縮排進行美化排版；否則，文字將原樣儲存。 | COMBO | 否 | `"txt"`<br>`"csv"`<br>`"md"`<br>`"json"` |

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `text` | 已儲存至檔案的原始文字內容 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveText/zh-TW.md)

---
**Source fingerprint (SHA-256):** `09bd896cab770358132834892c1b37efd2ffa0cb0aa7b02b7ef91163331dc9b1`
