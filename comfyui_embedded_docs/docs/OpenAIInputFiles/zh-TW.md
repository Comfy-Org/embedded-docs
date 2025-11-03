> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIInputFiles/zh-TW.md)

載入並格式化 OpenAI API 的輸入檔案。此節點會準備文字和 PDF 檔案，以作為 OpenAI 聊天節點的上下文輸入。這些檔案將在生成回應時由 OpenAI 模型讀取。可以將多個輸入檔案節點鏈接在一起，以便在單一訊息中包含多個檔案。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `file` | COMBO | 是 | 提供多個選項 | 要作為模型上下文包含的輸入檔案。目前僅接受文字檔 (.txt) 和 PDF 檔 (.pdf)。檔案必須小於 32MB。 |
| `OPENAI_INPUT_FILES` | OPENAI_INPUT_FILES | 否 | N/A | 可選的附加檔案，可與此節點載入的檔案批次處理。允許鏈接輸入檔案，以便單一訊息可以包含多個輸入檔案。 |

**檔案限制：**

- 僅支援 .txt 和 .pdf 檔案
- 最大檔案大小：32MB
- 檔案從輸入目錄載入

## 輸出參數

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `OPENAI_INPUT_FILES` | OPENAI_INPUT_FILES | 格式化後的輸入檔案，準備好作為 OpenAI API 呼叫的上下文使用。 |