# SamplerSEEDS2

此節點提供了一個用於圖像生成的可配置採樣器。它實現了SEEDS-2算法，這是一種隨機微分方程（SDE）求解器。透過調整其參數，您可以將其配置為類似於幾個特定採樣器的行為，包括`seeds_2`、`exp_heun_2_x0`和`exp_heun_2_x0_sde`。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `solver_type` | 為採樣器選擇底層求解器算法。 | COMBO | 是 | "phi_1"<br>"phi_2" |
| `eta` | 隨機強度（預設值：1.0）。 | FLOAT | 否 | 0.0 - 100.0 |
| `s_noise` | SDE 雜訊倍數（預設值：1.0）。 | FLOAT | 否 | 0.0 - 100.0 |
| `r` | 中間階段（c2 節點）的相對步長（預設值：0.5）。 | FLOAT | 否 | 0.01 - 1.0 |

**注意：** 節點描述定義了以下採樣器預設：
- `seeds_2`：預設設定
- `exp_heun_2_x0`：`solver_type` = "phi_2"，`r` = 1.0，`eta` = 0.0
- `exp_heun_2_x0_sde`：`solver_type` = "phi_2"，`r` = 1.0，`eta` = 1.0，`s_noise` = 1.0

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `sampler` | 一個已配置的採樣器物件，可傳遞給其他採樣節點。 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSEEDS2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f48744a706a49ef93d41845bf8c308af971853f6150afd00ded45f0317ffc4f9`
