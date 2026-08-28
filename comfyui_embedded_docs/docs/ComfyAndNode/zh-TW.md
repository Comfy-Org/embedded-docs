# And

And 節點對一組輸入值執行邏輯 AND 運算。僅當所有提供的值皆依據 Python 的真值規則判定為真時，才會傳回 `true`。此節點常用於確認多個條件全部成立後再繼續執行。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `values` | 要評估的值。節點至少接受一個值，您可以透過點擊節點上的「+」按鈕來新增更多值。接受任何資料類型。 | ANY | 是 | 1 個或以上（無上限） |

**注意：** 此節點使用 Python 的真值規則來判斷值為 `true` 或 `false`。例如，空字串、數字 0、空清單及 `None` 皆視為 `false`。所有其他值則視為 `true`。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `BOOLEAN` | 若所有輸入值皆為真，則傳回 `true`，否則傳回 `false`。 | BOOLEAN |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyAndNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e7359c46da62f9859ea4f4a239cf20c565b5f7de22d280afc00c7ca321f1c89d`
