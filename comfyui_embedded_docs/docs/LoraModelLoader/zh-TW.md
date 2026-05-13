> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraModelLoader/zh-TW.md)

## 概述

LoraModelLoader 節點會將訓練好的 LoRA（低秩適應）權重應用於擴散模型。它透過從訓練好的 LoRA 模型載入權重並調整其影響強度來修改基礎模型。這讓您能夠自訂擴散模型的行為，而無需從頭開始重新訓練。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `模型` | MODEL | 是 | - | 將套用 LoRA 的擴散模型。 |
| `LoRA 模型` | LORA_MODEL | 是 | - | 要套用至擴散模型的 LoRA 模型。 |
| `模型強度` | FLOAT | 是 | -100.0 至 100.0 | 修改擴散模型的強度。此值可為負數（預設值：1.0）。 |
| `bypass` | BOOLEAN | 是 | True 或 False | 啟用時，以旁路模式套用 LoRA，不修改基礎模型權重。適用於訓練以及模型權重卸載時使用（預設值：False）。 |

**注意：** 當 `strength_model` 設為 0 時，節點會回傳原始模型，不套用任何 LoRA 修改。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `模型` | MODEL | 已套用 LoRA 權重的修改後擴散模型。 |

---
**Source fingerprint (SHA-256):** `82afa7dbbc990f1a9f202f920aaf8fad7fe69dc35e75ed8a95eb63c9dec74961`
