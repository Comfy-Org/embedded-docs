# SamplerSEEDS2

## 概述

此節點提供一個可配置的取樣器，用於生成圖像。它實作了 SEEDS-2 演算法，這是一種隨機微分方程 (SDE) 求解器。透過調整其參數，您可以將其配置為類似多種特定取樣器的行為，包括 `seeds_2`、`exp_heun_2_x0` 和 `exp_heun_2_x0_sde`。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `solver_type` | 選擇取樣器的底層求解器演算法。 | COMBO | 是 | `"phi_1"`<br>`"phi_2"` |
| `eta` | 隨機強度（預設值：1.0）。 | FLOAT | 否 | 0.0 - 100.0 |
| `s_noise` | SDE 噪聲倍數（預設值：1.0）。 | FLOAT | 否 | 0.0 - 100.0 |
| `r` | 中間階段（c2 節點）的相對步長（預設值：0.5）。 | FLOAT | 否 | 0.01 - 1.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `sampler` | 一個已配置的取樣器物件，可傳遞給其他取樣節點。 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSEEDS2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `13cfc064dab8b77dbdfdc27238130bdf3dc6c1eca47110f4a7f7d6b8c2866b90`
