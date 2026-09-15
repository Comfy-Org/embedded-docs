# 切換

If/Else Switch 節點會根據布林條件在兩個可能的輸入之間進行選擇。當 `switch` 啟用（true）時，會將 `on_true` 輸入傳遞至輸出；當停用（false）時，則傳遞 `on_false`。這些輸入是惰性的，因此只會評估被選取的分支，另一個輸入不需要連接。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `切換` | 一個布林條件，決定哪個輸入會傳遞至輸出。啟用（true）時，會選取 `on_true` 輸入。停用（false）時，會選取 `on_false` 輸入。 | BOOLEAN | 是 |  |
| `為假時` | 當 `switch` 停用（false）時要傳遞至輸出的資料。只有在 `switch` 為 false 時才會要求此輸入。 | MATCH_TYPE | 否 |  |
| `為真時` | 當 `switch` 啟用（true）時要傳遞至輸出的資料。只有在 `switch` 為 true 時才會要求此輸入。 | MATCH_TYPE | 否 |  |

**輸入需求注意事項：** `on_false` 和 `on_true` 輸入是有條件地要求。節點只會在 `switch` 為 true 時要求 `on_true`，且只會在 `switch` 為 false 時要求 `on_false`。兩個輸入都必須具有相同的資料類型，且該類型必須與輸出的資料類型相符。如果選取的輸入未連接，節點將不會輸出任何值。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `output` | 選取的資料：當 `switch` 為 true 時來自 `on_true` 的值，或當 `switch` 為 false 時來自 `on_false` 的值。 | MATCH_TYPE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `42c442efeda0197d950702c52647233dee1a30216fb07e1ce4bc844784a6c5f2`
