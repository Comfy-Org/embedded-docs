# 空白潛空間音訊

EmptyLatentAudio 節點會建立用於音訊處理的空潛在張量。它會根據指定的持續時間和批次大小，產生空白的音訊潛在表示，可作為音訊生成或處理工作流程的起點。此節點會根據音訊持續時間和取樣率自動計算適當的潛在維度。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `seconds` | 音訊的持續時間（以秒為單位）（預設值：47.6） | FLOAT | 是 | 1.0 - 1000.0 (step 0.1) |
| `batch_size` | 批次中的潛在影像數量（預設值：1） | INT | 是 | 1 - 4096 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 傳回一個用於音訊處理的空潛在張量，具有指定的持續時間和批次大小。該張量的形狀為 [batch_size, 64, length]，其中 length 是根據音訊持續時間和取樣率計算而得。輸出還包含中繼資料，指出類型為「audio」，時間降取樣比例為 2048。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6ca63d26febe2d87ff751a57044eb81b553b19756f4b3f9478ecb5a733ec0041`
