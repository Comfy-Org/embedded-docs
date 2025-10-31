> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringConcatenate/zh-TW.md)

StringConcatenate 節點透過指定的分隔符將兩個文字字串組合成一個。它接收兩個輸入字串和一個分隔字符或字串，然後輸出單一字串，其中兩個輸入字串以分隔符連接在一起。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `string_a` | STRING | 是 | - | 要連接的第一個文字字串 |
| `string_b` | STRING | 是 | - | 要連接的第二個文字字串 |
| `delimiter` | STRING | 否 | - | 在兩個輸入字串之間插入的字符或字串（預設：空字串） |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | STRING | 在 string_a 和 string_b 之間插入分隔符後的組合字串 |