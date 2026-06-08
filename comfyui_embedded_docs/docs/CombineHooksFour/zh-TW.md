## 概述

Combine Hooks [4] 節點可將最多四個獨立的鉤子群組合為單一合併鉤子群。它會接收四個可用鉤子輸入的任意組合，並使用 ComfyUI 的鉤子組合系統進行合併。這讓您能夠整合多個鉤子配置，以在進階工作流程中實現簡化處理。

## 輸入

| 參數 | 說明 | 資料類型 | 輸入類型 | 預設值 | 範圍 |
| --- | --- | --- | --- | --- | --- |
| `hooks_A` | 要組合的第一個鉤子群 | HOOKS | 可選 | None | - |
| `hooks_B` | 要組合的第二個鉤子群 | HOOKS | 可選 | None | - |
| `hooks_C` | 要組合的第三個鉤子群 | HOOKS | 可選 | None | - |
| `hooks_D` | 要組合的第四個鉤子群 | HOOKS | 可選 | None | - |

**注意：** 所有四個鉤子輸入皆為可選。此節點只會組合已提供的鉤子群，若未連接任何輸入，則會回傳空的鉤子群。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `HOOKS` | 包含所有已提供鉤子配置的合併鉤子群 | HOOKS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooksFour/zh-TW.md)

---
**Source fingerprint (SHA-256):** `92a8038e7b5a7491afcbd48830a1e278fe4d697321fb874821ebf7edd09d5815`
