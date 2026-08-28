# LTXVLatentUpsampler

LTXVLatentUpsampler 節點會將影片潛在表示（latent representation）的空間解析度提升兩倍。它使用專門的超解析度模型來處理潛在資料，這些資料會先經過反標準化，再使用所提供 VAE 的通道統計資料重新標準化。此節點專為潛在空間中的影片工作流程而設計。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `樣本` | 要進行超解析度處理的影片輸入潛在表示。 | LATENT | 是 |  |
| `放大模型` | 用於對潛在資料執行 2 倍超解析度處理的已載入模型。 | LATENT_UPSCALE_MODEL | 是 |  |
| `vae` | 用於在超解析度處理前對輸入潛在進行反標準化，並在之後對輸出潛在進行標準化的 VAE 模型。 | VAE | 是 |  |

注意：此節點在 ComfyUI 中被標記為實驗性功能。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 超解析度處理後的潛在表示，其空間維度與輸入相比增加一倍。輸出潛在與輸入具有相同的批次大小、通道數和時間長度。輸入中的 `noise_mask`（如果存在的話）會從輸出中移除。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVLatentUpsampler/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7d7f0b733cb3758e9ec985cac30134d719b130b5b86c35bfdd14576a5b4575db`
