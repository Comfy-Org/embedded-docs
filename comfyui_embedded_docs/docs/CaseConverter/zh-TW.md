> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CaseConverter/zh-TW.md)

Case Converter 節點可將文字字串轉換為不同的字母大小寫格式。它接收輸入字串並根據所選模式進行轉換，產生應用指定大小寫格式的輸出字串。此節點支援四種不同的字體大小寫轉換選項，可修改文字的大小寫格式。

## 輸入參數

| 參數名稱 | 資料類型 | 輸入類型 | 預設值 | 數值範圍 | 描述 |
|-----------|-----------|------------|---------|-------|-------------|
| `string` | STRING | 字串 | - | - | 要轉換為不同大小寫格式的文字字串 |
| `mode` | STRING | 下拉選單 | - | ["UPPERCASE", "lowercase", "Capitalize", "Title Case"] | 要套用的大小寫轉換模式：UPPERCASE 將所有字母轉換為大寫，lowercase 將所有字母轉換為小寫，Capitalize 僅將首字母大寫，Title Case 將每個單詞的首字母大寫 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | STRING | 已轉換為指定大小寫格式的輸入字串 |