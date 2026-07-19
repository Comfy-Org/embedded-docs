# 大小寫轉換器

## 概述

Case Converter 節點可將文字字串轉換為不同的字母大小寫格式。它接收輸入字串，並根據選取的模式進行轉換，產生套用指定大小寫格式的輸出字串。此節點支援四種不同的大小寫轉換選項，可用於修改文字的大小寫。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `字串` | 要轉換為不同大小寫格式的文字字串 | STRING | 是 | - |
| `模式` | 要套用的大小寫轉換模式（預設值：`"UPPERCASE"`） | STRING | 是 | `"UPPERCASE"`<br>`"lowercase"`<br>`"Capitalize"`<br>`"Title Case"` |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 已轉換為指定大小寫格式的輸入字串 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CaseConverter/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2493daccd5bdd86ce3fb24c6658057f5e50c2d6ed7616785f40806826f9a60dc`
