# Perp-Neg（已被 PerpNegGuider 棄用）

## 概述

PerpNeg 節點將垂直負向引導應用於模型的取樣過程。此節點會修改模型的配置函數，以使用負向條件和縮放因子調整雜訊預測。此節點已棄用，並由 PerpNegGuider 節點取代以提供更佳功能。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用垂直負向引導的模型 | MODEL | 是 | - |
| `empty_conditioning` | 用於負向引導計算的空條件 | CONDITIONING | 是 | - |
| `neg_scale` | 負向引導的縮放因子（預設值：1.0） | FLOAT | 否 | 0.0 - 100.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用垂直負向引導的修改後模型 | MODEL |

**注意**：此節點已棄用，並已由 PerpNegGuider 取代。它被標記為實驗性功能，不應用於生產工作流程。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNeg/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6be4ab03cfbda33ed3966ecd579c1a5e3242bdfb163fecefb9c80073a8827cae`
