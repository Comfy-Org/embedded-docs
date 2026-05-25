> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNotNode/zh-TW.md)

## 概述

Not 節點對任何輸入值執行邏輯 NOT 運算。如果輸入值被視為假值（例如 0、空字串、None、False），則回傳 True；如果輸入值為真值，則回傳 False。此節點使用 Python 的標準規則來判斷真值。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `value` | ANY | 是 | 任何值 | 要進行反轉的輸入值。接受任何資料類型，並使用 Python 的真值規則進行評估。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | BOOLEAN | 輸入值的邏輯反轉。如果輸入為假值則回傳 True，如果輸入為真值則回傳 False。 |

---
**Source fingerprint (SHA-256):** `fd8f940218538fce28079bc836379703c0e3c04f80351520497855c464176877`
