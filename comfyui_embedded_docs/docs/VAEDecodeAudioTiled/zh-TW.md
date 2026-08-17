# VAE 解碼音訊（分塊）

此節點使用變分自編碼器（VAE），將壓縮的音訊表示（潛在樣本）轉換回音訊波形。它會以較小且重疊的區段（tiles）處理資料，以管理記憶體使用量，因此適合處理較長音訊序列。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `samples` | 要解碼的音訊壓縮潛在表示。 | LATENT | 是 | N/A |
| `vae` | 用於執行解碼的變分自編碼器模型。 | VAE | 是 | N/A |
| `tile_size` | 每個處理區段的大小。音訊以此長度分段解碼，以節省記憶體（預設值：512）。 | INT | 是 | 32 至 8192 |
| `overlap` | 相鄰區段重疊的樣本數。這有助於減少區段邊界處的偽影（預設值：64）。 | INT | 是 | 0 至 1024 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 解碼後的音訊波形。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudioTiled/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5ddedf218ba27ab9f463646c1e5288091172f2d7fae8f2980bb2b5e4d3dca89c`
