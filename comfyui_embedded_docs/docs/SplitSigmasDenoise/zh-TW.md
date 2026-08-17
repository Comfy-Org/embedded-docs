# 分割 Sigmas（去噪）

SplitSigmasDenoise 節點會根據去雜訊強度參數，將 sigma 值序列分割成兩個部分。它將輸入的 `sigmas` 分割成高 sigma 序列與低 sigma 序列，分割點由總步數乘以去雜訊因子決定。這樣可以將雜訊排程分離成不同的強度範圍，以進行專門處理。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `sigmas` | 代表雜訊排程的 sigma 值輸入序列 | SIGMAS | 是 | - |
| `denoise` | 決定 sigma 序列分割位置的去雜訊強度因子（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |

注意：總步數為 sigma 值數目減 1。兩個輸出序列在分割點共用一個 sigma 值。當 `denoise` = 0.0 時，`high_sigmas` 為空；當 `denoise` = 1.0 時，`high_sigmas` 僅包含第一個 sigma 值，而 `low_sigmas` 包含完整序列。

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `high_sigmas` | 包含較高 sigma 值的第一部分 sigma 序列 | SIGMAS |
| `low_sigmas` | 包含較低 sigma 值的第二部分 sigma 序列 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmasDenoise/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6198cdbc07b5c9aacf1137a5d6350e090ffd14050abbcc37ff79ff5e975a8c20`
