# Wan22ImageToVideoLatent

Wan22ImageToVideoLatent 節點準備用於 Wan 2.2 影片生成的潛在輸入。它會建立一個具有指定寬度、高度和影格數的空影片潛在空間，並在提供起始影像時，將該影像編碼到潛在空間的前幾個影格中。它也會輸出一個雜訊遮罩，用於標記哪些影格已由影像填充，哪些影格仍需生成。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `vae` | 用於將起始影像編碼到潛在空間的 VAE 模型 | VAE | 是 | - |
| `width` | 輸出影片的寬度（像素）（預設值：1280，步長：32） | INT | 是 | 32 至 MAX_RESOLUTION |
| `height` | 輸出影片的高度（像素）（預設值：704，步長：32） | INT | 是 | 32 至 MAX_RESOLUTION |
| `length` | 影片中的影格數（預設值：49，步長：4） | INT | 是 | 1 至 MAX_RESOLUTION |
| `batch_size` | 平行生成的影片潛在數量（預設值：1） | INT | 是 | 1 至 4096 |
| `start_image` | 可選的影像或影像序列，放置於影片潛在空間的前幾個影格中。僅使用前 `length` 個影格。此影像在由 VAE 編碼前，會使用雙線性重取樣並置中裁切，調整為 `width` x `height` 的大小。 | IMAGE | 否 | - |

**注意：** 潛在空間的空間維度為 `width / 16` 和 `height / 16`，因此 `width` 和 `height` 必須能被 16 整除。潛在空間的時間維度計算方式為 `((length - 1) // 4) + 1`，且具有 48 個通道。當提供 `start_image` 時，編碼後的影像會填入潛在空間的前幾個影格，而 `noise_mask` 會將這些影格設為 0，其餘影格設為 1，這會告訴取樣器保持影像影格不變並生成其餘部分。當未提供 `start_image` 時，潛在空間會以零填充，且不會包含雜訊遮罩。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 生成的影片潛在，重複 `batch_size` 次。當提供 `start_image` 時，它還包含一個 `noise_mask`，標記影像編碼的影格（0）和要生成的影格（1）。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3d05980641eeef2e86df7a845aa8b2bd703882db98fe71adef2746ab34a9d717`
