# VAE 編碼（分割區塊）

VAEEncodeTiled 節點透過將影像分割成較小的區塊，並使用變分自編碼器進行編碼來處理影像。這種分塊方法可以處理可能超出記憶體限制的大型影像。此節點同時支援影像和影片 VAE，並針對空間和時間維度提供獨立的分塊控制。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `pixels` | 要編碼的輸入影像資料 | IMAGE | 是 | - |
| `vae` | 用於編碼的變分自編碼器模型 | VAE | 是 | - |
| `tile_size` | 用於空間處理的每個區塊大小（預設值：512） | INT | 是 | 64-4096（步進：64） |
| `overlap` | 相鄰區塊之間的重疊量（預設值：64） | INT | 是 | 0-4096（步進：32） |
| `temporal_size` | 僅用於影片 VAE：每次編碼的影格數（預設值：64） | INT | 是 | 8-4096（步進：4） |
| `temporal_overlap` | 僅用於影片 VAE：要重疊的影格數（預設值：8） | INT | 是 | 4-4096（步進：4） |

**注意：** `temporal_size` 和 `temporal_overlap` 參數僅在使用影片 VAE 時相關，對標準影像 VAE 沒有影響。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 輸入影像的編碼潛在表示 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeTiled/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c36b02f8eeed5c72f9efa2392e2013e89be7644c022d987d413d4da088dfbaad`
