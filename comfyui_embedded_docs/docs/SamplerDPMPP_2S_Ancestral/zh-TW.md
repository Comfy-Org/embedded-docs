# SamplerDPMPP_2S_Ancestral

## 概述

SamplerDPMPP_2S_Ancestral 節點建立一個使用 DPM++ 2S Ancestral 採樣方法來生成圖像的採樣器。此採樣器結合了確定性與隨機性元素，能在維持一定一致性的同時產生多樣化的結果。它讓您能夠控制採樣過程中的隨機性與噪聲程度。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `eta` | 控制採樣過程中添加的隨機噪聲量（預設值：1.0） | FLOAT | 是 | 0.0 - 100.0 |
| `s_noise` | 控制採樣過程中應用的噪聲規模（預設值：1.0） | FLOAT | 是 | 0.0 - 100.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `sampler` | 回傳一個已配置的採樣器物件，可用於採樣流程中 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2S_Ancestral/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9634c96934850f5b746cd7c8b29727396af534133b8d54b6bdac12e9e0975189`
