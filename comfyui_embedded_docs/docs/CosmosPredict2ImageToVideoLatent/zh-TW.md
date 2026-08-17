# CosmosPredict2ImageToVideoLatent

CosmosPredict2ImageToVideoLatent 節點會從影像建立影片潛在表示，以供影片生成使用。它可以生成空白的影片潛在，或結合起始與結束影像，建立具有指定尺寸與時長的影片序列。該節點負責將影像編碼為適合影片處理的潛在空間格式。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `vae` | 用於將影像編碼至潛在空間的 VAE 模型 | VAE | 是 | - |
| `width` | 輸出影片的寬度（像素）（預設值：848，必須能被 16 整除） | INT | 是 | 16 to MAX_RESOLUTION (step 16) |
| `height` | 輸出影片的高度（像素）（預設值：480，必須能被 16 整除） | INT | 是 | 16 to MAX_RESOLUTION (step 16) |
| `length` | 影片序列中的影格數（預設值：93） | INT | 是 | 1 to MAX_RESOLUTION (step 4) |
| `batch_size` | 要生成的影片序列數量（預設值：1） | INT | 是 | 1 to 4096 |
| `start_image` | 影片序列的選用起始影像 | IMAGE | 否 | - |
| `end_image` | 影片序列的選用結束影像 | IMAGE | 否 | - |

**注意：** 若未提供 `start_image` 與 `end_image`，節點會生成空白的影片潛在。若提供了影像，則會將影像編碼，並以適當的遮罩放置在影片序列的開頭及/或結尾。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `samples` | 生成的影片潛在表示，包含已編碼的影片序列 | LATENT |
| `noise_mask` | 指示生成期間應保留潛在哪些部分的遮罩 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `842bd2b8cda438e7b938439d4eba280478939e3302dc1846d52595d40082ff05`
