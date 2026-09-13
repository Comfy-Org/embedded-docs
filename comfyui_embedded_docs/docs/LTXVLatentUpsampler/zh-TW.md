# LTXVLatentUpsampler

LTXVLatentUpsampler 節點將影片潛在表示的空間解析度提高兩倍。它使用專用的放大模型來處理潛在資料，這些資料首先被去標準化，然後使用所提供的 VAE 的通道統計資料重新標準化。此節點專為潛在空間中的影片工作流程而設計。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `樣本` | 要放大的影片輸入潛在表示。 | LATENT | 是 |  |
| `放大模型` | 用於對潛在資料執行 2 倍放大的已載入模型。 | LATENT_UPSCALE_MODEL | 是 |  |
| `vae` | 用於在放大前對輸入潛在進行去標準化，並在放大後對輸出潛在進行標準化的 VAE 模型。 | VAE | 是 |  |

注意：此節點在 ComfyUI 中被標記為實驗性。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 放大後的潛在表示，其空間尺寸是輸入的兩倍。輸出潛在具有與輸入相同的批次大小、通道數和時間長度。如果輸入中存在 `noise_mask`，則會從輸出中移除。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVLatentUpsampler/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7d7f0b733cb3758e9ec985cac30134d719b130b5b86c35bfdd14576a5b4575db`
