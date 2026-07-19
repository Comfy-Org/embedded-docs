# 條件配對組屬性

### 概述

**PairConditioningSetProperties** 節點允許您同時修改正向和負向條件配對的屬性。它對兩個條件輸入套用強度調整、條件區域設定以及可選的遮罩或時間控制，並返回修改後的正向和負向條件資料。

### 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向_NEW` | 要修改的正向條件輸入 | CONDITIONING | 是 | - |
| `負向_NEW` | 要修改的負向條件輸入 | CONDITIONING | 是 | - |
| `強度` | 套用於條件的強度乘數（預設值：1.0） | FLOAT | 是 | 0.0 至 10.0 |
| `設定條件區域` | 決定條件區域的計算方式（預設值："default"） | STRING | 是 | "default"<br>"mask bounds" |
| `遮罩` | 可選遮罩，用於限制條件區域 | MASK | 否 | - |
| `hooks` | 用於進階條件修改的可選鉤子群組 | HOOKS | 否 | - |
| `時間步驟` | 可選時間步範圍，用於限制條件套用的時機 | TIMESTEPS_RANGE | 否 | - |

### 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `positive` | 已套用屬性的修改後正向條件 | CONDITIONING |
| `negative` | 已套用屬性的修改後負向條件 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetProperties/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3f750c270665b4f3567790ab1ae0bdbfa176527d4f8d96cf10570a5c5deb9636`
