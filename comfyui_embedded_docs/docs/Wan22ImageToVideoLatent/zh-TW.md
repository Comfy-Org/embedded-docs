> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/zh-TW.md)

Wan22ImageToVideoLatent 節點可從影像建立影片潛在空間表示。它會生成具有指定尺寸的空白影片潛在空間，並可選擇性地將起始影像序列編碼到前幾個影格中。當提供起始影像時，它會將該影像編碼到潛在空間中，並為修補區域建立對應的雜訊遮罩。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `vae` | VAE | 是 | - | 用於將影像編碼到潛在空間的 VAE 模型 |
| `width` | INT | 是 | 32 至 MAX_RESOLUTION | 輸出影片的像素寬度（預設值：1280，步長：32） |
| `height` | INT | 是 | 32 至 MAX_RESOLUTION | 輸出影片的像素高度（預設值：704，步長：32） |
| `length` | INT | 是 | 1 至 MAX_RESOLUTION | 影片序列中的影格數量（預設值：49，步長：4） |
| `batch_size` | INT | 是 | 1 至 4096 | 要生成的批次數量（預設值：1） |
| `start_image` | IMAGE | 否 | - | 可選的起始影像序列，用於編碼到影片潛在空間中 |

**注意：** 當提供 `start_image` 時，節點會將影像序列編碼到潛在空間的起始影格中，並生成對應的雜訊遮罩。`width` 和 `height` 參數必須能被 16 整除，以確保潛在空間尺寸正確。`length` 參數決定影片潛在空間中的影格數量；潛在空間的時間維度計算方式為 `((length - 1) // 4) + 1`。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `samples` | LATENT | 生成的影片潛在空間表示 |
| `noise_mask` | LATENT | 雜訊遮罩，指示生成過程中哪些區域應進行去噪處理 |

---
**Source fingerprint (SHA-256):** `0f27e20bcc63f0dd224cda0fa26ee676c42898ac74fcfbe0a2b591def933689c`
