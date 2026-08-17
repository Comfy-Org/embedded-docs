# EmptySD3LatentImage

The EmptySD3LatentImage 節點會建立一個專為 Stable Diffusion 3 模型格式化的空白潛在影像張量。它會產生一個充滿零的張量，其維度與結構符合 SD3 管線的預期。這通常用作影像生成工作流程的起點。

## 輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `width` | 輸出潛在影像的寬度（像素）（預設：1024） | INT | 是 | 16 to MAX_RESOLUTION (step: 16) |
| `height` | 輸出潛在影像的高度（像素）（預設：1024） | INT | 是 | 16 to MAX_RESOLUTION (step: 16) |
| `batch_size` | 每批生成的潛在影像數量（預設：1） | INT | 是 | 1 to 4096 |

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
| --- | --- | --- |
| `LATENT` | 包含具 SD3 相容維度之空白樣本的潛在張量。此張量有 16 個通道，空間尺寸相較於輸入寬高縮小 8 倍。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptySD3LatentImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `694ede56f43e3f3889b4d23e636fa6b33b490bcbd214584557f0dc883fa0a32d`
