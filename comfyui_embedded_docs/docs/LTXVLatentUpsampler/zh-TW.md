# LTXVLatentUpsampler 節點

LTXVLatentUpsampler 節點可將影片潛在表示（latent representation）的空間解析度提升兩倍。它使用專門的放大模型來處理潛在資料，首先進行去標準化（un-normalize），然後使用提供的 VAE 通道統計資料重新進行標準化（re-normalize）。此節點專為潛在空間內的影片工作流程而設計。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `樣本` | 要進行放大處理的輸入影片潛在表示。 | LATENT | 是 |  |
| `放大模型` | 用於對潛在資料執行 2 倍放大的已載入模型。 | LATENT_UPSCALE_MODEL | 是 |  |
| `vae` | 用於在放大前對輸入潛在資料進行去標準化，並在放大後對輸出潛在資料進行標準化的 VAE 模型。 | VAE | 是 |  |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 放大後的潛在表示，其空間維度相較於輸入增加一倍。輸出潛在資料的批次大小、通道數量和時間長度與輸入相同。輸入中的 `noise_mask`（若存在）將從輸出中移除。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVLatentUpsampler/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b2c726d3a3e4881eee7e1d3bae8c478adf01cd87a9652be882579f4e26c1536f`
