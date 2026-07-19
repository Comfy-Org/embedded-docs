# CosmosPredict2ImageToVideoLatent

CosmosPredict2ImageToVideoLatent 節點可從影像建立影片潛在表示，以用於影片生成。它能生成空白影片潛在，或結合起始與結束影像，建立具有指定尺寸與時長的影片序列。此節點負責將影像編碼為適合影片處理的潛在空間格式。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `VAE` | 用於將影像編碼至潛在空間的 VAE 模型 | VAE | 是 | - |
| `寬度` | 輸出影片的寬度（像素），預設值：848，必須為 16 的倍數 | INT | 否 | 16 至 MAX_RESOLUTION |
| `高度` | 輸出影片的高度（像素），預設值：480，必須為 16 的倍數 | INT | 否 | 16 至 MAX_RESOLUTION |
| `長度` | 影片序列的影格數，預設值：93，步進值：4 | INT | 否 | 1 至 MAX_RESOLUTION |
| `批次大小` | 要生成的影片序列數量，預設值：1 | INT | 否 | 1 至 4096 |
| `起始影像` | 可選的影片序列起始影像 | IMAGE | 否 | - |
| `結束影像` | 可選的影片序列結束影像 | IMAGE | 否 | - |

**注意：** 當未提供 `start_image` 與 `end_image` 時，節點會生成空白影片潛在。若提供了影像，則會將其編碼，並透過適當的遮罩，置於影片序列的開頭及/或結尾。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `samples` | 生成的影片潛在表示，包含編碼後的影片序列 | LATENT |
| `noise_mask` | 一個遮罩，指示生成過程中應保留潛在的哪些部分 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `55fab16180c0e3fa254bcc77694dbc666810b28522e61b9c613f720fae66bd0c`
