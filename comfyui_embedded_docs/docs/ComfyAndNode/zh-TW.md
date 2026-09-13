# And

And 節點會對一組輸入值執行邏輯 AND 運算。只有在所有已連接的值根據 Python 的真值規則都被視為 truthy 時，它才會回傳 `true`；這使其適合用來檢查多個條件是否同時全部成立。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `values` | 可擴充的一組待評估值。節點一開始會有一個 slot，你可以點擊節點上的「+」按鈕來新增更多 slot。接受任何資料類型。 | ANY | 是 | 最小 1（無上限） |

**注意：** 此輸入是可擴充的 slot 群組。Slot 會逐一新增（例如 `value_1`、`value_2` 等），且至少必須有一個 slot。

**注意：** 此節點使用 Python 的真值規則來判斷值是 `true` 還是 `false`。例如，空字串、數字 0、空列表和 `None` 都會被視為 `false`。所有其他值都會被視為 `true`。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `BOOLEAN` | 若所有輸入值皆為真（truthy），則回傳 `true`；否則回傳 `false`。 | BOOLEAN |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyAndNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e7359c46da62f9859ea4f4a239cf20c565b5f7de22d280afc00c7ca321f1c89d`
