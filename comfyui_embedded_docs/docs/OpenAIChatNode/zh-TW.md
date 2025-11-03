> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/zh-TW.md)

此節點從 OpenAI 模型生成文字回應。它允許您透過發送文字提示並接收生成的回應來與 AI 模型進行對話。該節點支援多輪對話，能夠記住先前的上下文，並且還能處理影像和檔案作為模型的額外上下文。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | - | 提供給模型的文字輸入，用於生成回應（預設值：空） |
| `persist_context` | BOOLEAN | 是 | - | 在多輪對話中保持聊天上下文（預設值：True） |
| `model` | COMBO | 是 | 多種 OpenAI 模型可用 | 用於生成回應的 OpenAI 模型 |
| `images` | IMAGE | 否 | - | 可選的影像，作為模型的上下文。若要包含多張影像，可以使用批次影像節點（預設值：None） |
| `files` | OPENAI_INPUT_FILES | 否 | - | 可選的檔案，作為模型的上下文。接受來自 OpenAI 聊天輸入檔案節點的輸入（預設值：None） |
| `advanced_options` | OPENAI_CHAT_CONFIG | 否 | - | 模型的可選配置。接受來自 OpenAI 聊天進階選項節點的輸入（預設值：None） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output_text` | STRING | 由 OpenAI 模型生成的文字回應 |