> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetPropertiesAndCombine/zh-TW.md)

## 概述

ConditioningSetPropertiesAndCombine 節點透過將新條件輸入的屬性套用至現有條件輸入，來修改條件資料。它結合兩個條件設定，同時控制新條件的強度，並指定條件區域的套用方式。

## 輸入

| 參數 | 資料類型 | 輸入類型 | 預設值 | 範圍 | 說明 |
|-----------|-----------|------------|---------|-------|-------------|
| `cond` | CONDITIONING | 必要 | - | - | 要修改的原始條件資料 |
| `cond_NEW` | CONDITIONING | 必要 | - | - | 提供要套用屬性的新條件資料 |
| `強度` | FLOAT | 必要 | 1.0 | 0.0 - 10.0 | 控制新條件屬性的強度 |
| `設定條件區域` | STRING | 必要 | default | ["default", "mask bounds"] | 決定條件區域的套用方式 |
| `遮罩` | MASK | 可選 | - | - | 可選遮罩，用於定義條件的特定區域 |
| `hooks` | HOOKS | 可選 | - | - | 用於自訂處理的可選鉤子函數 |
| `時間步驟` | TIMESTEPS_RANGE | 可選 | - | - | 可選時間步長範圍，用於控制條件套用的時機 |

**注意：** 當提供 `mask` 時，`set_cond_area` 參數可使用 "mask bounds" 將條件套用限制在遮罩區域內。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 已修改屬性的組合條件資料 |

---
**Source fingerprint (SHA-256):** `da57eeae428a103cbad77af063419ed0e85aeaa0b8805c8c197df27613477fa8`
