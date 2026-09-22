# 從 JSON 擷取字串

JsonExtractString 節點會掃描文字字串，尋找第一個有效的 JSON 物件，並提取與特定鍵相關聯的值，將其轉換為字串。JSON 物件前後的任何文字都會被忽略，因此此節點也適用於 Markdown 程式碼區塊，以及將 JSON 包在額外說明文字中的模型回覆。如果找不到有效的 JSON 物件、找不到該鍵，或該值為 `null`，此節點會傳回空字串。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `json_string` | 要搜尋 JSON 物件的文字。此欄位支援多行輸入，且可包含周圍的說明文字或 Markdown 程式碼區塊。 | STRING | 是 | N/A |
| `key` | 您想從 JSON 物件中提取其值的特定鍵。此欄位僅支援單行輸入。 | STRING | 是 | N/A |

**注意：** 此節點僅從 JSON 物件（字典）中提取值。它會依序嘗試輸入中的每個 `{`，並從第一個能產生有效 JSON 物件的位置開始解碼，因此會略過開頭或結尾的文字。如果無法解碼出任何 JSON 物件，或指定的鍵不存在於其中，輸出就會是空字串。如果與該鍵相關聯的值為 `null`，此節點也會傳回空字串。非字串的值會以其字串表示法回傳。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `output` | 從 JSON 中為指定鍵提取出的字串值；如果提取失敗，則為空字串。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JsonExtractString/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ca697fd3bd2d4de764372470ad1102b345d9d60f6df1c151fa0573e85fab2382`
