> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetDefaultAndCombine/zh-TW.md)

## 概述

此節點使用基於鉤子的系統，將主要條件輸入與預設條件輸入結合。它將兩個條件來源合併為單一輸出，讓預設條件在主要條件不完整時作為備用或基礎。

## 輸入

| 參數 | 資料類型 | 輸入類型 | 預設值 | 範圍 | 說明 |
|-----------|-----------|------------|---------|-------|-------------|
| `cond` | CONDITIONING | 必要 | - | - | 要處理並結合的主要條件輸入 |
| `cond_DEFAULT` | CONDITIONING | 必要 | - | - | 要與主要條件結合的預設條件資料 |
| `hooks` | HOOKS | 可選 | - | - | 可選的鉤子配置，用於控制條件資料的處理與結合方式 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 合併主要與預設條件輸入後產生的結合條件資料 |

---
**Source fingerprint (SHA-256):** `5e6c95f454c7e262878cc362c6b199e01abff10f803c81afe6e76a317c30d039`
