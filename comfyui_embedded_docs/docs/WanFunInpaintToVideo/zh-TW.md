WanFunInpaintToVideo 節點透過在起始與結束影像之間進行修補來建立影片序列。它接收正向與負向條件輸入，以及可選的幀影像，以生成影片潛在表示。此節點可處理具有可配置尺寸與長度參數的影片生成。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向` | 用於影片生成的正向條件提示 | CONDITIONING | 是 | - |
| `負向` | 影片生成中需避免的負向條件提示 | CONDITIONING | 是 | - |
| `vae` | 用於編碼/解碼操作的 VAE 模型 | VAE | 是 | - |
| `寬度` | 輸出影片的寬度（像素）（預設值：832，步長：16） | INT | 是 | 16 至 MAX_RESOLUTION |
| `高度` | 輸出影片的高度（像素）（預設值：480，步長：16） | INT | 是 | 16 至 MAX_RESOLUTION |
| `長度` | 影片序列的幀數（預設值：81，步長：4） | INT | 是 | 1 至 MAX_RESOLUTION |
| `批次大小` | 每批次生成的影片數量（預設值：1） | INT | 是 | 1 至 4096 |
| `clip_vision_output` | 可選的 CLIP 視覺輸出，用於額外條件控制 | CLIP_VISION_OUTPUT | 否 | - |
| `起始影像` | 可選的影片生成起始幀影像 | IMAGE | 否 | - |
| `結束圖片` | 可選的影片生成結束幀影像 | IMAGE | 否 | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `負向` | 處理後的正向條件輸出 | CONDITIONING |
| `潛在空間` | 處理後的負向條件輸出 | CONDITIONING |
| `latent` | 生成的影片潛在表示 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `bbc5c2614f5fc21877345b3f01686ea57bee5108cdb253fb5dbf4b2cce9e59dd`
