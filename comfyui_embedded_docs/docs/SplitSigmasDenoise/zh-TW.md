# 分割 Sigmas（去噪）

SplitSigmasDenoise 節點會根據去噪強度參數，將一系列 sigma 值分割成兩部分。它會將輸入的 sigma 分割成高 sigma 序列與低 sigma 序列，分割點由總步數（比 sigma 值數量少一）乘以 `denoise` 因子決定。這可讓噪聲排程被分離成不同強度範圍，以進行專門處理。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `sigmas` | 輸入的 sigma 值序列，代表噪聲排程 | SIGMAS | 是 | - |
| `去雜訊強度` | 決定 sigma 序列分割位置的去噪強度係數（預設：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `high_sigmas` | sigma 序列的第一部分，包含直到分割點前較高的 sigma 值 | SIGMAS |
| `low_sigmas` | sigma 序列的第二部分，包含從分割點起較低的 sigma 值 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmasDenoise/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6198cdbc07b5c9aacf1137a5d6350e090ffd14050abbcc37ff79ff5e975a8c20`
