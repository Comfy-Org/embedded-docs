# EmptyMiniMaxMusic3LatentAudio

此節點為 MiniMax Music3 模型建立一個空的（零填充）潛在音訊張量。它會將要求的持續時間（秒）轉換為對應的音訊幀，並產生正確大小的空白潛在張量，作為音樂生成的起點。

## 輸入

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `seconds` | 音訊潛在張量的持續時間（秒）（預設值：120.0）。此值會轉換為音訊幀，並限制在模型支援的持續時間範圍內。 | FLOAT | 是 | 0.04 至 model maximum (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND), 步長 0.04 |
| `batch_size` | 一次生成的音訊潛在張量數量（預設值：1）。 | INT | 是 | 1 至 4096 |

注意：`seconds` 值會四捨五入到最接近的音訊幀，並限制在最少 1 幀、最多 `MAX_AUDIO_FRAMES` 幀之間，因此實際潛在長度可能與輸入的精確值略有不同。

## 輸出

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `LATENT` | 一個形狀為 (batch_size, 128, latent_length) 的零填充音訊潛在張量。包含將樣本標記為音訊資料的元資料，時間向下取樣比例為 512。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMiniMaxMusic3LatentAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `77e6a69702a837c958c2954bba061c979152f034bc7774a5b6c97ea8d57bda4b`
