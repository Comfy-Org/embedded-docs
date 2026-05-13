> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JsonExtractString/zh-TW.md)

## 概述

JsonExtractString 節點會讀取包含 JSON 資料的文字字串，並提取與特定鍵相關聯的值。它會將提取的值轉換為字串。如果 JSON 無效、找不到該鍵或值為 null，此節點將回傳空字串。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `json_string` | STRING | 是 | 不適用 | 包含待解析 JSON 資料的文字內容。 |
| `key` | STRING | 是 | 不適用 | 您想從 JSON 物件中提取字串值的特定鍵。 |

**注意：** 此節點僅從 JSON 物件（字典）中提取值。如果解析後的 JSON 不是物件，或指定的鍵在物件中不存在，則輸出將為空字串。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | STRING | 從 JSON 中為指定鍵提取的字串值，若提取失敗則回傳空字串。 |

---
**Source fingerprint (SHA-256):** `f05e2d9fd4888870a844c85ac7543d6c38c1c56f2ef22a402fc93ee716743612`
