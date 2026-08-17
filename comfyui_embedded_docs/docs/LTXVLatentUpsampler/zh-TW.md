# LTXVLatentUpsampler

LTXVLatentUpsampler 節點會將影片潛在表示（latent representation）的空間解析度提高兩倍。它使用專門的放大模型來處理潛在資料，這些資料會先使用所提供的 VAE 頻道統計資料進行去標準化，然後再重新標準化。此節點專為潛在空間中的影片工作流程所設計。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `samples` | 要放大的影片輸入潛在表示。 | LATENT | 是 |  |
| `upscale_model` | 已載入的模型，用於對潛在資料執行 2 倍放大。 | LATENT_UPSCALE_MODEL | 是 |  |
| `vae` | VAE 模型，用於在放大前對輸入潛在變數進行去標準化，並在放大後對輸出潛在變數進行標準化。 | VAE | 是 |  |

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 放大後的潛在表示，其空間維度為輸入的兩倍。輸出潛在變數與輸入具有相同的批次大小、通道數和時間長度，並轉換回與輸入潛在變數相同的資料型別。若輸入包含 `noise_mask`，則會從輸出中移除。 | LATENT |

注意：此節點標記為實驗性功能。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVLatentUpsampler/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7d7f0b733cb3758e9ec985cac30134d719b130b5b86c35bfdd14576a5b4575db`
