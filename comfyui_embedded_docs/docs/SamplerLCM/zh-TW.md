# SamplerLCM

SamplerLCM 節點提供一個具有可調整每步噪聲設定的 LCM（潛在一致性模型）取樣器。`s_noise` 參數作為模型訓練噪聲尺度的乘數，允許對每個取樣步驟中應用的噪聲進行精細控制。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `s_noise` | 第一步的每步噪聲乘數（1.0 = 符合訓練設定）。預設值：1.0。 | FLOAT | 是 | 0.0 至 64.0（步長：0.01） |
| `s_noise_end` | 最後一步的每步噪聲乘數。設定為與 `s_noise` 相同以保持恆定排程。預設值：1.0。 | FLOAT | 是 | 0.0 至 64.0（步長：0.01） |
| `noise_clip_std` | 將每步噪聲限制在 +/- N*標準差範圍內。設為 0 則停用。預設值：0.0。 | FLOAT | 是 | 0.0 至 10.0（步長：0.01） |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `SAMPLER` | 已設定的 LCM 取樣器物件，可用於取樣工作流程中。 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCM/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0d18f2f977ddadeedcd7807233b48ebcc4e94c6213f8540b9037a45a9c70c6cf`
