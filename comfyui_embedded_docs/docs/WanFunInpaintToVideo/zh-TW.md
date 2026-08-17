# WanFun 修補轉影片

WanFunInpaintToVideo 節點透過在開始與結束圖像之間進行修補（inpainting）來建立影片序列。它接受正向與負向條件，以及可選的幀圖像，以生成影片潛在表示。此節點處理具有可設定尺寸與長度參數的影片生成。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 用於影片生成的正向條件提示詞 | CONDITIONING | 是 | - |
| `negative` | 用於影片生成中要避免的負向條件提示詞 | CONDITIONING | 是 | - |
| `vae` | 用於編碼/解碼操作的 VAE 模型 | VAE | 是 | - |
| `width` | 輸出影片寬度（像素）（預設：832，步長：16） | INT | 是 | 16 至 MAX_RESOLUTION |
| `height` | 輸出影片高度（像素）（預設：480，步長：16） | INT | 是 | 16 至 MAX_RESOLUTION |
| `length` | 影片序列中的幀數（預設：81，步長：4） | INT | 是 | 1 至 MAX_RESOLUTION |
| `batch_size` | 每批生成的影片數量（預設：1） | INT | 是 | 1 至 4096 |
| `clip_vision_output` | 可選的 CLIP 視覺輸出，用於額外條件輸入 | CLIP_VISION_OUTPUT | 否 | - |
| `start_image` | 可選的開始幀圖像，用於影片生成 | IMAGE | 否 | - |
| `end_image` | 可選的結束幀圖像，用於影片生成 | IMAGE | 否 | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 已處理的正向條件輸出 | CONDITIONING |
| `negative` | 已處理的負向條件輸出 | CONDITIONING |
| `latent` | 生成的影片潛在表示 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `70b58e961c5df12f94183245ce320197439b2505b47d0bb3ff643b25c9fe6175`
