# 載入 LoRA（繞過模式）（除錯用）

LoraLoaderBypass 節點以特殊的「繞過」（bypass）模式將 LoRA（低秩適應）應用於擴散模型與 CLIP 模型。與標準 LoRA 載入器不同，此方法不會永久修改基礎模型的權重。相反，它會將 LoRA 的效果加到模型正常的前向傳播中來計算輸出，這在訓練或處理已卸載權重的模型時非常有用。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 將套用 LoRA 的擴散模型。 | MODEL | 是 | - |
| `clip` | 將套用 LoRA 的 CLIP 模型。 | CLIP | 是 | - |
| `lora_name` | LoRA 的名稱。可用的 LoRA 檔案會從 `loras` 資料夾中載入。 | COMBO | 是 | 可用 LoRA 檔案清單 |
| `strength_model` | 修改擴散模型的強度。此值可為負數（預設：1.0）。 | FLOAT | 是 | -100.0 至 100.0 (step: 0.01) |
| `strength_clip` | 修改 CLIP 模型的強度。此值可為負數（預設：1.0）。 | FLOAT | 是 | -100.0 至 100.0 (step: 0.01) |

**注意：** 如果 `strength_model` 和 `strength_clip` 都設為 0，此節點將直接傳回原始未修改的 `model` 與 `clip` 輸入，不進行任何處理。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `MODEL` | 修改後的擴散模型。 | MODEL |
| `CLIP` | 修改後的 CLIP 模型。 | CLIP |

**注意：** 此節點被標記為實驗性。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/zh-TW.md)

---
**Source fingerprint (SHA-256):** `025f0638a6690a53b1a6c4548dac24fb7e7f26e04ff4b1c88d29b061430037a8`
