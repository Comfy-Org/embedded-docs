# CFG 正規化

## 概述

CFGNorm 節點對擴散模型中的無分類器引導（CFG）過程應用正規化技術。它透過比較條件輸出與非條件輸出的範數來調整去噪預測的縮放比例，然後套用強度乘數來控制效果。這有助於防止引導縮放中出現極端值，從而穩定生成過程。

## 輸入

| 參數 | 說明 | 資料類型 | 輸入類型 | 預設值 | 範圍 |
| --- | --- | --- | --- | --- | --- |
| `模型` | 要套用 CFG 正規化的擴散模型 | MODEL | 必要 | - | - |
| `強度` | 控制套用於 CFG 縮放的正規化效果強度 | FLOAT | 必要 | 1.0 | 0.0 - 100.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `patched_model` | 傳回已在其取樣過程中套用 CFG 正規化的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/zh-TW.md)

---
**Source fingerprint (SHA-256):** `af9e5f965500b959ff46f781e9329524fc0a4b94af2ce6d74116fe27b0e9005e`
