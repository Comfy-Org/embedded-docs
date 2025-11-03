> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexMatch/zh-TW.md)

RegexMatch 節點用於檢查文字字串是否符合指定的正規表示式模式。它會在輸入字串中搜尋符合正規表示式模式的任何出現位置，並回傳是否找到符合項。您可以設定各種正規表示式旗標，例如大小寫敏感度、多行模式和 dotall 模式，以控制模式匹配的行為。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | 是 | - | 要搜尋符合項的文字字串 |
| `regex_pattern` | STRING | 是 | - | 用於與字串匹配的正規表示式模式 |
| `case_insensitive` | BOOLEAN | 否 | - | 匹配時是否忽略大小寫（預設值：True） |
| `multiline` | BOOLEAN | 否 | - | 是否啟用正規表示式匹配的多行模式（預設值：False） |
| `dotall` | BOOLEAN | 否 | - | 是否啟用正規表示式匹配的 dotall 模式（預設值：False） |

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `matches` | BOOLEAN | 如果正規表示式模式匹配輸入字串的任何部分則回傳 True，否則回傳 False |