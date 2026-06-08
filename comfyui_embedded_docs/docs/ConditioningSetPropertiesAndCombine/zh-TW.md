## 概述

ConditioningSetPropertiesAndCombine 節點透過將新條件輸入的屬性套用至現有條件輸入，來修改條件資料。它結合兩個條件設定，同時控制新條件的強度，並指定條件區域的套用方式。

## 輸入

| 參數 | 說明 | 資料類型 | 輸入類型 | 預設值 | 範圍 |
| --- | --- | --- | --- | --- | --- |
| `cond` | 要修改的原始條件資料 | CONDITIONING | 必要 | - | - |
| `cond_NEW` | 提供要套用屬性的新條件資料 | CONDITIONING | 必要 | - | - |
| `強度` | 控制新條件屬性的強度 | FLOAT | 必要 | 1.0 | 0.0 - 10.0 |
| `設定條件區域` | 決定條件區域的套用方式 | STRING | 必要 | default | ["default", "mask bounds"] |
| `遮罩` | 可選遮罩，用於定義條件的特定區域 | MASK | 可選 | - | - |
| `hooks` | 用於自訂處理的可選鉤子函數 | HOOKS | 可選 | - | - |
| `時間步驟` | 可選時間步長範圍，用於控制條件套用的時機 | TIMESTEPS_RANGE | 可選 | - | - |

**注意：** 當提供 `mask` 時，`set_cond_area` 參數可使用 "mask bounds" 將條件套用限制在遮罩區域內。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 已修改屬性的組合條件資料 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetPropertiesAndCombine/zh-TW.md)

---
**Source fingerprint (SHA-256):** `da57eeae428a103cbad77af063419ed0e85aeaa0b8805c8c197df27613477fa8`
