> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringCompare/zh-TW.md)

## 概述

StringCompare 節點使用不同的比較方法來比較兩個文字字串。它可以檢查一個字串是否以另一個字串開頭、結尾，或兩個字串是否完全相等。比較時可以選擇是否考慮字母大小寫差異。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `string_a` | STRING | 是 | - | 要比較的第一個字串 |
| `string_b` | STRING | 是 | - | 要比較的第二個字串 |
| `mode` | COMBO | 是 | "Starts With"<br>"Ends With"<br>"Equal" | 使用的比較方法（預設："Starts With"） |
| `case_sensitive` | BOOLEAN | 否 | - | 比較時是否考慮字母大小寫（預設：true） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | BOOLEAN | 如果符合比較條件則回傳 true，否則回傳 false |

---
**Source fingerprint (SHA-256):** `4491e4acd2c1881e9c924c6ae51d764dec5f46279094d173fe551e9ee9256597`
