# CosmosPredict2ImageToVideoLatent

CosmosPredict2ImageToVideoLatent 會從影像建立影片潛在表示，用於影片生成。它可以產生空白的影片潛在，或結合起始影像與結束影像，建立具有指定尺寸與時長的影片序列。此節點負責將影像編碼為適合影片處理的潛在空間格式。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `VAE` | 用於將影像編碼至潛在空間的 VAE 模型 | VAE | 是 | - |
| `寬度` | 輸出影片的寬度（像素，預設值：848，必須能被 16 整除） | INT | 是 | 16 至 MAX_RESOLUTION |
| `高度` | 輸出影片的高度（像素，預設值：480，必須能被 16 整除） | INT | 是 | 16 至 MAX_RESOLUTION |
| `長度` | 影片序列中的影格數（預設值：93，間距：4） | INT | 是 | 1 至 MAX_RESOLUTION |
| `批次大小` | 要生成的影片序列數量（預設值：1） | INT | 是 | 1 至 4096 |
| `起始影像` | 影片序列的選用起始影像 | IMAGE | 否 | - |
| `結束影像` | 影片序列的選用結束影像 | IMAGE | 否 | - |

**注意：** 當未提供 `start_image` 與 `end_image` 時，節點會生成空白的影片潛在。當提供其中一張或兩張影像時，這些影像會被調整為 `width` 與 `height`，編碼至潛在空間，並放置在影片序列的開頭及/或結尾，並在噪聲遮罩中標記對應區域，以便在生成期間保留這些區域。產生的潛在與遮罩會重複 `batch_size` 次。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `samples` | 生成的影片潛在表示，包含已編碼的影片序列 | LATENT |
| `noise_mask` | 表示生成期間應保留哪些潛在部分的遮罩。僅在提供 `start_image` 或 `end_image` 至少其中之一時存在。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `842bd2b8cda438e7b938439d4eba280478939e3302dc1846d52595d40082ff05`
