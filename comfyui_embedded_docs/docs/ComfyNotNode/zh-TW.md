# Not

Not 節點對任何輸入值執行邏輯 NOT 運算。如果輸入值被視為假值（falsy）（例如 0、空字串、None 或 False），則回傳 True；如果輸入值為真值（truthy），則回傳 False。它使用 Python 的標準規則來判斷真值（truthiness）。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `value` | 要反轉的輸入值。接受任何資料類型，並使用 Python 的真值規則進行評估。 | ANY | 是 | 任意值 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 輸入值的邏輯反向。如果輸入為假值（falsy）則回傳 True；如果輸入為真值（truthy）則回傳 False。 | BOOLEAN |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNotNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `24bbe667a0800b187d991b24894794e2ce710256200a2667ff391c1e644963a5`
