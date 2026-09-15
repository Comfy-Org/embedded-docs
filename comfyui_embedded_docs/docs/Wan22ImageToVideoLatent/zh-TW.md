# Wan22ImageToVideoLatent

Wan22ImageToVideoLatent 會從影像建立影片潛在表示。它會產生一個空白影片潛在空間，具有指定的寬度、高度、影格長度與批次大小，並可選擇將起始影像序列編碼到開頭影格中。當提供起始影像時，此節點會將其編碼到潛在空間中，並建立對應的雜訊遮罩，標記在生成期間應進行去雜訊的區域。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `VAE` | 用於將起始影像編碼到潛在空間的 VAE 模型 | VAE | 是 | - |
| `寬度` | 輸出影片的寬度（像素）（預設：1280，步長：32） | INT | 是 | 32 to MAX_RESOLUTION |
| `高度` | 輸出影片的高度（像素）（預設：704，步長：32） | INT | 是 | 32 to MAX_RESOLUTION |
| `長度` | 影片序列中的影格數（預設：49，步長：4） | INT | 是 | 1 to MAX_RESOLUTION |
| `批次大小` | 要產生的影片潛在表示數量（預設：1） | INT | 是 | 1 至 4096 |
| `起始圖像` | 可選的起始影像序列，用於編碼到影片潛在表示的開頭影格中（使用前 `length` 個影格） | IMAGE | 否 | - |

**注意：** 當提供 `start_image` 時，影像序列會放大到目標 `width` 與 `height`，以 VAE 編碼，並放入潛在表示的前幾個影格中。這些影格的雜訊遮罩會設為 0（保留），而其餘影格的遮罩值為 1（要去雜訊）。潛在表示一律有 48 個通道，空間維度為 `height / 16` 乘 `width / 16`，時間維度為 `((length - 1) // 4) + 1`。`width` 與 `height` 必須可被 16 整除（由步長 32 強制達成），而 `length` 會以 4 為步長增加時間維度。

當未提供 `start_image` 時，會傳回完全空白的潛在表示，且沒有雜訊遮罩，而 `batch_size` 輸入不會套用到該空白潛在表示。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `samples` | 產生的影片潛在表示，會針對批次中的每個項目重複 | LATENT |
| `noise_mask` | 雜訊遮罩，指出哪些區域應該去雜訊（值為 1），以及哪些區域保留編碼後的起始影像（值為 0） | LATENT |

這兩個欄位會一起包含在單一的 LATENT 輸出中。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3d05980641eeef2e86df7a845aa8b2bd703882db98fe71adef2746ab34a9d717`
