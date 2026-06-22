# SaveLoRANode

SaveLoRA 節點會將 LoRA（低秩適應）模型儲存到您的輸出目錄中。它接收一個 LoRA 模型作為輸入，並建立一個具有自動生成檔案名稱的 safetensors 檔案。您可以自訂檔案名稱前綴，並選擇性地在檔案名稱中包含訓練步數，以便更好地組織管理。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `lora` | 要儲存的 LoRA 模型。請勿使用帶有 LoRA 層的模型。 | LORA_MODEL | 是 | - |
| `prefix` | 用於已儲存 LoRA 檔案的前綴（預設值："loras/ComfyUI_trained_lora"）。 | STRING | 是 | - |
| `steps` | 可選：LoRA 已訓練的步數，用於命名已儲存的檔案。 | INT | 否 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| *無* | 此節點不返回任何輸出，但會將 LoRA 模型儲存到輸出目錄。 | - |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRANode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `06a1067433aa4b720b51050b09fbad4870caf12c5e92f788d44ea022a39efef4`
