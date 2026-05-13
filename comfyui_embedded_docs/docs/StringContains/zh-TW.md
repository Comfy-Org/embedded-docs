> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringContains/zh-TW.md)

## 概述

StringContains 節點會檢查指定的字串是否包含特定的子字串。它可以執行區分大小寫或不區分大小寫的比對，並回傳一個布林值結果，指示在主字串中是否找到了該子字串。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | 是 | - | 要進行搜尋的主要文字字串 |
| `substring` | STRING | 是 | - | 要在主字串中搜尋的文字 |
| `case_sensitive` | BOOLEAN | 否 | - | 決定搜尋是否區分大小寫（預設值：true） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `contains` | BOOLEAN | 如果在字串中找到子字串則回傳 true，否則回傳 false |

---
**Source fingerprint (SHA-256):** `ef7329ca8586e0f894306d93835490edb948a346db1e0cb011e4da5a6fe44202`
