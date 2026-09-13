# Not

Not 節點會對任何輸入值執行邏輯 NOT 運算。當輸入值被視為假值（例如 0、空字串、None 或 False）時，它會傳回 True；當輸入值為真值時，它會傳回 False，並遵循 Python 的標準真值判斷規則。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `value` | 要反轉的輸入值。接受任何資料類型，並使用 Python 的真值判斷規則進行評估。 | ANY | 是 | Any value |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `output` | 輸入值的邏輯反相。若輸入為假值則傳回 True，若輸入為真值則傳回 False。 | BOOLEAN |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNotNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `24bbe667a0800b187d991b24894794e2ce710256200a2667ff391c1e644963a5`
