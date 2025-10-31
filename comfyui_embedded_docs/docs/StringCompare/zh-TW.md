> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringCompare/zh-TW.md)

StringCompare 節點使用不同的比較方法來比較兩個文字字串。它可以檢查一個字串是否以另一個字串開頭、結尾，或者兩個字串是否完全相等。比較時可以選擇是否考慮字母大小寫的差異。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `string_a` | STRING | 是 | - | 要比較的第一個字串 |
| `string_b` | STRING | 是 | - | 要比較的第二個字串 |
| `mode` | COMBO | 是 | "Starts With"<br>"Ends With"<br>"Equal" | 使用的比較方法 |
| `case_sensitive` | BOOLEAN | 否 | - | 比較時是否考慮字母大小寫（預設值：true） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | BOOLEAN | 如果符合比較條件則返回 true，否則返回 false |