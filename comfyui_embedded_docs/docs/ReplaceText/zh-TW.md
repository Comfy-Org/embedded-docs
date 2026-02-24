> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceText/zh-TW.md)

Replace Text 節點執行簡單的文字替換功能。它會在輸入文字中搜尋指定的文字片段，並將所有匹配的內容替換為新的文字。此操作會套用至節點接收的所有文字輸入。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `text` | STRING | 是 | - | 需要處理的文字。 |
| `find` | STRING | 否 | - | 要尋找並替換的文字（預設為空字串）。 |
| `replace` | STRING | 否 | - | 用於替換找到文字的新文字（預設為空字串）。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `text` | STRING | 處理後的文字，其中所有 `find` 文字均已被 `replace` 文字替換。 |
