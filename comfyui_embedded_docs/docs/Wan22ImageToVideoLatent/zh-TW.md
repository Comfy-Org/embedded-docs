# Wan22ImageToVideoLatent

Wan22ImageToVideoLatent 可從圖像建立影片潛在表示。它會產生具有指定寬度、高度、幀長度和批次大小的空白影片潛在空間，並可選擇性地將起始圖像序列編碼到前幾幀中。當提供起始圖像時，此節點會將其編碼到潛在空間，並建立相應的雜訊遮罩，標記在生成過程中應去雜訊的區域。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `VAE` | 用於將起始圖像編碼到潛在空間的 VAE 模型 | VAE | 是 | - |
| `寬度` | 輸出影片的寬度（像素）（預設值：1280，步長：32） | INT | 是 | 32 to MAX_RESOLUTION |
| `高度` | 輸出影片的高度（像素）（預設值：704，步長：32） | INT | 是 | 32 to MAX_RESOLUTION |
| `長度` | 影片序列的幀數（預設值：49，步長：4） | INT | 是 | 1 to MAX_RESOLUTION |
| `批次大小` | 要生成的影片潛在數量（預設值：1） | INT | 是 | 1 至 4096 |
| `起始圖像` | 可選的起始圖像序列，用於編碼到影片潛在的起始幀中（使用前 `length` 幀） | IMAGE | 否 | - |

**注意：** 當提供 `start_image` 時，圖像序列會放大到目標 `width` 和 `height`，使用 VAE 編碼，並放入潛在的前幾幀中。這些幀的雜訊遮罩設為 0（保留），而其餘幀的遮罩值為 1（待去雜訊）。潛在始終擁有 48 個通道，空間維度為 `height / 16` × `width / 16`，時間維度為 `((length - 1) // 4) + 1`。`width` 和 `height` 必須能被 16 整除（由步長 32 強制），且 `length` 以 4 為步長增加時間維度。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `samples` | 生成的影片潛在表示，對批次中的每個項目重複 | LATENT |
| `noise_mask` | 雜訊遮罩，指示哪些區域應去雜訊（值 1）以及哪些區域保留已編碼的起始圖像（值 0） | LATENT |

兩個欄位會一起在單一 LATENT 輸出中返回。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3d05980641eeef2e86df7a845aa8b2bd703882db98fe71adef2746ab34a9d717`
