# UNet 交叉注意力倍增

## 概述

UNetCrossAttentionMultiply 節點將乘法因子應用於 UNet 模型中的交叉注意力機制。它允許您縮放交叉注意力層中的查詢、鍵、值和輸出組件，以實驗不同的注意力行為和效果。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要透過注意力縮放因子修改的 UNet 模型 | MODEL | 是 | - |
| `q` | 交叉注意力中查詢組件的縮放因子（預設值：1.0） | FLOAT | 否 | 0.0 - 10.0 |
| `k` | 交叉注意力中鍵組件的縮放因子（預設值：1.0） | FLOAT | 否 | 0.0 - 10.0 |
| `v` | 交叉注意力中值組件的縮放因子（預設值：1.0） | FLOAT | 否 | 0.0 - 10.0 |
| `out` | 交叉注意力中輸出組件的縮放因子（預設值：1.0） | FLOAT | 否 | 0.0 - 10.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已修改的 UNet 模型，其交叉注意力組件已套用縮放 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetCrossAttentionMultiply/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2623858c11e93ab5952194670c9e4ea74bba4e2ea32089540665eea361dc1491`
