# 分割 SeedVR2 latent

此節點將 SeedVR2 影片潛在變量分割成較小的時間區塊，以便在可用 VRAM 範圍內逐一處理。它會根據您的 GPU 記憶體自動計算最佳區塊大小，或讓您手動指定區塊大小，並按順序輸出區塊以供處理。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `latent` | 要分割的 VAE 編碼 SeedVR2 潛在變量。必須是 5 維張量（B, C, T, H, W），且通道數符合 SeedVR2 潛在預期。 | LATENT | 是 | - |
| `temporal_overlap` | 相鄰區塊之間共享並在合併時交叉淡化的潛在影格；0 表示無重疊（預設值：0）。有效重疊上限為區塊的潛在影格數減 1。 | INT | 否 | 0 至 16384 |
| `chunking_mode` | 手動模式精確使用 frames_per_chunk；自動模式預測符合可用 VRAM 的最大區塊。 | COMBO | 是 | "auto"<br>"manual" |

當 `chunking_mode` 設為 "manual" 時，會出現一個額外參數：

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `frames_per_chunk` | 每個時間區塊的像素影格數（4n+1：1、5、9、13、17、21...）；介面以 4 為步進（預設值：21）。 | INT | 是 | 1 至 16384 |

注意：`frames_per_chunk` 參數僅在 `chunking_mode` 設為 "manual" 時才會顯示。該值必須滿足公式 `(frames_per_chunk - 1) % 4 == 0`，即必須為以下數值之一：1、5、9、13、17、21 等。輸入潛在必須為 5 維且包含預期的 SeedVR2 潛在通道數；否則節點將引發錯誤。如果潛在中的總像素影格數等於或小於所選區塊大小（或自動計算的大小），節點將回傳原始潛在作為單一區塊且無重疊。

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `latents` | 按順序排列的時間區塊。 | LATENT |
| `temporal_overlap` | 相鄰區塊之間有效的潛在影格重疊量，用於合併 SeedVR2 潛在變量。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalChunk/zh-TW.md)

---
**Source fingerprint (SHA-256):** `40af2b690f74555efbe38f4cf76825417f52735ce90296a9ad662f78cfe4c6bf`
