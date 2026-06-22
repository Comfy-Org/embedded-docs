# SamplerLCM

## 概述

SamplerLCM 節點提供了一個具有可調每步雜訊參數的 LCM（潛在一致性模型）取樣器。它讓您能夠控制每個取樣步驟中應用的雜訊，從而實現對取樣過程的精細調整。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `s_noise` | 第一步的每步雜訊乘數。值為 1.0 時與模型的訓練雜訊規模一致。(預設值: 1.0) | FLOAT | 是 | 0.0 至 64.0 (步長: 0.01) |
| `s_noise_end` | 最後一步的每步雜訊乘數。設定為與 `s_noise` 相同可獲得恆定的雜訊排程。(預設值: 1.0) | FLOAT | 是 | 0.0 至 64.0 (步長: 0.01) |
| `noise_clip_std` | 將每步雜訊限制在 +/- N 個標準差範圍內。值為 0 時停用限制。(預設值: 0.0) | FLOAT | 是 | 0.0 至 10.0 (步長: 0.01) |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `SAMPLER` | 配置完成的 LCM 取樣器物件，可直接用於取樣工作流程中。 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCM/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e6f9007f66625baeee8850018784187cf45117591c443f117c593eef547ada98`
