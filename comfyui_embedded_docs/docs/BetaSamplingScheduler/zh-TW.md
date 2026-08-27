# BetaSamplingScheduler

BetaSamplingScheduler 節點使用 beta 調度演算法，為取樣過程生成一系列噪聲級別（sigma）。它接受一個模型和配置參數，以建立自訂的噪聲排程，控制影像生成期間的去噪過程。此調度器可透過 alpha 和 beta 參數微調噪聲降低軌跡。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於取樣的模型，提供模型取樣物件 | MODEL | 是 | - |
| `步驟數` | 要為其生成 sigma 的取樣步數（預設值：20） | INT | 是 | 1 至 10000 |
| `alpha` | beta 調度器的 Alpha 參數，控制調度曲線（預設值：0.6，進階參數） | FLOAT | 是 | 0.0 至 50.0 |
| `beta` | beta 調度器的 Beta 參數，控制調度曲線（預設值：0.6，進階參數） | FLOAT | 是 | 0.0 至 50.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `SIGMAS` | 用於取樣過程的一系列噪聲級別（sigma） | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BetaSamplingScheduler/zh-TW.md)

---
**Source fingerprint (SHA-256):** `80adae3cbedff7fe544a1fbcf638af7965f1216e422931063ecf67da53ddff95`
