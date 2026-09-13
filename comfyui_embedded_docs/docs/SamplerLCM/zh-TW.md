# SamplerLCM

此節點提供一個可調整每步雜訊的 LCM（Latent Consistency Model，潛在一致性模型）取樣器。它讓您能控制取樣過程中套用的雜訊量：`s_noise` 可作為模型訓練雜訊尺度的乘數，而雜訊程度可以從第一步到最後一步有所變化。設定完成的取樣器接著便可接入取樣工作流程中使用。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `s_noise` | 第一步的每步雜訊乘數（1.0 = 符合訓練設定）。預設值：1.0。 | FLOAT | 是 | 0.0 至 64.0 （步進值：0.01） |
| `s_noise_end` | 最後一步的每步雜訊乘數。設為與 `s_noise` 相同可維持固定排程。預設值：1.0。 | FLOAT | 是 | 0.0 至 64.0 （步進值：0.01） |
| `noise_clip_std` | 將每步雜訊限制在 +/- N*std 範圍內。設為 0 表示停用。預設值：0.0。 | FLOAT | 是 | 0.0 至 10.0 （步進值：0.01） |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `SAMPLER` | 設定完成的 LCM 取樣器物件，可直接用於取樣工作流程中。 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCM/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0d18f2f977ddadeedcd7807233b48ebcc4e94c6213f8540b9037a45a9c70c6cf`
