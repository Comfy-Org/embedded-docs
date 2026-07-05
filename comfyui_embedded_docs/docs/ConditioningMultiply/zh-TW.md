# ConditioningMultiply

此節點將條件化數值乘以指定的係數，讓您可以調整條件化對生成過程的影響程度。其運作方式是將乘數同時應用於主要條件化張量與池化輸出值。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `conditioning` | 要進行縮放的條件化資料 | CONDITIONING | 是 | - |
| `multiplier` | 用於乘以條件化數值的係數（預設值：1.0） | FLOAT | 是 | -100.0 至 100.0（步長：0.01） |

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `CONDITIONING` | 經過數值相乘後的縮放條件化資料 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningMultiply/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8d241e3d5d91e513c24ade5b4bece4bf879fe093a4be6d53dab11a5a0bf55616`
