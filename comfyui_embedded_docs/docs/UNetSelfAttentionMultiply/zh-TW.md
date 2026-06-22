# UNet 自注意力倍增

## 概述

UNetSelfAttentionMultiply 節點會對 UNet 模型中的自注意力機制中的查詢、鍵、值和輸出元件套用乘法因子。它允許您縮放注意力計算的不同部分，以實驗注意力權重如何影響模型的行為。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要透過注意力縮放因子修改的 UNet 模型 | MODEL | 是 | - |
| `q` | 查詢元件的乘法因子（預設值：1.0） | FLOAT | 否 | 0.0 - 10.0 |
| `k` | 鍵元件的乘法因子（預設值：1.0） | FLOAT | 否 | 0.0 - 10.0 |
| `v` | 值元件的乘法因子（預設值：1.0） | FLOAT | 否 | 0.0 - 10.0 |
| `out` | 輸出元件的乘法因子（預設值：1.0） | FLOAT | 否 | 0.0 - 10.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `MODEL` | 已套用縮放注意力元件的修改後 UNet 模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetSelfAttentionMultiply/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ee6328c6cba44d30d2e219a2af04bb3d3d9adeaabb959a46f87b3b299dfe2f43`
