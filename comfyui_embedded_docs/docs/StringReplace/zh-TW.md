## 概述

StringReplace 節點對輸入字串執行文字替換操作。它會在輸入文字中搜尋指定的子字串，並將所有出現的內容替換為不同的子字串。此節點會傳回已套用所有替換的修改後字串。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `字串` | 將執行替換操作的輸入文字字串 | STRING | 是 | - |
| `尋找` | 要在輸入文字中搜尋的子字串 | STRING | 是 | - |
| `取代` | 將取代所有找到內容的替換文字 | STRING | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 已將所有找到的 find 文字替換為 replace 文字的修改後字串 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringReplace/zh-TW.md)

---
**Source fingerprint (SHA-256):** `72159dba72261efe9df283c1ea3f789651eade923efdaeb108bacc1d0da663f8`
