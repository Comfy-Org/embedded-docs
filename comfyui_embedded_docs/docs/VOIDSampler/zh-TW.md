## 概述

VOIDSampler 節點提供一種專門為 VOID 修復模型設計的 DDIM 取樣方法。它實作了與 VOID 模型訓練期間相同的去噪過程，但未套用標準 KSampler 所使用的噪聲縮放。此節點旨在與 SamplerCustom 或 SamplerCustomAdvanced 節點搭配使用，並應與 RandomNoise 或 VOIDWarpedNoiseSource 配對。

## 輸入

此節點沒有可設定的輸入參數。它是一個自包含的取樣器，套用固定的 DDIM 取樣演算法。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| *無輸入* | 此節點不接受任何輸入參數。 | - | - | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `SAMPLER` | 一個實作 VOID DDIM 演算法的取樣器物件，準備好連接到 SamplerCustom 或 SamplerCustomAdvanced 節點。 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c6f1be9a90003906c54cced20e8136ab7e4f7e7118e63b67ce366eeb7f790dca`
