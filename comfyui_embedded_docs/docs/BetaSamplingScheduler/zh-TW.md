# BetaSamplingScheduler

BetaSamplingScheduler 節點會產生一系列雜訊等級（sigmas），用於控制影像生成過程中取樣階段的雜訊移除方式。它採用 beta 排程演算法，其中 `alpha` 與 `beta` 設定可調整雜訊排程的形狀。產生的 sigmas 會傳遞給取樣器，以引導去噪過程。

## 輸入

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於取樣的模型，提供模型取樣物件。 | MODEL | 是 | - |
| `steps` | 要為其產生 sigmas 的取樣步數（預設值：20）。 | INT | 是 | 1 至 10000 |
| `alpha` | Beta 排程器的 Alpha 參數，控制排程曲線（預設值：0.6）。進階參數。 | FLOAT | 是 | 0.0 至 50.0 |
| `beta` | Beta 排程器的 Beta 參數，控制排程曲線（預設值：0.6）。進階參數。 | FLOAT | 是 | 0.0 至 50.0 |

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
| --- | --- | --- |
| `SIGMAS` | 用於取樣過程的一系列雜訊等級（sigmas）。 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BetaSamplingScheduler/zh-TW.md)

---
**Source fingerprint (SHA-256):** `80adae3cbedff7fe544a1fbcf638af7965f1216e422931063ecf67da53ddff95`
