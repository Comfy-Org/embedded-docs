> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveStringMultiline/zh-TW.md)

PrimitiveStringMultiline 節點提供了一個多行文字輸入欄位，用於在工作流程中輸入和傳遞字串值。它接受包含多行的文字輸入，並將相同的字串值原封不動地輸出。當您需要輸入較長文字內容或跨越多行的格式化文字時，此節點非常有用。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `值` | STRING | 是 | N/A | 可跨越多行的文字輸入值 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | STRING | 與輸入值相同的字串值 |