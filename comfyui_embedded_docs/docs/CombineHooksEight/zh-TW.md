# CombineHooksEight

## 概述

Combine Hooks [8] 節點可將最多八個不同的鉤子群組合為單一合併鉤子群。它接收多個鉤子輸入，並使用 ComfyUI 的鉤子組合功能進行合併。這讓您可以整合多個鉤子配置，在進階工作流程中實現簡化處理。

## 輸入

| 參數 | 說明 | 資料類型 | 輸入類型 | 預設值 | 範圍 |
| --- | --- | --- | --- | --- | --- |
| `hooks_A` | 要組合的第一個鉤子群 | HOOKS | 可選 | None | - |
| `hooks_B` | 要組合的第二個鉤子群 | HOOKS | 可選 | None | - |
| `hooks_C` | 要組合的第三個鉤子群 | HOOKS | 可選 | None | - |
| `hooks_D` | 要組合的第四個鉤子群 | HOOKS | 可選 | None | - |
| `hooks_E` | 要組合的第五個鉤子群 | HOOKS | 可選 | None | - |
| `hooks_F` | 要組合的第六個鉤子群 | HOOKS | 可選 | None | - |
| `hooks_G` | 要組合的第七個鉤子群 | HOOKS | 可選 | None | - |
| `hooks_H` | 要組合的第八個鉤子群 | HOOKS | 可選 | None | - |

**注意：** 所有輸入參數皆為可選。節點只會組合已提供的鉤子群，忽略任何留空的輸入。您可以提供一到八個鉤子群進行組合。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `HOOKS` | 包含所有已提供鉤子配置的單一合併鉤子群 | HOOKS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooksEight/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8cd13ec6710a9b2905c14301cfd15be616c00f1b4140451cdf0915f091c77197`
