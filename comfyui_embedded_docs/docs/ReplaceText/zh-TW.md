## 概述

替換文字節點執行簡單的文字替換操作。它會在輸入文字中搜尋指定的文字片段，並將每個出現的位置替換為新的文字片段。此操作會套用至提供給節點的所有文字輸入。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `text` | 要處理的文字。 | STRING | 是 | - |
| `find` | 要尋找的文字（預設為空字串）。 | STRING | 是 | - |
| `replace` | 要替換成的文字（預設為空字串）。 | STRING | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `texts` | 已處理的文字，其中所有出現的 `find` 文字皆已替換為 `replace` 文字。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceText/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e9d4681e638c5ca2732ec254282243e9e9cdd01cc985af8bbfa41dea208cb7dd`
