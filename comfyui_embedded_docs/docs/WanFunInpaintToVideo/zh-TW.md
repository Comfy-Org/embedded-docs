# WanFun 修補轉影片

WanFunInpaintToVideo 節點會為修補式影片生成準備條件與潛在資料，並使用選用的 `start_image` 與 `end_image` 來引導結果。它會將提供的條件、VAE 與影像影格，透過與首尾幀影片生成相同的邏輯進行處理，並傳回更新後的條件，以及供取樣使用的空白潛在表示。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向` | 用於影片生成的正向條件提示詞 | CONDITIONING | 是 | - |
| `負向` | 用於影片生成時避免出現的負向條件提示詞 | CONDITIONING | 是 | - |
| `vae` | 用於編碼與解碼影片影格的 VAE 模型 | VAE | 是 | - |
| `寬度` | 輸出影片寬度，單位為像素（預設值：832，步長：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `高度` | 輸出影片高度，單位為像素（預設值：480，步長：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `長度` | 影片序列中的影格數量（預設值：81，步長：4） | INT | 是 | 1 to MAX_RESOLUTION |
| `批次大小` | 一個批次中要生成的影片數量（預設值：1） | INT | 是 | 1 至 4096 |
| `clip_vision_output` | 選用的 CLIP 視覺輸出，用於作為 `start_image` 的條件 | CLIP_VISION_OUTPUT | 否 | - |
| `起始影像` | 選用的起始影格影像，用於影片生成 | IMAGE | 否 | - |
| `結束圖片` | 選用的結束影格影像，用於影片生成 | IMAGE | 否 | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 處理後的正向條件輸出 | CONDITIONING |
| `negative` | 處理後的負向條件輸出 | CONDITIONING |
| `latent` | 生成的影片潛在表示 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `70b58e961c5df12f94183245ce320197439b2505b47d0bb3ff643b25c9fe6175`
