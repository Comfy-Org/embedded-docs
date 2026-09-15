# 載入 LoRA（繞過模式）（除錯用）

`LoraLoaderBypass` 節點以特殊的「bypass」模式，將 LoRA（Low-Rank Adaptation）套用到擴散模型與 CLIP 模型。與標準 LoRA 載入器不同，此方法不會永久修改基礎模型的權重。取而代之，它會將 LoRA 的貢獻加入模型的正常前向傳遞中來計算結果；這在訓練時，或處理權重被卸載的模型時很有用。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | LoRA 將套用到的擴散模型。 | MODEL | 是 | - |
| `clip` | LoRA 將套用到的 CLIP 模型。 | CLIP | 是 | - |
| `lora_name` | LoRA 的名稱。可用的 LoRA 檔案會從 `loras` 資料夾載入。 | COMBO | 是 | 可用 LoRA 檔案列表 |
| `strength_model` | 修改擴散模型的強度。此值可為負數（預設：1.0）。 | FLOAT | 是 | -100.0 到 100.0（步長：0.01） |
| `strength_clip` | 修改 CLIP 模型的強度。此值可為負數（預設：1.0）。 | FLOAT | 是 | -100.0 到 100.0（步長：0.01） |

**注意：** 若 `strength_model` 與 `strength_clip` 都設為 0，節點會直接回傳原始、未修改的 `model` 與 `clip` 輸入，而不進行處理。

**注意：** 所選的 LoRA 檔案在首次載入後會被快取。只有在選擇不同的 `lora_name` 時，才會從磁碟重新讀取。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `MODEL` | 修改後的擴散模型。 | MODEL |
| `CLIP` | 修改後的 CLIP 模型。 | CLIP |

**注意：** 此節點被標示為實驗性功能。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/zh-TW.md)

---
**Source fingerprint (SHA-256):** `025f0638a6690a53b1a6c4548dac24fb7e7f26e04ff4b1c88d29b061430037a8`
