# ComfySoftSwitchNode

Soft Switch 節點會根據布林條件在兩個可能的輸入值之間進行選擇。當 `switch` 為 true 時，輸出 `on_true` 輸入的值；當 `switch` 為 false 時，輸出 `on_false` 輸入的值。此節點設計為惰性（lazy）運算，意思是它只會根據 switch 狀態評估所需的輸入。

## 輸入

| 參數 | 說明 | 資料型態 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `switch` | 決定要傳遞哪個輸入的布林條件。當為 true 時，選取 `on_true` 輸入；當為 false 時，選取 `on_false` 輸入。 | BOOLEAN | 是 | True 或 False |
| `on_false` | 當 `switch` 條件為 false 時要輸出的值。此輸入為選用，但 `on_false` 或 `on_true` 至少需連接其中一個。 | MATCH_TYPE | 否 | 與 `on_true` 相同的資料型態 |
| `on_true` | 當 `switch` 條件為 true 時要輸出的值。此輸入為選用，但 `on_false` 或 `on_true` 至少需連接其中一個。 | MATCH_TYPE | 否 | 與 `on_false` 相同的資料型態 |

**注意：** `on_false` 與 `on_true` 輸入必須具有相同的資料型態，此由節點內部範本定義。這兩個輸入至少需連接一個，節點才能運作。由於節點是惰性的，當只連接一個輸入時，無論 `switch` 狀態為何，節點都會一律輸出該輸入的值。

## 輸出

| 輸出名 | 說明 | 資料型態 |
| --- | --- | --- |
| `output` | 選取後的值。其資料型態會與已連接的 `on_false` 或 `on_true` 輸入相符。當兩個輸入都連接時，若 `switch` 為 true 則輸出 `on_true`，若 `switch` 為 false 則輸出 `on_false`。 | MATCH_TYPE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7bf4bed69d8fd8c360e971ab8068382cd8ebaa02004d5df44312977a7309ae00`
