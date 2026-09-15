# EmptyChromaRadianceLatentImage

EmptyChromaRadianceLatentImage 節點會建立一個具有你指定尺寸的空白潛在影像，用於 chroma radiance 工作流程。它會產生一個填充零的張量，作為潛空間操作的起始點，讓你可以定義空白潛在影像的 `width`、`height` 與 `batch_size`。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `寬度` | 潛在影像的寬度，以像素為單位（預設值：1024） | INT | 是 | 16 to MAX_RESOLUTION |
| `高度` | 潛在影像的高度，以像素為單位（預設值：1024） | INT | 是 | 16 to MAX_RESOLUTION |
| `批次大小` | 一個批次中要產生的潛在影像數量（預設值：1） | INT | 是 | 1 至 4096 |

注意：`width` 與 `height` 以步長 16 定義，因此數值會以 16 的倍數進行調整。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `samples` | 產生的空白潛在影像張量，填充零，形狀為 batch_size x 3 x height x width | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `870cc89fb021c258c214db153cda0a32a63da1b6bf92f09cbd3b8498c363096b`
