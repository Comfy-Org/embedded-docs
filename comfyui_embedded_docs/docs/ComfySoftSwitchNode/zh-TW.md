# ComfySoftSwitchNode

Soft Switch 節點根據布林條件在兩個可能的輸入值之間進行選擇。當 `switch` 為 true 時，它輸出 `on_true` 輸入的值；當 `switch` 為 false 時，它輸出 `on_false` 輸入的值。此節點設計為惰性運算，意即它只會根據 switch 狀態評估所需的輸入。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `switch` | 決定要傳遞哪個輸入的布林條件。當為 true 時，選擇 `on_true` 輸入。當為 false 時，選擇 `on_false` 輸入。 | BOOLEAN | Yes | true<br>false |
| `on_false` | 當 `switch` 條件為 false 時要輸出的值。此輸入為選用，但 `on_false` 或 `on_true` 至少需連接其中一個。 | MATCH_TYPE | No |  |
| `on_true` | 當 `switch` 條件為 true 時要輸出的值。此輸入為選用，但 `on_false` 或 `on_true` 至少需連接其中一個。 | MATCH_TYPE | No |  |

**注意：**`on_false` 與 `on_true` 輸入必須具有相同的資料類型，如節點內部模板所定義。此兩個輸入至少需連接一個，節點才能運作。如果僅連接一個輸入，則無論 `switch` 狀態為何，該值都會傳遞到輸出。

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 選取的值。它將符合所連接的 `on_false` 或 `on_true` 輸入的資料類型。 | MATCH_TYPE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7bf4bed69d8fd8c360e971ab8068382cd8ebaa02004d5df44312977a7309ae00`
