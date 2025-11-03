> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringContains/zh-TW.md)

此節點檢查給定字串是否包含指定的子字串。它可以執行區分大小寫或不區分大小寫的比對檢查，並返回一個布林值結果，指示是否在主字串中找到子字串。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | 是 | - | 要搜尋的主要文字字串 |
| `substring` | STRING | 是 | - | 要在主字串中搜尋的文字 |
| `case_sensitive` | BOOLEAN | 否 | - | 決定搜尋是否應區分大小寫（預設值：true） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `contains` | BOOLEAN | 如果在字串中找到子字串則返回 true，否則返回 false |