# 切換

Switch 節點根據布林條件在兩個可能的輸入之間進行選擇。當 `switch` 啟用時，它輸出 `on_true` 輸入；當 `switch` 停用時，則輸出 `on_false` 輸入。僅會評估所選的分支，因此另一個輸入並非必要。這讓您能夠建立條件邏輯，並在工作流程中選擇不同的資料路徑。

## 輸入

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `切換` | 決定要傳遞哪個輸入的布林條件。啟用（true）時，會選取 `on_true` 輸入。停用（false）時，會選取 `on_false` 輸入。 | BOOLEAN | 是 |  |
| `為假時` | 當 `switch` 停用（false）時，要傳遞到輸出的資料。僅當 `switch` 為 false 時，才需要此輸入。 | MATCH_TYPE | 否 |  |
| `為真時` | 當 `switch` 啟用（true）時，要傳遞到輸出的資料。僅當 `switch` 為 true 時，才需要此輸入。 | MATCH_TYPE | 否 |  |

**關於輸入需求的說明：** `on_false` 和 `on_true` 輸入是依條件需要的。節點只會在 `switch` 為 true 時要求 `on_true` 輸入，並且只會在 `switch` 為 false 時要求 `on_false` 輸入。兩個輸入必須具有相同的資料型別，且必須符合輸出的資料型別。

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
| --- | --- | --- |
| `輸出` | 所選取的資料。如果 `switch` 為 true，則為 `on_true` 輸入的值；如果 `switch` 為 false，則為 `on_false` 輸入的值。 | MATCH_TYPE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d0adda02e7f997f27182cb26e11e934660ae5bd80f3091bed2fed7c981632ce5`
