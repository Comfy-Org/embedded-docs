> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveFloat/zh-TW.md)

## 概述

PrimitiveFloat 節點會建立一個可在工作流程中使用的浮點數值。它接受單一數值輸入，並輸出相同的數值，讓您能夠在 ComfyUI 流程中定義並在不同節點之間傳遞浮點數值。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `數值` | FLOAT | 是 | -sys.maxsize 至 sys.maxsize（步長：0.1） | 要輸出的浮點數值（預設值：0.0） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | FLOAT | 輸入的浮點數值 |

---
**Source fingerprint (SHA-256):** `a12473ac0efac903249f249770bec92a562b1ef6dede45fc0296e0e397a0754f`
