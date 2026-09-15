# CosmosPredict2ImageToVideoLatent

為 Cosmos Predict2 圖像轉影片工作流程建立影片潛在表徵。此節點可產生指定大小與長度的空白影片潛在表徵，或將編碼後的起始及/或結束影像插入序列中，讓這些影格在生成期間被保留。任何提供的影像都會調整至指定的 `width` 與 `height`，並使用提供的 VAE 編碼後，放置在潛在序列的開頭及/或結尾。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `VAE` | 用於將起始與結束影像編碼至潛在空間的 VAE 模型 | VAE | 是 | - |
| `寬度` | 輸出影片的寬度（像素，預設值：848，必須為 16 的倍數） | INT | 是 | 16 to MAX_RESOLUTION |
| `高度` | 輸出影片的高度（像素，預設值：480，必須為 16 的倍數） | INT | 是 | 16 to MAX_RESOLUTION |
| `長度` | 影片序列中的影格數（預設值：93） | INT | 是 | 1 to MAX_RESOLUTION |
| `批次大小` | 要生成的影片序列數量（預設值：1） | INT | 是 | 1 至 4096 |
| `起始影像` | 影片序列的選用起始影像 | IMAGE | 否 | - |
| `結束影像` | 影片序列的選用結束影像 | IMAGE | 否 | - |

**注意：** 當 `start_image` 與 `end_image` 皆未提供時，此節點只會傳回指定大小與長度的空白潛在表徵。當提供其中一張或兩張影像時，它們會調整為 `width` 與 `height`，使用 `vae` 編碼，並放置在潛在序列的開頭及/或結尾。對應區域會在雜訊遮罩中標記，以便在生成期間保留。編碼後的潛在表徵會使用 Wan 2.1 潛在格式進行轉換，而產生的潛在表徵與遮罩會重複 `batch_size` 次。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 產生的影片潛在表徵，包含 `samples`（影片潛在序列），且當至少提供 `start_image` 或 `end_image` 其中之一時，會包含 `noise_mask`，用於標記生成期間應保留的影格 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `842bd2b8cda438e7b938439d4eba280478939e3302dc1846d52595d40082ff05`
