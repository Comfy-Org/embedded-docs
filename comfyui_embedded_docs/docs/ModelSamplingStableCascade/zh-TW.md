# 模型取樣 Stable Cascade

## 概述

ModelSamplingStableCascade 節點透過調整帶有偏移值的取樣參數，將穩定級聯取樣應用於模型。它會建立一個具有自訂取樣配置的輸入模型修改版本，以實現穩定級聯生成。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用穩定級聯取樣的輸入模型 | MODEL | 是 | - |
| `偏移` | 套用至取樣參數的偏移值（預設值：2.0） | FLOAT | 是 | 0.0 - 100.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用穩定級聯取樣的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2d0a342fff05434c8fe78999187bd31dbee7deb6f4447759a489102a8ce277de`
