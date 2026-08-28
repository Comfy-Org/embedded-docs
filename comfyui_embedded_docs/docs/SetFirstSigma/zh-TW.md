# SetFirstSigma

SetFirstSigma 節點通過僅將序列中的第一個值替換為自訂 sigma 值來更改 sigma 序列。它接收現有的 sigma 序列和一個新的 sigma 值，然後返回一個新的 sigma 序列，其中除了第一個值之外的所有值保持不變。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `sigmas` | 要修改的 sigma 值輸入序列 | SIGMAS | 是 | - |
| `sigma` | 要設定為序列中第一個元素的新 sigma 值（預設值：136.0） | FLOAT | 是 | 0.0 至 20000.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `sigmas` | 修改後的 sigma 序列，其中第一個元素已替換為自訂 sigma 值 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetFirstSigma/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5302bc61a7ca094fee9ee2ad8c9dc32997ef0bbf27c9945acd7287e7df6b6db3`
