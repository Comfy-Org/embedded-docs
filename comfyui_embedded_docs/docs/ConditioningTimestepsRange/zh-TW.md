# 步驟範圍

## 概述

ConditioningTimestepsRange 節點會建立三個不同的時間步長範圍，用於控制在生成過程中何時套用條件化效果。它接收起始與結束的百分比數值，並將整個時間步長範圍（0.0 到 1.0）劃分為三個區段：指定百分比之間的主要範圍、起始百分比之前的範圍，以及結束百分比之後的範圍。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `起始百分比` | 時間步長範圍的起始百分比（預設值：0.0） | FLOAT | 是 | 0.0 - 1.0 |
| `結束百分比` | 時間步長範圍的結束百分比（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `範圍之前` | 由 start_percent 和 end_percent 定義的主要時間步長範圍 | TIMESTEPS_RANGE |
| `範圍之前` | 從 0.0 到 start_percent 的時間步長範圍 | TIMESTEPS_RANGE |
| `範圍之後` | 從 end_percent 到 1.0 的時間步長範圍 | TIMESTEPS_RANGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningTimestepsRange/zh-TW.md)

---
**Source fingerprint (SHA-256):** `dee21b5ac80fabdeacf3f4a985550fff795702e02911400ae49a97baae834e5e`
