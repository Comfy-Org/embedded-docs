# EmptyChromaRadianceLatentImage

EmptyChromaRadianceLatentImage 節點會建立具有指定維度的空白潛在影像，用於 chroma radiance 工作流程。它會產生一個填充為零（包含 3 個色彩通道）的張量，作為潛在空間運算的起點。此節點可讓您定義空潛在影像的寬度、高度和批次大小。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `width` | 潛在影像的寬度（像素）（預設值：1024，必須能被 16 整除） | INT | 是 | 16 to MAX_RESOLUTION |
| `height` | 潛在影像的高度（像素）（預設值：1024，必須能被 16 整除） | INT | 是 | 16 to MAX_RESOLUTION |
| `batch_size` | 批次中要生成的潛在影像數量（預設值：1） | INT | 否 | 1 to 4096 |

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `samples` | 生成的空潛在影像張量，具有指定維度，填充為零 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `870cc89fb021c258c214db153cda0a32a63da1b6bf92f09cbd3b8498c363096b`
