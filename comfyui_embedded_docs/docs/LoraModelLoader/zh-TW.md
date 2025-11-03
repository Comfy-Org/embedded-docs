> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraModelLoader/zh-TW.md)

LoraModelLoader 節點會將訓練過的 LoRA（低秩適應）權重應用至擴散模型。它透過載入已訓練 LoRA 模型中的 LoRA 權重並調整其影響強度，來修改基礎模型。這讓您能夠自訂擴散模型的行為，而無需從頭重新訓練。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 將要應用 LoRA 的擴散模型。 |
| `lora` | LORA_MODEL | 是 | - | 要應用至擴散模型的 LoRA 模型。 |
| `strength_model` | FLOAT | 是 | -100.0 至 100.0 | 修改擴散模型的強度。此值可以為負數（預設值：1.0）。 |

**注意：** 當 `strength_model` 設定為 0 時，節點將返回原始模型，不應用任何 LoRA 修改。

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `model` | MODEL | 已應用 LoRA 權重的修改後擴散模型。 |