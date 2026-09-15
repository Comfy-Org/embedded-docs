# SamplerSEEDS2

此節點提供用於影像生成的可設定取樣器。它基於隨機微分方程（SDE）求解器，並可依其設定表現得像多個特定取樣器，包括 `seeds_2`、`exp_heun_2_x0` 與 `exp_heun_2_x0_sde`。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `solver_type` | 選擇取樣器的底層求解器演算法。 | COMBO | 是 | "phi_1"<br>"phi_2" |
| `eta` | 隨機強度（預設：1.0）。 | FLOAT | 否 | 0.0 - 100.0 |
| `s_noise` | SDE 雜訊乘數（預設：1.0）。 | FLOAT | 否 | 0.0 - 100.0 |
| `r` | 中間階段（c2 節點）的相對步長（預設：0.5）。 | FLOAT | 否 | 0.01 - 1.0 |

**注意：** 節點描述定義了以下取樣器預設：
- `seeds_2`：預設設定
- `exp_heun_2_x0`：`solver_type` = "phi_2", `r` = 1.0, `eta` = 0.0
- `exp_heun_2_x0_sde`：`solver_type` = "phi_2", `r` = 1.0, `eta` = 1.0, `s_noise` = 1.0

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `sampler` | 已設定的取樣器物件，可傳遞給其他取樣節點。 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSEEDS2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f48744a706a49ef93d41845bf8c308af971853f6150afd00ded45f0317ffc4f9`
