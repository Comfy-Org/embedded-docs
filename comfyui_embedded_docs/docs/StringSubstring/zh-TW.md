# 子字串

## 概述

StringSubstring 節點可從較長的字串中擷取一部分文字。它透過指定起始位置與結束位置來定義欲擷取的區段，並傳回這兩個位置之間的文字內容。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `字串` | 要從中擷取文字的輸入字串。支援多行文字。 | STRING | 是 | - |
| `開始` | 子字串的起始位置索引。第一個字元的索引為 0。 | INT | 是 | - |
| `結束` | 子字串的結束位置索引。此索引處的字元不會包含在結果中。 | INT | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 從輸入文字中擷取的子字串，包含從 `開始` 位置開始到（但不包含）`結束` 位置之間的所有字元。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringSubstring/zh-TW.md)

---
**Source fingerprint (SHA-256):** `962d0b19af88b6c95b5c9d374081ecd55ee8cffbfb638de7ed38e6e378b220c5`
