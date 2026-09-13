# 空白 YuE2 潛空間音訊

此節點會為 YuE2 建立一個空的音訊 latent，大小會依所選時長與批次數量決定。它會產生無聲的預留音訊資料，供後續節點在音訊生成期間填入。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `seconds` | 要建立的音訊 latent 長度，以秒為單位（預設：120.0）。latent 幀數會依此值計算，最少為 1 幀。 | FLOAT | 是 | 0.04 至 1000.0 （步進值：0.04） |
| `batch_size` | 一個批次中要建立的音訊 latent 數量（預設：1）。 | INT | 是 | 1 至 4096 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `LATENT` | 一個空的音訊 latent，包含全零張量，大小由 `batch_size` 以及從 `seconds` 推導出的幀數決定。它會被標記為音訊類型，時間下採樣比率為 1920。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyYuE2LatentAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3397e3feb534c87d9790bbfe36e8e641476d9b6aa00d75a4e6d0c32f4a948563`
