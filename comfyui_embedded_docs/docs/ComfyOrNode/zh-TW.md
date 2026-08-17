# Or

ComfyOrNode 會對一組輸入值執行邏輯 OR 運算。根據 Python 的標準真假值（truthiness）規則，如果任何提供的值被視為真值（truthy），此節點將回傳 `true`。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `value` | 要評估真假值的數值。您可以透過新增更多輸入來提供多個數值。如果任何一個數值為真值（truthy），此節點將回傳 `true`。 | ANY | 是 | 最小值 1 個值；可接受多個值 |

**注意：** 此節點至少接受 1 個輸入值。您可以根據需要使用自動增長功能新增更多輸入。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `BOOLEAN` | 如果任何輸入值為真值（truthy），則回傳 `true`；如果所有輸入值皆為假值（falsy），則回傳 `false`。 | BOOLEAN |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyOrNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f673aa2b0d754f55c51ba9c9ceea7d9de9a21d2e7308bd1281b4d4461243e4ad`
