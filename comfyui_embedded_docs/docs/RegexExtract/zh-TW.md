> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexExtract/zh-TW.md)

RegexExtract 節點使用正規表示式在文字中搜尋模式。它可以找到第一個匹配項、所有匹配項、匹配項中的特定群組，或是跨多個匹配項的所有群組。此節點支援多種正規表示式旗標，用於控制大小寫敏感度、多行匹配和 dotall 行為。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | 是 | - | 要搜尋模式的輸入文字 |
| `regex_pattern` | STRING | 是 | - | 要搜尋的正規表示式模式 |
| `mode` | COMBO | 是 | "First Match"<br>"All Matches"<br>"First Group"<br>"All Groups" | 決定要回傳匹配項的哪些部分 |
| `case_insensitive` | BOOLEAN | 否 | - | 匹配時是否忽略大小寫（預設值：True） |
| `multiline` | BOOLEAN | 否 | - | 是否將字串視為多行（預設值：False） |
| `dotall` | BOOLEAN | 否 | - | 點號（.）是否匹配換行符（預設值：False） |
| `group_index` | INT | 否 | 0-100 | 使用群組模式時要提取的捕獲群組索引（預設值：1） |

**注意：** 當使用「First Group」或「All Groups」模式時，`group_index` 參數指定要提取哪個捕獲群組。群組 0 代表整個匹配項，而群組 1+ 代表正規表示式模式中編號的捕獲群組。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | STRING | 根據所選模式和參數提取的文字 |