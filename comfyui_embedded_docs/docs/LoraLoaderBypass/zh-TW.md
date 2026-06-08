## 概述

LoraLoaderBypass 節點以特殊的「繞過」模式將 LoRA（低秩適應）應用於擴散模型和 CLIP 模型。與標準的 LoRA 載入器不同，此方法不會永久修改基礎模型的權重。相反地，它透過將 LoRA 的效果添加到模型的正常前向傳播中來計算輸出，這在訓練或處理已卸載權重的模型時非常有用。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 將套用 LoRA 的擴散模型。 | MODEL | 是 | - |
| `clip` | 將套用 LoRA 的 CLIP 模型。 | CLIP | 是 | - |
| `lora_name` | 要套用的 LoRA 檔案名稱。選項從 `loras` 資料夾中載入。 | COMBO | 是 | *可用的 LoRA 檔案列表* |
| `strength_model` | 修改擴散模型的強度。此值可為負數（預設值：1.0）。 | FLOAT | 是 | -100.0 至 100.0 |
| `strength_clip` | 修改 CLIP 模型的強度。此值可為負數（預設值：1.0）。 | FLOAT | 是 | -100.0 至 100.0 |

**注意：** 如果 `strength_model` 和 `strength_clip` 都設為 0，則節點將直接返回原始的、未經修改的 `model` 和 `clip` 輸入，而不進行任何處理。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `MODEL` | 以繞過模式套用 LoRA 後的擴散模型。 | MODEL |
| `CLIP` | 以繞過模式套用 LoRA 後的 CLIP 模型。 | CLIP |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2642f4ed98457e5fd08e2103ffb9f2c02f11326590aadf0636fb7db51f484815`
