# 儲存文字

「Save Text」節點會將文字內容寫入輸出目錄中的檔案。它支援以 .txt、.csv、.md 或 .json 格式儲存，並在提供有效的 JSON 時自動進行美化列印。

## 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `text` | 要儲存到檔案的文字內容。此輸入必須從另一個節點連接。 | STRING | 是 | - |
| `filename_prefix` | 輸出檔案名稱的前綴。會附加一個 5 位數計數器，以避免覆寫現有檔案（預設值："ComfyUI"）。 | STRING | 否 | - |
| `format` | 要將文字儲存為的檔案格式（預設值："txt"）。當選取 "json" 時，有效的 JSON 文字會以 2 個空格縮排進行美化列印；否則，文字將按原樣儲存。 | COMBO | 否 | `"txt"`<br>`"csv"`<br>`"md"`<br>`"json"` |

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `text` | 已儲存到檔案中的原始文字內容 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveText/zh-TW.md)

---
**Source fingerprint (SHA-256):** `09bd896cab770358132834892c1b37efd2ffa0cb0aa7b02b7ef91163331dc9b1`
