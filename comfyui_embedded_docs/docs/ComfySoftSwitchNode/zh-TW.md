# ComfySoftSwitchNode

Soft Switch 節點根據布林條件在兩個可能的輸入值之間進行選擇。當 `switch` 為 true 時，它輸出 `on_true` 輸入的值；當 `switch` 為 false 時，它輸出 `on_false` 輸入的值。此節點採用惰性設計，表示它只會根據 switch 狀態評估實際需要的輸入。

## 輸入

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `switch` | 決定要傳遞哪個輸入的布林條件。當為 true 時，會選取 `on_true` 輸入。當為 false 時，會選取 `on_false` 輸入。 | BOOLEAN | 是 | True or False |
| `on_false` | 當 `switch` 條件為 false 時要輸出的值。此輸入為選用，但 `on_false` 或 `on_true` 至少必須連接一個。 | MATCH_TYPE | 否 | 與 `on_true` 相同的資料類型 |
| `on_true` | 當 `switch` 條件為 true 時要輸出的值。此輸入為選用，但 `on_false` 或 `on_true` 至少必須連接一個。 | MATCH_TYPE | 否 | 與 `on_false` 相同的資料類型 |

**注意：** `on_false` 和 `on_true` 輸入必須是相同的資料類型，這由節點的內部範本定義。這兩個輸入中至少要連接一個，否則節點會傳回驗證訊息 "At least one of on_false or on_true must be connected to Switch node"。因為節點是惰性的，當只連接一個輸入時，無論 `switch` 狀態為何，節點一律輸出該輸入的值。

## 輸出

| Output Name | Description | Data Type |
| --- | --- | --- |
| `output` | 選取的值。它會與已連接的 `on_false` 或 `on_true` 輸入資料類型相符。當兩個輸入都已連接時，如果 `switch` 為 true，則輸出 `on_true`；如果 `switch` 為 false，則輸出 `on_false`。 | MATCH_TYPE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7bf4bed69d8fd8c360e971ab8068382cd8ebaa02004d5df44312977a7309ae00`
