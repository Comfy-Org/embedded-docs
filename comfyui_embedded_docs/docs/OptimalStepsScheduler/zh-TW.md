# 最佳步數排程器

OptimalStepsScheduler 節點會根據所選的模型類型與步數設定，計算擴散模型的雜訊排程 sigma 值。它會依照 `denoise` 參數調整總步數，並內插雜訊等級以符合指定的步數。此節點會傳回一系列 sigma 值，這些值決定了擴散取樣過程中所使用的雜訊等級。

## 輸入
| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model_type` | 用於雜訊等級計算的擴散模型類型 | COMBO | 是 | "FLUX"<br>"Wan"<br>"Chroma" |
| `steps` | 要計算的取樣步驟總數（預設值：20） | INT | 是 | 3-1000 |
| `denoise` | 控制去噪強度，用以調整有效步數（預設值：1.0） | FLOAT | 是 | 0.0-1.0 |

**注意：** 當 `denoise` 設定為小於 1.0 時，節點會將有效步數計算為 `steps * denoise`。如果 `denoise` 設定為 0.0，節點會傳回空的張量。

## 輸出
| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `sigmas` | 一系列 sigma 值，代表擴散取樣的雜訊排程 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OptimalStepsScheduler/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fd48c94ca16c8a3d8e6f0138018e7b13c15d100d6147807bcb23d838899045b7`
