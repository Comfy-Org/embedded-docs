# SplitSigmasDenoise 節點

SplitSigmasDenoise 節點根據去噪強度參數將 sigma 值序列分割為兩個部分。它將輸入的 sigmas 分割為高 sigma 序列和低 sigma 序列，分割點由總步數乘以去噪因子決定。這允許將噪聲調度分離到不同的強度範圍以進行專門處理。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `sigmas` | 代表噪聲調度的 sigma 值輸入序列 | SIGMAS | 是 | - |
| `去雜訊強度` | 決定 sigma 序列分割點的去噪強度因子（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `低 sigma` | 包含較高 sigma 值的 sigma 序列第一部分 | SIGMAS |
| `low_sigmas` | 包含較低 sigma 值的 sigma 序列第二部分 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmasDenoise/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fda53efe2fcaed9244376b7360d8b0b76ce7395d594de4c2ecc48a8f243d7ca6`
