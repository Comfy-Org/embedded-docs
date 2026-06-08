## 概述

StringCompare 節點使用不同的比較方法來比較兩個文字字串。它可以檢查一個字串是否以另一個字串開頭、結尾，或兩個字串是否完全相等。比較時可以選擇是否考慮字母大小寫差異。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `字串_a` | 要比較的第一個字串 | STRING | 是 | - |
| `字串_b` | 要比較的第二個字串 | STRING | 是 | - |
| `模式` | 使用的比較方法（預設："Starts With"） | COMBO | 是 | "Starts With"<br>"Ends With"<br>"Equal" |
| `區分大小寫` | 比較時是否考慮字母大小寫（預設：true） | BOOLEAN | 否 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 如果符合比較條件則回傳 true，否則回傳 false | BOOLEAN |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringCompare/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4491e4acd2c1881e9c924c6ae51d764dec5f46279094d173fe551e9ee9256597`
