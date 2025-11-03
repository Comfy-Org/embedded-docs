> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiInputFiles/zh-TW.md)

載入並格式化輸入檔案以供 Gemini API 使用。此節點允許使用者將文字檔 (.txt) 和 PDF 檔 (.pdf) 作為輸入上下文提供給 Gemini 模型。檔案會被轉換為 API 所需的適當格式，並且可以鏈接在一起，以便在單一請求中包含多個檔案。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `file` | COMBO | 是 | 提供多個選項 | 要作為模型上下文包含的輸入檔案。目前僅接受文字檔 (.txt) 和 PDF 檔 (.pdf)。檔案必須小於最大輸入檔案大小限制。 |
| `GEMINI_INPUT_FILES` | GEMINI_INPUT_FILES | 否 | N/A | 可選的附加檔案，用於與此節點載入的檔案進行批次處理。允許鏈接輸入檔案，以便單一訊息可以包含多個輸入檔案。 |

**注意：** `file` 參數僅顯示小於最大輸入檔案大小限制的文字檔 (.txt) 和 PDF 檔 (.pdf)。檔案會自動按名稱篩選和排序。

## 輸出參數

| 輸出名稱 | 資料類型 | 參數說明 |
|-------------|-----------|-------------|
| `GEMINI_INPUT_FILES` | GEMINI_INPUT_FILES | 格式化後的檔案資料，準備好用於 Gemini LLM 節點，其中包含已載入的檔案內容，並轉換為適當的 API 格式。 |