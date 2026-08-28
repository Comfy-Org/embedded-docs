# 分割 Sigmas（去噪）

SplitSigmasDenoise 節點會根據去噪強度參數，將一組 sigma 值序列分割成兩個部分。它會將輸入的 sigma 分割為高 sigma 與低 sigma 序列，分割點的決定方式是將總步數乘以去噪因子。如此便能將噪聲調度分離成不同的強度範圍，以進行專業化處理。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `sigmas` | 代表噪聲調度的 sigma 值輸入序列 | SIGMAS | 是 | - |
| `去雜訊強度` | 決定 sigma 序列分割位置的去噪強度因子（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `高 sigma` | 包含較高 sigma 值的 sigma 序列第一部分 | SIGMAS |
| `低 sigma` | 包含較低 sigma 值的 sigma 序列第二部分 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmasDenoise/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6198cdbc07b5c9aacf1137a5d6350e090ffd14050abbcc37ff79ff5e975a8c20`
