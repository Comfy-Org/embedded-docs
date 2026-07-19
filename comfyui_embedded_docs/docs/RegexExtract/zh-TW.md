# 正則表達式提取

## 概述

RegexExtract 節點使用正則表達式在文字中搜尋模式。它可以找到第一個匹配項、所有匹配項、匹配項中的特定群組，或跨多個匹配項的所有群組。此節點支援多種正則表達式標誌，用於控制大小寫敏感性、多行匹配和點號匹配換行符的行為。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `字串` | 要搜尋模式的輸入文字 | STRING | 是 | - |
| `正則表達式模式` | 要搜尋的正則表達式模式 | STRING | 是 | - |
| `模式` | 提取模式決定返回匹配項的哪些部分（預設："First Match"） | COMBO | 是 | "First Match"<br>"All Matches"<br>"First Group"<br>"All Groups" |
| `忽略大小寫` | 匹配時是否忽略大小寫（預設：True） | BOOLEAN | 否 | - |
| `多行模式` | 是否將字串視為多行（預設：False） | BOOLEAN | 否 | - |
| `點號匹配所有` | 點號 (.) 是否匹配換行符（預設：False） | BOOLEAN | 否 | - |
| `群組索引` | 使用群組模式時要提取的捕獲群組索引（預設：1） | INT | 否 | 0-100 |

**注意：** 使用「First Group」或「All Groups」模式時，`group_index` 參數指定要提取哪個捕獲群組。群組 0 代表整個匹配項，而群組 1+ 代表正則表達式模式中編號的捕獲群組。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 根據所選模式和參數提取的文字 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexExtract/zh-TW.md)

---
**Source fingerprint (SHA-256):** `38e365d21bea966ed65bc78c184766330924fe75392cdb88c6978052037f5d5f`
