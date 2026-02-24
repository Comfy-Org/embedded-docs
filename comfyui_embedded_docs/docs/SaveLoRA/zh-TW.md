> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/zh-TW.md)

SaveLoRA 節點會將 LoRA（低秩適應）模型儲存至檔案。它接收一個 LoRA 模型作為輸入，並將其寫入輸出目錄中的 `.safetensors` 檔案。您可以指定檔案名稱前綴以及可選的訓練步數，這些資訊將包含在最終的檔案名稱中。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `lora` | MODEL | 是 | N/A | 要儲存的 LoRA 模型。請勿使用已套用 LoRA 層的模型。 |
| `prefix` | STRING | 是 | N/A | 用於儲存 LoRA 檔案的前綴（預設值："loras/ComfyUI_trained_lora"）。 |
| `steps` | INT | 否 | N/A | 可選：LoRA 已訓練的步數，用於命名儲存的檔案。 |

**注意：** `lora` 輸入必須是純粹的 LoRA 模型。請勿提供已套用 LoRA 層的基礎模型。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| *無* | N/A | 此節點不會輸出任何資料至工作流程。它是一個輸出節點，負責將檔案儲存至磁碟。 |
