# EmptyMiniMaxMusic3LatentAudio

此節點為 MiniMax Music3 模型建立一個空白（填零）的音訊潛在表示。它將以秒為單位的請求持續時間轉換為對應的音訊幀，並產生正確大小的空白潛在張量，可作為音樂生成的起點。

## 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `秒數` | 音訊潛在表示的持續時間（秒）（預設：120.0）。該值會被轉換為音訊幀，並限制在模型支援的持續時間範圍內。 | FLOAT | 是 | 0.04 to (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND), step 0.04 |
| `batch_size` | 一次批次產生的音訊潛在表示數量（預設：1）。 | INT | 是 | 1 至 4096 |

注意：`seconds` 值會四捨五入至最接近的音訊幀，並限制在至少 1 幀、至多 `MAX_AUDIO_FRAMES` 幀的範圍內，因此實際潛在長度可能與輸入的精確值略有差異。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `LATENT` | 一個形狀為 (batch_size, 128, latent_length) 的補零音訊潛在張量。包含將樣本標記為音訊資料（時序下採樣比率為 512）的元資料。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMiniMaxMusic3LatentAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `77e6a69702a837c958c2954bba061c979152f034bc7774a5b6c97ea8d57bda4b`
