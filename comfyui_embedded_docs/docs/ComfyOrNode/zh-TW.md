# Or

Or 節點對一組輸入值執行邏輯 OR 運算。根據 Python 標準的真值規則，如果任何提供的值被視為 truthy，則返回 `true`。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `values` | 一個可擴充的值的集合，用於評估真值。每個新增的輸入槽位命名為 `value_1`、`value_2`，依此類推。如果任何這些值為 truthy，節點返回 `true`。 | ANY | 是 | 1 個或更多值 |

**注意：** 此節點至少接受 1 個輸入值。您可以使用自動擴充功能視需要新增更多輸入。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `BOOLEAN` | 如果任何輸入值為 truthy，則返回 `true`；如果所有輸入值皆為 falsy，則返回 `false`。 | BOOLEAN |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyOrNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f673aa2b0d754f55c51ba9c9ceea7d9de9a21d2e7308bd1281b4d4461243e4ad`
