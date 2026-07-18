RegexMatch 節點會檢查文字字串是否包含符合指定正規表示式模式的內容。它會搜尋輸入字串，並回傳簡單的是/否結果，指示該模式是否存在於文字中的任何位置。您可以透過啟用不區分大小寫比對或多行模式等選項來調整搜尋方式。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `字串` | 要搜尋比對的文字字串 | STRING | 是 | - |
| `正則表達式模式` | 用於比對字串的正規表示式模式 | STRING | 是 | - |
| `忽略大小寫` | 比對時是否忽略大小寫（預設：True） | BOOLEAN | 否 | - |
| `多行模式` | 是否啟用正規表示式比對的多行模式（預設：False） | BOOLEAN | 否 | - |
| `點號匹配所有` | 是否啟用正規表示式比對的 dotall 模式（預設：False） | BOOLEAN | 否 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `匹配結果` | 如果正規表示式模式比對到輸入字串的任何部分，則回傳 True，否則回傳 False | BOOLEAN |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexMatch/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b0ee05277edd8600d880051aa33a940c01abc170553515ab02960f25b1aec2be`
