# MiniMax H3 圖片轉影片

MiniMax H3 Image to Video 節點準備了使用 MiniMax H3 模型生成影片所需的 conditioning 與空 latent。它接受文字提示詞，以及可選擇的影片首幀及/或末幀影像，並將它們轉換為模型輸入。關鍵幀影像會被調整大小、編碼，並在影片的開頭與結尾附加到 conditioning 中。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `clip` | 用於將提示詞標記化並將關鍵幀影像編碼為 conditioning 的 CLIP 模型。 | CLIP | 是 |  |
| `vae` | 當提供關鍵幀影像時，用於將關鍵幀影像編碼至潛在空間的 VAE 模型。 | VAE | 是 |  |
| `prompt` | 描述要生成之影片的文字提示詞。支援多行和動態提示詞。 | STRING | 是 |  |
| `width` | 影片的寬度（像素，預設值：1344）。 | INT | 是 | 32 to MAX_RESOLUTION (step 32) |
| `height` | 影片的高度（像素，預設值：768）。 | INT | 是 | 32 to MAX_RESOLUTION (step 32) |
| `length` | 以 24 fps 計的幀數，會向上調整至模型的 17k+5 網格（124 ≈ 5 秒；訓練範圍約為 124-362，更長未經測試）（預設值：124）。 | INT | 是 | 5 to 3600 (step 17) |
| `first_frame` | 可選的影像，用作影片的第一幀。它會被拉伸至完整畫布大小，因此不會保留其長寬比。僅使用輸入批次中的第一張影像。 | IMAGE | 否 |  |
| `last_frame` | 可選的影像，用作影片的最後一幀。它會被裁切以覆蓋畫布，同時保留其長寬比。僅使用輸入批次中的第一張影像。 | IMAGE | 否 |  |

當提供 `first_frame` 及/或 `last_frame` 時，關鍵幀影像會使用 VAE 編碼，並分別附加到第 0 幀與最後一幀的 conditioning 中。當兩者皆未提供時，此節點僅依據提示詞運作。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `positive` | 包含編碼後提示詞的 conditioning，且當提供關鍵幀影像時，包含位於影片第一幀與最後一幀、適用於 MiniMax H3 模型的編碼後關鍵幀。 | CONDITIONING |
| `latent` | 空 latent，代表要生成的影片及其伴隨音軌，具有請求的寬度、高度與幀數。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ImageToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d1bdf3f8c66ef20ff11c35203d2c266a88dcf8cc00c65dbb0aea2b1dd16befd6`
