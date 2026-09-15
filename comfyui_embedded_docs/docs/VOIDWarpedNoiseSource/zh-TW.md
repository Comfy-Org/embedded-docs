# VOIDWarpedNoiseSource

此節點會將 LATENT（例如 VOIDWarpedNoise 節點的輸出）轉換為 NOISE 來源。這讓您可以將預先計算好的扭曲雜訊饋入需要雜訊來源的節點，例如 SamplerCustomAdvanced。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `warped_noise` | 來自 VOIDWarpedNoise 的扭曲雜訊 latent | LATENT | 是 | N/A |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `NOISE` | 包裝所提供 latent 的雜訊來源，可與 SamplerCustomAdvanced 搭配使用 | NOISE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/zh-TW.md)

---
**Source fingerprint (SHA-256):** `61d7c82cb8a2acba28f980c4c42c6d4be12788b27676a5d30885799cf9c36185`
