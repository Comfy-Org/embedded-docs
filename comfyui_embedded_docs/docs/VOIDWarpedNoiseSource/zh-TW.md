# VOIDWarpedNoiseSource

## 概述

此節點將 LATENT（例如 VOIDWarpedNoise 節點的輸出）轉換為 NOISE 來源。這讓您能將扭曲噪點與 SamplerCustomAdvanced 節點搭配使用，以實現更可控的影像生成。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `warped_noise` | 來自 VOIDWarpedNoise 的扭曲噪點潛在空間 | LATENT | 是 | N/A |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `NOISE` | 可與 SamplerCustomAdvanced 搭配使用的噪點來源 | NOISE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ff798d223da5cf705a40ad1f36cc403030105331d0cc4173e9553cd3718c5d93`
