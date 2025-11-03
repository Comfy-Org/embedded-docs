> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/zh-TW.md)

OpenAIChatConfig 節點允許為 OpenAI Chat 節點設定額外的配置選項。它提供進階設定，用於控制模型生成回應的方式，包括截斷行為、輸出長度限制和自訂指令。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `truncation` | COMBO | 是 | `"auto"`<br>`"disabled"` | 模型回應使用的截斷策略。auto：若此回應與先前回應的上下文超過模型的上下文視窗大小，模型將透過丟棄對話中間的輸入項目來截斷回應以適應上下文視窗。disabled：若模型回應將超過模型的上下文視窗大小，請求將失敗並返回 400 錯誤（預設值："auto"） |
| `max_output_tokens` | INT | 否 | 16-16384 | 為回應生成之 token 數量的上限，包括可見的輸出 token（預設值：4096） |
| `instructions` | STRING | 否 | - | 模型回應的額外指令（支援多行輸入） |

## 輸出參數

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `OPENAI_CHAT_CONFIG` | OPENAI_CHAT_CONFIG | 包含指定設定的配置物件，供 OpenAI Chat 節點使用 |