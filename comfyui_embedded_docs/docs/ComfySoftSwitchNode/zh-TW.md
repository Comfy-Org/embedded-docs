> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/zh-TW.md)

## 概述

軟開關節點根據布林條件在兩個可能的輸入值之間進行選擇。當 `switch` 為 true 時，輸出 `on_true` 輸入的值；當 `switch` 為 false 時，輸出 `on_false` 輸入的值。此節點設計為惰性求值，意味著它只會根據開關狀態評估所需的輸入。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `switch` | BOOLEAN | 是 | | 決定傳遞哪個輸入的布林條件。當為 true 時，選取 `on_true` 輸入。當為 false 時，選取 `on_false` 輸入。 |
| `on_false` | MATCH_TYPE | 否 | | 當 `switch` 條件為 false 時輸出的值。此輸入為選填，但 `on_false` 或 `on_true` 至少需連接其中一個。 |
| `on_true` | MATCH_TYPE | 否 | | 當 `switch` 條件為 true 時輸出的值。此輸入為選填，但 `on_false` 或 `on_true` 至少需連接其中一個。 |

**注意：** `on_false` 和 `on_true` 輸入必須為相同的資料類型，由節點內部模板定義。節點運作時，這兩個輸入至少需連接其中一個。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | MATCH_TYPE | 選取的值。其資料類型將與已連接的 `on_false` 或 `on_true` 輸入保持一致。 |

---
**Source fingerprint (SHA-256):** `f5e40e7f43948b81b5442c885c3e1ff15e38f8f7ddda00ef3be42225765bfd1c`
