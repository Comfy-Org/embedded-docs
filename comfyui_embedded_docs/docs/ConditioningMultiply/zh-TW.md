# 條件（乘法）

### 概述

此節點將條件化向量乘以一個純量因子，讓您可以縮放條件化輸入的影響力。它會將乘數同時應用於主要條件化張量與池化輸出（若存在）。

### 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `conditioning` | 要進行縮放的條件化資料 | CONDITIONING | 是 | - |
| `multiplier` | 應用於條件化的縮放因子（預設值：1.0） | FLOAT | 是 | -100.0 至 100.0（步長：0.01） |

### 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `CONDITIONING` | 已縮放的條件化資料，乘數已同時應用於主要張量與池化輸出 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningMultiply/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8d241e3d5d91e513c24ade5b4bece4bf879fe093a4be6d53dab11a5a0bf55616`
