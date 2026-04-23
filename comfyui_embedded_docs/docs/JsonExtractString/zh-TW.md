> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JsonExtractString/zh-TW.md)

JsonExtractString 節點會讀取包含 JSON 資料的文字字串，並提取與特定鍵相關聯的值。它會將提取的值轉換為字串。如果 JSON 無效、找不到鍵或值為 null，節點將返回一個空字串。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `json_string` | STRING | 是 | N/A | 包含待解析 JSON 資料的文字。 |
| `key` | STRING | 是 | N/A | 您希望從 JSON 物件中提取其字串值的特定鍵。 |

**注意：** 此節點僅從 JSON 物件（字典）中提取值。如果解析的 JSON 不是物件，或者指定的鍵不存在於其中，輸出將為空字串。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | STRING | 從 JSON 中為指定鍵提取的字串值，如果提取失敗則為空字串。 |