# SamplerDPMPP_2S_Ancestral

SamplerDPMPP_2S_Ancestral 節點會建立一個使用 DPM++ 2S Ancestral 採樣方法來生成圖像的取樣器。此取樣器結合了確定性與隨機性元素，以產生多樣化的結果，同時保持一定的一致性。它讓您能夠在採樣過程中控制隨機性和噪聲等級。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `eta` | 控制採樣期間添加的隨機噪聲量（預設值：1.0） | FLOAT | 是 | 0.0 - 100.0 |
| `s_noise` | 控制採樣過程中應用的噪聲尺度（預設值：1.0） | FLOAT | 是 | 0.0 - 100.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `sampler` | 返回一個已配置的取樣器物件，可用於取樣管線中 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2S_Ancestral/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8d20ec21e6c699965753413d9ef8b6191553c4b7b606d93c10470aa9d988a308`
