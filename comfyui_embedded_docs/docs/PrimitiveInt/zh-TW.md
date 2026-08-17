# 整數

PrimitiveInt 節點提供了一種簡單的方式，讓您在工作流程中處理整數值。它接受整數輸入並輸出相同的值，非常適合在節點之間傳遞整數參數，或為其他操作設定特定數值。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `value` | 要輸出的整數值（預設值：0） | INT | 是 | -9223372036854775807 至 9223372036854775807 |

注意：`value` 參數設定為固定的「生成後控制」行為，因此每次生成後該值不會自動變更。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `output` | 輸入的整數值原封不動地傳遞輸出 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveInt/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b928ec40c781043c1c8652de3aebedc755d9b63be9e2c773e3fb26ce4d594bba`
