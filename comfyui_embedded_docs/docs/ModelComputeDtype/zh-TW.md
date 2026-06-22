# ModelComputeDtype

## 概述

ModelComputeDtype 節點會變更模型在處理過程中所使用的計算資料類型（精確度）。它會建立輸入模型的副本，並套用所選的精確度設定，這有助於根據您的硬體最佳化記憶體使用量與效能。此功能對於除錯和測試不同的精確度配置非常有用。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用新計算資料類型的輸入模型 | MODEL | 是 | - |
| `dtype` | 要套用至模型的計算資料類型（預設值："default"） | STRING | 是 | "default"<br>"fp32"<br>"fp16"<br>"bf16" |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用新計算資料類型的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelComputeDtype/zh-TW.md)

---
**Source fingerprint (SHA-256):** `bc65f1e452d0122ad175a8b95f38a36503253c9908157037c516496e65c828e6`
