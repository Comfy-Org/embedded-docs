# BerniniConditioning

BerniniConditioning 節點負責為 Wan2.2-A14B 模型準備影片與影像的條件化資料。它使用提供的 VAE 對來源影片、參考影片及參考影像進行編碼，然後將其附加到條件化資料中，以執行情境內生成任務。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 正向條件化資料 | CONDITIONING | 是 | - |
| `negative` | 負向條件化資料 | CONDITIONING | 是 | - |
| `vae` | 用於編碼影片與影像輸入的 VAE 模型 | VAE | 是 | - |
| `width` | 輸出潛在空間的寬度（預設值：832） | INT | 是 | 16 至 8192（步長：16） |
| `height` | 輸出潛在空間的高度（預設值：480） | INT | 是 | 16 至 8192（步長：16） |
| `length` | 輸出潛在空間的影格數（預設值：81） | INT | 是 | 1 至 8192（步長：4） |
| `batch_size` | 單一批次中生成的影片數量（預設值：1） | INT | 是 | 1 至 4096 |
| `source_video` | 要編輯或重新風格的來源影片（v2v, rv2v）。會調整為指定的寬度/高度，並裁剪至指定長度。 | IMAGE | 否 | - |
| `reference_video` | 要插入來源影片中的影片（ads2v）。 | IMAGE | 否 | - |
| `reference_images` | 作為情境內標記注入的參考影像（r2v, rv2v）。最多可提供 8 張影像。 | IMAGE | 否 | 0 至 8 張影像 |
| `ref_max_size` | 參考影片與參考影像長邊的最大尺寸。會保持長寬比進行調整，並對齊至 16 像素（預設值：848）。 | INT | 否 | 16 至 8192（步長：16） |

**注意：** 任務類型會根據連接的輸入推斷：
- 未連接任何輸入 → 文字轉影片（t2v）
- 僅連接 `source_video` → 影片轉影片（v2v）
- 連接 `source_video` + `reference_images` → 參考引導的影片編輯（rv2v）
- 僅連接 `reference_images` → 參考轉影片（r2v）
- 連接 `source_video` + `reference_video` → 將影像/影片插入影片（ads2v）

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `positive` | 附加了情境潛在空間的正向條件化資料 | CONDITIONING |
| `negative` | 附加了情境潛在空間的負向條件化資料 | CONDITIONING |
| `latent` | 空的潛在空間張量，其維度符合指定的寬度、高度、長度與批次大小 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BerniniConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3535bbe9a1ae007dc579242b44787ab315479a820eb0da680eab9b870ab60699`
