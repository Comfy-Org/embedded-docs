# 切換

Switch 節點會根據布林條件在兩個可能的輸入之間進行選擇。當 `switch` 啟用時，輸出 `on_true` 輸入；當 `switch` 停用時，輸出 `on_false` 輸入，讓您能夠建立條件邏輯，在工作流程中選擇不同的資料路徑。此節點目前標記為實驗性功能。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | Range |
| --- | --- | --- | --- | --- |
| `switch` | 決定要傳遞哪個輸入的布林條件。啟用（true）時，會選取 `on_true` 輸入。停用（false）時，會選取 `on_false` 輸入。 | BOOLEAN | 是 |  |
| `on_false` | 當 `switch` 停用（false）時要傳遞到輸出的資料。此輸入僅在 `switch` 為 false 時為必填。 | MATCH_TYPE | 否 |  |
| `on_true` | 當 `switch` 啟用（true）時要傳遞到輸出的資料。此輸入僅在 `switch` 為 true 時為必填。 | MATCH_TYPE | 否 |  |

**輸入需求說明：** `on_false` 和 `on_true` 輸入是條件性必填。節點只會在 `switch` 為 true 時要求 `on_true` 輸入，並只在 `switch` 為 false 時要求 `on_false` 輸入。兩個輸入必須具有相同的資料類型。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 選取的資料。如果 `switch` 為 true，則為 `on_true` 輸入的值；如果 `switch` 為 false，則為 `on_false` 輸入的值。 | MATCH_TYPE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d0adda02e7f997f27182cb26e11e934660ae5bd80f3091bed2fed7c981632ce5`
