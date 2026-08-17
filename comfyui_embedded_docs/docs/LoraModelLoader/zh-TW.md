# 載入 LoRA 模型

LoraModelLoader 節點將訓練好的 LoRA（低秩適應）權重套用到擴散模型。它透過從訓練好的 LoRA 模型載入 LoRA 權重並調整其影響強度，來修改基礎模型。這讓您能夠自訂擴散模型的行為，而無需從頭重新訓練。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 將套用 LoRA 的擴散模型。 | MODEL | 是 | - |
| `lora` | 要套用到擴散模型的 LoRA 模型。 | LORA_MODEL | 是 | - |
| `strength_model` | 修改擴散模型的強度。此值可為負數（預設值：1.0）。 | FLOAT | 是 | -100.0 至 100.0 |
| `bypass` | 啟用時，以繞過模式套用 LoRA，而不修改基礎模型權重。適用於訓練以及模型權重已卸載的情況（預設值：False）。 | BOOLEAN | 是 | True 或 False |

**注意：** 當 `strength_model` 設定為 0 時，節點會回傳原始模型，不套用任何 LoRA 修改。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model` | 修改後的擴散模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraModelLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `81eb2a9b0376fe7453f6e7e422414472e80a3d1b92bb6874b91df6de8aed0d9a`
