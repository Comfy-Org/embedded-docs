# SamplerLCM

SamplerLCM 節點提供了一個具有可調每步雜訊參數的 LCM（潛在一致性模型）取樣器。它讓您可以控制取樣過程中每一步所應用的雜訊；`s_noise` 是模型訓練雜訊尺度的乘數。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `s_noise` | 第一步的每步雜訊乘數（1.0 = 符合訓練）。預設值：1.0 | FLOAT | 是 | 0.0 至 64.0（步長：0.01） |
| `s_noise_end` | 最後一步的每步雜訊乘數。設定為與 `s_noise` 相同即可使用恆定雜訊排程。預設值：1.0 | FLOAT | 是 | 0.0 至 64.0（步長：0.01） |
| `noise_clip_std` | 將每步雜訊限制在 +/- N*std 範圍內。設為 0 則停用。預設值：0.0 | FLOAT | 是 | 0.0 至 10.0（步長：0.01） |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `SAMPLER` | 已設定的 LCM 取樣器物件，可直接用於取樣工作流程。 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCM/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0d18f2f977ddadeedcd7807233b48ebcc4e94c6213f8540b9037a45a9c70c6cf`
