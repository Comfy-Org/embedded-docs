# VAE 編碼（分割區塊）

VAEEncodeTiled 透過將影像分割成較小的圖塊，並使用變分自編碼器（Variational Autoencoder）對其進行編碼來處理影像。這種圖塊化方法允許處理可能超出記憶體限制的大型影像。此節點支援影像和影片 VAE，並針對空間與時間維度提供個別的分塊控制。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `像素` | 要編碼的輸入影像資料 | IMAGE | 是 | - |
| `vae` | 用於編碼的變分自編碼器模型 | VAE | 是 | - |
| `區塊大小` | 空間處理中每個圖塊的大小（預設：512） | INT | 是 | 64-4096 (step: 64) |
| `重疊` | 相鄰圖塊之間的重疊量（預設：64） | INT | 是 | 0-4096 (step: 32) |
| `時間區塊大小` | 僅用於影片 VAE：每次編碼的影格數量（預設：64） | INT | 是 | 8-4096 (step: 4) |
| `時間重疊` | 僅用於影片 VAE：要重疊的影格數量（預設：8） | INT | 是 | 4-4096 (step: 4) |

**注意：** `temporal_size` 和 `temporal_overlap` 參數僅在使用影片 VAE 時才有作用，對標準影像 VAE 沒有影響。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 輸入影像經過編碼後的潛在表示 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeTiled/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c36b02f8eeed5c72f9efa2392e2013e89be7644c022d987d413d4da088dfbaad`
