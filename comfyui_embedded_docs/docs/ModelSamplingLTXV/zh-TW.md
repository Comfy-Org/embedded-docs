## 概述

ModelSamplingLTXV 節點根據 token 數量對模型套用進階取樣參數。它透過基礎偏移值與最大偏移值之間的線性插值計算偏移值，計算結果取決於輸入潛在空間中的 token 數量。該節點隨後建立專門的模型取樣配置，並將其套用至輸入模型。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用取樣參數的輸入模型 | MODEL | 是 | - |
| `最大偏移` | 線性插值計算中使用的最大偏移值（預設值：2.05） | FLOAT | 是 | 0.0 至 100.0 |
| `基礎偏移` | 線性插值計算中使用的基礎偏移值（預設值：0.95） | FLOAT | 是 | 0.0 至 100.0 |
| `潛在空間` | 可選的潛在空間輸入，用於決定偏移計算的 token 數量。若未提供，則使用預設的 4096 個 token 數量 | LATENT | 否 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用取樣參數的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2325754df1b2541a6adbdebecefde92e08535af0e179d7444093a61eb35cb24c`
