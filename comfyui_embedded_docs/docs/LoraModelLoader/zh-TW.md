# 載入 LoRA 模型

## 輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要套用 LoRA 的擴散模型。 | MODEL | 是 | - |
| `LoRA 模型` | 要套用至擴散模型的 LoRA 模型。 | LORA_MODEL | 是 | - |
| `模型強度` | 修改擴散模型的強度。此值可為負數（預設值：1.0）。 | FLOAT | 是 | -100.0 至 100.0 |
| `bypass` | 啟用時，以繞過模式套用 LoRA，不修改基礎模型權重。適用於訓練期間以及模型權重已卸載時（預設值：False）。 | BOOLEAN | 是 | True 或 False |

**注意：** 當 `strength_model` 設為 0 時，此節點會傳回原始模型，不套用任何 LoRA 修改。

## 輸出

| 輸出名 | 說明 | 資料型別 |
| --- | --- | --- |
| `model` | 已套用 LoRA 權重的修改後擴散模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraModelLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `81eb2a9b0376fe7453f6e7e422414472e80a3d1b92bb6874b91df6de8aed0d9a`
