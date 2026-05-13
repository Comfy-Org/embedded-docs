> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddTextPrefix/zh-TW.md)

新增文字前綴節點透過將指定的字串添加到每個輸入文字的開頭來修改文字。它接收文字和前綴作為輸入，然後返回合併後的結果。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `text` | STRING | 是 | | 將被添加前綴的文字。 |
| `前綴` | STRING | 否 | | 要添加到文字開頭的字串（預設值：""）。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `text` | STRING | 在前端添加了前綴後所產生的文字結果。 |

---
**Source fingerprint (SHA-256):** `7f1282b1b84ea06a96ecefdec8e9e684cb6e7d3e618250dfb6e54d01f9e9ba87`
