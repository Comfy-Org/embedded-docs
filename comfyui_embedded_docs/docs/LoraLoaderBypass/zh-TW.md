# 載入 LoRA（繞過模式）（除錯用）

LoraLoaderBypass 節點以特殊的繞過模式將 LoRA（低秩適應）應用於擴散模型和 CLIP 模型。與標準 LoRA 載入器不同，它不會永久修改基礎模型的權重。相反，它將 LoRA 的效果添加到模型正常的前向傳遞中，這在訓練或處理權重已卸載的模型時很有用。

## 輸入

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用 LoRA 的擴散模型。 | MODEL | 是 | N/A |
| `clip` | 要套用 LoRA 的 CLIP 模型。 | CLIP | 是 | N/A |
| `lora_name` | 要套用的 LoRA 檔案名稱。選項從 `loras` 資料夾載入。 | COMBO | 是 | 可用的 LoRA 檔案清單 |
| `strength_model` | 修改擴散模型的強度。此值可為負數（預設值：1.0）。 | FLOAT | 是 | -100.0 至 100.0 |
| `strength_clip` | 修改 CLIP 模型的強度。此值可為負數（預設值：1.0）。 | FLOAT | 是 | -100.0 至 100.0 |

**注意：** 如果 `strength_model` 和 `strength_clip` 都設為 0，節點將直接返回原始、未修改的 `model` 和 `clip` 輸入，不做任何處理。

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
| --- | --- | --- |
| `MODEL` | 以繞過模式套用 LoRA 後的擴散模型。 | MODEL |
| `CLIP` | 以繞過模式套用 LoRA 後的 CLIP 模型。 | CLIP |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/zh-TW.md)

---
**Source fingerprint (SHA-256):** `025f0638a6690a53b1a6c4548dac24fb7e7f26e04ff4b1c88d29b061430037a8`
