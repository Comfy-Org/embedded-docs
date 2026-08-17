# SamplerDPMPP_2S_Ancestral

SamplerDPMPP_2S_Ancestral 節點會建立一個使用 DPM++ 2S Ancestral 取樣方法來生成圖像的取樣器。此取樣器結合了確定性與隨機性元素，以在維持一定一致性的同時產生多樣化的結果。它讓您能夠控制取樣過程中的隨機性與雜訊程度。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `eta` | 控制取樣期間加入的隨機雜訊量（預設值：1.0） | FLOAT | 是 | 0.0 - 100.0 (step 0.01) |
| `s_noise` | 控制取樣過程中套用的雜訊尺度（預設值：1.0） | FLOAT | 是 | 0.0 - 100.0 (step 0.01) |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `sampler` | 傳回一個已設定好的取樣器物件，可用於取樣管線中 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2S_Ancestral/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8d20ec21e6c699965753413d9ef8b6191553c4b7b606d93c10470aa9d988a308`
