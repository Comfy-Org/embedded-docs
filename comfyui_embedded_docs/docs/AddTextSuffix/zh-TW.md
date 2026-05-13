> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddTextSuffix/zh-TW.md)

此節點會將指定的後綴附加到輸入文字字串的結尾。它接收原始文字與後綴作為輸入，然後回傳合併後的結果。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `text` | STRING | 是 | | 將被附加後綴的原始文字。 |
| `suffix` | STRING | 否 | | 要附加到文字上的後綴（預設值：""）。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `text` | STRING | 附加後綴後所產生的結果文字。 |

---
**Source fingerprint (SHA-256):** `5dd75a9a29709a35343ec0dce144d2eb27a6e7aef5cb0b9245329c678897a763`
