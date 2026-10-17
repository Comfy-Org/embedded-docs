# Get Audio Latent Size

讀取音訊潛在表示並回傳其長度、音訊通道數與批次大小，因此這些數值可在不解碼音訊的情況下重複使用。可用於設定雜訊遮罩的大小，或在取樣前讓音訊與影片長度相符。量測到的數值也會顯示在節點本身上。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `latent` | 要檢查的音訊或音訊/影片潛在表示。當潛在表示包含多個串流時，會量測音訊串流。 | LATENT | 是 | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `length` | 音訊潛在表示的長度，以潛在單元為單位，而非音訊樣本。 | INT |
| `audio_channels` | 音訊通道數。沒有音訊通道維度的潛在表示會回報一個通道。 | INT |
| `batch_size` | 批次中的潛在表示數量。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetAudioLatentSize/zh-TW.md)

---
**Source fingerprint (SHA-256):** `82bac0636a070d14a8845c3f4a5e73359c1d943ce223be3b93212ef25d44b1a8`
