# 空白 MiniMax Music3 latent 音訊

此節點會為 MiniMax Music3 模型建立一個空白（全零填充）的音訊 latent。它會將要求的持續時間（以秒為單位）轉換為對應的音訊幀數，並產生正確大小的空白 latent 張量，可直接作為音樂生成的起始點。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `秒數` | 音訊 latent 的持續時間，以秒為單位（預設：120.0）。該值會轉換為音訊幀，並限制在模型支援的持續時間範圍內。 | FLOAT | 是 | 0.04 to (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND), step 0.04 |
| `batch_size` | 一次批次中要產生的音訊 latent 數量（預設：1）。 | INT | 是 | 1 至 4096 |

注意：`seconds` 值會四捨五入至最接近的音訊幀，並限制在最少 1 幀、最多 `MAX_AUDIO_FRAMES` 幀，因此實際 latent 長度可能與輸入的確切值略有不同。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `LATENT` | 一個形狀為 (batch_size, 128, latent_length) 的全零填充音訊 latent 張量。包含將樣本標記為音訊資料、時間降採樣比例為 512 的中繼資料。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMiniMaxMusic3LatentAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `77e6a69702a837c958c2954bba061c979152f034bc7774a5b6c97ea8d57bda4b`
