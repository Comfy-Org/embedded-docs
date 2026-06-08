## 概述

組合鉤子 [2] 節點將兩個鉤子群組合為單一合併的鉤子群。它接受兩個可選的鉤子輸入，並使用 ComfyUI 的鉤子組合功能將它們合併。這讓您可以整合多個鉤子配置，以實現簡化的處理流程。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `hooks_A` | 要組合的第一個鉤子群 | HOOKS | 否 | - |
| `hooks_B` | 要組合的第二個鉤子群 | HOOKS | 否 | - |

**注意：** 兩個輸入皆為選填，但至少必須提供一個鉤子群，節點才能正常運作。如果只提供一個鉤子群，則會原樣回傳。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `hooks` | 包含兩個輸入群中所有鉤子的組合鉤子群 | HOOKS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooks/zh-TW.md)

---
**Source fingerprint (SHA-256):** `558ceef1cebedd0b7e045b7d1eb1afa4316ea6a3c35f982968af132dca164126`
