# SetFirstSigma

## 概述

SetFirstSigma 節點透過將序列中的第一個 sigma 值替換為自訂值來修改 sigma 值序列。它接收現有的 sigma 序列和一個新的 sigma 值作為輸入，然後回傳一個新的 sigma 序列，其中僅第一個元素已被更改，而所有其他 sigma 值保持不變。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `sigmas` | 待修改的輸入 sigma 值序列 | SIGMAS | 是 | - |
| `sigma` | 要設定為序列中第一個元素的新 sigma 值（預設值：136.0） | FLOAT | 是 | 0.0 至 20000.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `sigmas` | 已修改的 sigma 序列，其中第一個元素已被自訂 sigma 值取代 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetFirstSigma/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2414acd7f3f42032c12bae2c581de4721f4c1daa912255fa0956caaa567291d5`
