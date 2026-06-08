## 概述

Create Hook LoRA 節點用於生成鉤子物件，以便對模型套用 LoRA（低秩適應）修改。它會載入指定的 LoRA 檔案，建立可調整模型和 CLIP 強度的鉤子，然後將這些鉤子與傳入的任何現有鉤子合併。此節點透過快取先前載入的 LoRA 檔案來有效管理 LoRA 載入，避免重複操作。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `lora_name` | 要從 loras 目錄載入的 LoRA 檔案名稱 | STRING | 是 | 提供多個選項 |
| `strength_model` | 模型調整的強度倍數（預設值：1.0） | FLOAT | 是 | -20.0 至 20.0 |
| `strength_clip` | CLIP 調整的強度倍數（預設值：1.0） | FLOAT | 是 | -20.0 至 20.0 |
| `prev_hooks` | 可選的現有鉤子群組，用於與新的 LoRA 鉤子合併 | HOOKS | 否 | 不適用 |

**參數限制：**

- 如果 `strength_model` 和 `strength_clip` 都設為 0，節點將跳過建立新的 LoRA 鉤子，並直接回傳未修改的現有鉤子
- 節點會快取最後載入的 LoRA 檔案，以在重複使用相同 LoRA 時最佳化效能

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `HOOKS` | 包含合併後的 LoRA 鉤子以及任何先前鉤子的鉤子群組 | HOOKS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLora/zh-TW.md)

---
**Source fingerprint (SHA-256):** `42d5d776bfc9b239191952e2bce23513d183f904fc3c15039469381a547486f8`
