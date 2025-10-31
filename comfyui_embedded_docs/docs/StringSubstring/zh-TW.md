> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringSubstring/zh-TW.md)

StringSubstring 節點能從較長的字串中擷取部分文字內容。它透過設定起始位置和結束位置來定義您要擷取的區段，然後回傳這兩個位置之間的文字。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | 是 | - | 要從中擷取文字的輸入字串 |
| `start` | INT | 是 | - | 子字串的起始位置索引 |
| `end` | INT | 是 | - | 子字串的結束位置索引 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | STRING | 從輸入文字中擷取出的子字串 |