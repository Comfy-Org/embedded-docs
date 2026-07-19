# And

## 概述

And 節點對一組輸入值執行邏輯 AND 運算。僅當所有提供的值根據 Python 的真值規則都被視為真值時，才會回傳 `true`。此節點適用於在繼續執行前檢查多個條件是否全部滿足。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `values` | 要評估的值列表。此節點至少接受一個值，您可以透過點擊節點上的「+」按鈕來新增更多值。 | ANY | 是 | 1 個或多個值 |

**注意：** 此節點使用 Python 的真值規則來判斷值為 `true` 或 `false`。例如，空字串、數字 0、空列表和 `None` 都被視為 `false`。所有其他值都被視為 `true`。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `BOOLEAN` | 如果所有輸入值皆為真值則回傳 `true`，否則回傳 `false`。 | BOOLEAN |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyAndNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fd9d18ce698472a7e35ad3082f2ccff8ae264b11bd887a498f929cd877ff38c4`
