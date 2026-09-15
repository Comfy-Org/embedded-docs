# EmptyAceStep1.5LatentAudio

`Empty Ace Step 1.5 Latent Audio` 節點會為音訊生成工作流程建立一個空的（靜音）音訊潛在張量。它會建立一個具有 64 個通道的潛在張量，其時間長度根據所請求的持續時間計算，並將其標記為音訊資料，以供下游音訊節點使用。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `seconds` | 要生成之音訊的持續時間，以秒為單位（預設：120.0）。潛在長度計算方式為 `seconds * 48000 / 1920`，並四捨五入至最接近的整數。 | FLOAT | 是 | 1.0 - 1000.0 （步進值：0.01） |
| `batch_size` | 批次中的潛在影像數量（預設：1）。 | INT | 是 | 1 - 4096 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 一個代表靜音音訊的空潛在張量。此張量的形狀為 [batch_size, 64, length]，其中 length 由 `seconds` 推導而來。輸出也包含類型識別碼 "audio"，以及 `downscale_ratio_temporal` 值 1764，用於音訊處理中的時間降採樣。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStep1.5LatentAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `bb7120c91ce5d779147cb8553d6f96fa160d87468d4d87550fb6dd4ec89b1557`
