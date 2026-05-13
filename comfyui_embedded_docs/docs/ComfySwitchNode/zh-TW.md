> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/zh-TW.md)

## 概述

Switch 節點根據布林條件在兩個可能的輸入之間進行選擇。當 `switch` 啟用時，它會輸出 `on_true` 輸入；當 `switch` 停用時，則輸出 `on_false` 輸入。這讓您能夠建立條件邏輯，並在工作流程中選擇不同的資料路徑。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `switch` | BOOLEAN | 是 | | 決定傳遞哪個輸入的布林條件。啟用（true）時，選擇 `on_true` 輸入。停用（false）時，選擇 `on_false` 輸入。 |
| `on_false` | MATCH_TYPE | 否 | | 當 `switch` 停用（false）時，傳遞至輸出的資料。此輸入僅在 `switch` 為 false 時為必要。 |
| `on_true` | MATCH_TYPE | 否 | | 當 `switch` 啟用（true）時，傳遞至輸出的資料。此輸入僅在 `switch` 為 true 時為必要。 |

**關於輸入必要性的說明：** `on_false` 和 `on_true` 輸入是條件性必要的。節點僅在 `switch` 為 true 時要求 `on_true` 輸入，僅在 `switch` 為 false 時要求 `on_false` 輸入。兩個輸入必須為相同的資料類型。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | MATCH_TYPE | 被選取的資料。如果 `switch` 為 true，則為 `on_true` 輸入的值；如果 `switch` 為 false，則為 `on_false` 輸入的值。 |

---
**Source fingerprint (SHA-256):** `9f3cf58c1a04116fa0cbe8007fe3ed90e93c4de2e65f6778761d03fb21a63af3`
