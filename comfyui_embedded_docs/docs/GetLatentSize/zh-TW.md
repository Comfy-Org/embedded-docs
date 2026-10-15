# Get Image/Video Latent Size

讀取影像或視訊 latent，並傳回其寬度、高度、影格數與批次大小，因此無須解碼 latent 即可重複使用其幾何資訊。可用於調整雜訊遮罩大小、對齊解析度，或在為取樣器分塊時計算重疊區域。這些測量值也會顯示在節點本身上。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `latent` | 要檢查的影像或視訊 latent。當 latent 包含多個串流時，會測量第一個。 | LATENT | 是 | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `width` | latent 的寬度，以 latent 單元而非像素為單位。 | INT |
| `height` | latent 的高度，以 latent 單元而非像素為單位。 | INT |
| `frames` | latent 中的影格數。影像 latent 只有單一影格。 | INT |
| `batch_size` | 批次中的 latent 數量。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetLatentSize/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f75b3347cb1853b035b0bb283d5487ab1532d561d66d3cae3c67f54bf693d31a`
