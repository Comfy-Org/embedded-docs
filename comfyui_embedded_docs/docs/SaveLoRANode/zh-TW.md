> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRANode/zh-TW.md)

此節點將 LoRA（低秩適應）模型儲存到您的輸出目錄中。它接收一個 LoRA 模型作為輸入，並建立一個具有自動生成檔案名稱的 safetensors 檔案。您可以自訂檔案名稱前綴，並可選擇在檔案名稱中包含訓練步數以便更好地組織管理。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `lora` | LORA_MODEL | 是 | - | 要儲存的 LoRA 模型。請勿使用帶有 LoRA 層的模型。 |
| `prefix` | STRING | 是 | - | 用於儲存 LoRA 檔案的檔案名稱前綴（預設值："loras/ComfyUI_trained_lora"）。 |
| `steps` | INT | 否 | - | 可選：LoRA 已訓練的步數，用於命名儲存的檔案。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| *無* | - | 此節點不返回任何輸出，但會將 LoRA 模型儲存到輸出目錄中。 |