> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringConcatenate/zh-TW.md)

## 概述

StringConcatenate 節點透過指定的分隔符號將兩個文字字串合併為一個。它接收兩個輸入字串和一個分隔符號字元或字串，然後輸出一個單一字串，其中兩個輸入字串以分隔符號連接在兩者之間。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `string_a` | STRING | 是 | - | 要連接的第一個文字字串 |
| `string_b` | STRING | 是 | - | 要連接的第二個文字字串 |
| `delimiter` | STRING | 否 | - | 插入在兩個輸入字串之間的字元或字串（預設：空字串） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | STRING | 在 string_a 和 string_b 之間插入分隔符號後組合而成的字串 |

---
**Source fingerprint (SHA-256):** `8e33665fb14a53f6c3bbfb6a4553ac7effa96d7d16d9ab2a9d4a1249abfc62e4`
