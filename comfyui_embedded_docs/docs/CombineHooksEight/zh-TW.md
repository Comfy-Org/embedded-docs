> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooksEight/zh-TW.md)

## 概述

Combine Hooks [8] 節點可將最多八個不同的鉤子群組合為單一合併鉤子群。它接收多個鉤子輸入，並使用 ComfyUI 的鉤子組合功能進行合併。這讓您可以整合多個鉤子配置，在進階工作流程中實現簡化處理。

## 輸入

| 參數 | 資料類型 | 輸入類型 | 預設值 | 範圍 | 說明 |
|-----------|-----------|------------|---------|-------|-------------|
| `hooks_A` | HOOKS | 可選 | None | - | 要組合的第一個鉤子群 |
| `hooks_B` | HOOKS | 可選 | None | - | 要組合的第二個鉤子群 |
| `hooks_C` | HOOKS | 可選 | None | - | 要組合的第三個鉤子群 |
| `hooks_D` | HOOKS | 可選 | None | - | 要組合的第四個鉤子群 |
| `hooks_E` | HOOKS | 可選 | None | - | 要組合的第五個鉤子群 |
| `hooks_F` | HOOKS | 可選 | None | - | 要組合的第六個鉤子群 |
| `hooks_G` | HOOKS | 可選 | None | - | 要組合的第七個鉤子群 |
| `hooks_H` | HOOKS | 可選 | None | - | 要組合的第八個鉤子群 |

**注意：** 所有輸入參數皆為可選。節點只會組合已提供的鉤子群，忽略任何留空的輸入。您可以提供一到八個鉤子群進行組合。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `HOOKS` | HOOKS | 包含所有已提供鉤子配置的單一合併鉤子群 |

---
**Source fingerprint (SHA-256):** `8cd13ec6710a9b2905c14301cfd15be616c00f1b4140451cdf0915f091c77197`
