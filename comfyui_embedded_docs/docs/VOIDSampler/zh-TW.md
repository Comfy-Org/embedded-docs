# VOIDSampler

VOIDSampler 是針對 VOID 修復（inpainting）模型的專用 DDIM 取樣器。它實作了 VOID 訓練時所使用的相同去噪流程，但不包含標準 KSampler 所套用的雜訊縮放。請搭配 SamplerCustom 或 SamplerCustomAdvanced 節點使用此節點，並與 RandomNoise 或 VOIDWarpedNoiseSource 配對。

## 輸入

此節點沒有可設定的輸入參數。它是一個自包含的取樣器，套用固定的 DDIM 取樣演算法。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| *無輸入* | 此節點不接受任何輸入參數。 | - | - | - |

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `SAMPLER` | 一個實作 VOID DDIM 演算法的取樣器物件，可準備連接到 SamplerCustom 或 SamplerCustomAdvanced 節點。 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b8bb6d3d7220cca4a6dd252efe9c92953b1c5c67c14365e5e0583bc9bdb133be`
