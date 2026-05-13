> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetPropertiesAndCombine/zh-TW.md)

## 概述

PairConditioningSetPropertiesAndCombine 節點會透過將新的條件資料套用至現有的正向與負向條件輸入，來修改並組合條件配對。您可以調整所套用條件的強度，並控制條件區域的設定方式。此節點特別適用於需要將多個條件來源混合在一起的高階條件處理工作流程。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `正向` | CONDITIONING | 是 | - | 原始的正向條件輸入 |
| `負向` | CONDITIONING | 是 | - | 原始的負向條件輸入 |
| `positive_NEW` | CONDITIONING | 是 | - | 要套用的新正向條件 |
| `negative_NEW` | CONDITIONING | 是 | - | 要套用的新負向條件 |
| `強度` | FLOAT | 是 | 0.0 至 10.0 | 套用新條件的強度因子（預設值：1.0） |
| `設定條件區域` | STRING | 是 | "default"<br>"mask bounds" | 控制條件區域的套用方式（預設值："default"） |
| `遮罩` | MASK | 否 | - | 可選的遮罩，用於限制條件套用區域 |
| `hooks` | HOOKS | 否 | - | 可選的鉤子群組，用於進階控制 |
| `時間步驟` | TIMESTEPS_RANGE | 否 | - | 可選的時間步長範圍設定 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `負向` | CONDITIONING | 組合後的正向條件輸出 |
| `負向` | CONDITIONING | 組合後的負向條件輸出 |

---
**Source fingerprint (SHA-256):** `d434fdc1ccbe3ddee6293a6300cc55d30cb5bf357025b26777791746f51e755e`
