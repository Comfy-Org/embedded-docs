# And

此節點對一組輸入值執行邏輯 AND 運算。僅當所有提供的值根據 Python 的真值規則都被視為 `true` 時，它才會回傳 `true`。此節點可用於在繼續之前檢查是否同時滿足多個條件。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `values` | 一個可擴充的值列表，用於評估。節點至少需要一個值，您可以透過點擊節點上的「+」按鈕來新增更多插槽。每個插槽接受任何資料類型。 | ANY | 是 | 1 個或多個值 |

**注意：** 此節點使用 Python 的真值規則來判斷值為 `true` 或 `false`。例如，空字串、數字 0、空清單和 `None` 都被視為 `false`。所有其他值都被視為 `true`。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `BOOLEAN` | 如果所有輸入值皆為真，則回傳 `true`，否則回傳 `false`。 | BOOLEAN |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyAndNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e7359c46da62f9859ea4f4a239cf20c565b5f7de22d280afc00c7ca321f1c89d`
