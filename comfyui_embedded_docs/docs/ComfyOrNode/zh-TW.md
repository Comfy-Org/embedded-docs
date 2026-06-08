## 概述

ComfyOrNode 對一組輸入值執行邏輯 OR 運算。根據 Python 標準的真值規則，如果任何提供的值被視為真值，則返回 `true`。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `value` | 要評估真值的值。您可以透過添加更多輸入來提供多個值。如果這些值中的任何一個為真值，節點將返回 `true`。 | ANY | 是 | 接受多個值 |

**注意：** 此節點至少接受 1 個輸入值。您可以使用自動增長功能根據需要添加更多輸入。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `BOOLEAN` | 如果任何輸入值為真值，則返回 `true`；如果所有輸入值均為假值，則返回 `false`。 | BOOLEAN |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyOrNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `00c60d5c80bbddc993af0bcd92e35dc77f153731329c23a6e4e9a980709111b1`
