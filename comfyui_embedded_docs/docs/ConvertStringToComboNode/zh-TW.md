> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConvertStringToComboNode/zh-TW.md)

此節點接收文字字串作為輸入，並將其轉換為 COMBO 資料類型。這讓您能將文字值用作其他需要 COMBO 輸入的節點的選項。它僅會原封不動地傳遞字串值，但會改變其資料類型。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | 是 | 不適用 | 要轉換為 COMBO 類型的文字字串。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | COMBO | 輸入的字串，現已格式化為 COMBO 資料類型。 |
