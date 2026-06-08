## 概述

SamplerER_SDE 節點為擴散模型提供專門的取樣方法，提供不同的求解器類型，包括 ER-SDE、反向時間 SDE 和 ODE 方法。它允許控制取樣過程中的隨機行為和計算階段。該節點會根據所選的求解器類型自動調整參數，以確保正常功能。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `solver_type` | 用於取樣的求解器類型。決定擴散過程的數學方法。 | COMBO | 是 | "ER-SDE"<br>"Reverse-time SDE"<br>"ODE" |
| `max_stage` | 取樣過程的最大階段數（預設值：3）。控制計算複雜度和品質。 | INT | 否 | 1-3 |
| `eta` | 反向時間 SDE 的隨機強度（預設值：1.0）。當 eta=0 時，會簡化為確定性 ODE。此設定不適用於 ER-SDE 求解器類型。 | FLOAT | 否 | 0.0-100.0 |
| `s_noise` | 取樣過程的噪聲縮放因子（預設值：1.0）。控制取樣過程中應用的噪聲量。 | FLOAT | 否 | 0.0-100.0 |

**參數限制：**

- 當 `solver_type` 設定為 "ODE" 或使用 `eta`=0 的 "Reverse-time SDE" 時，無論使用者輸入值為何，`eta` 和 `s_noise` 都會自動設定為 0。
- `eta` 參數僅影響 "Reverse-time SDE" 求解器類型，對 "ER-SDE" 求解器類型無效。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `sampler` | 一個已配置的取樣器物件，可用於取樣流程中，並帶有指定的求解器設定。 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerER_SDE/zh-TW.md)

---
**Source fingerprint (SHA-256):** `bc24ec3c5dc645aebf55ef3392c5f4a40dcf0461b4b77731e8fe7ff397dcfadf`
