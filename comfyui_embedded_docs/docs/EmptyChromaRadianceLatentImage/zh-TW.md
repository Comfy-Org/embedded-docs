# EmptyChromaRadianceLatentImage

EmptyChromaRadianceLatentImage 節點會建立一個具有指定尺寸的空白潛在圖像，用於色度輝光工作流程。它會產生一個填充零的張量，作為潛在空間運算的起點。此節點可讓您定義空白潛在圖像的寬度、高度與批次大小。

## 輸入
| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `寬度` | 潛在圖像的寬度（像素）（預設值：1024，必須能被 16 整除） | INT | 是 | 16 to MAX_RESOLUTION |
| `高度` | 潛在圖像的高度（像素）（預設值：1024，必須能被 16 整除） | INT | 是 | 16 to MAX_RESOLUTION |
| `批次大小` | 批次中要生成的潛在圖像數量（預設值：1） | INT | 否 | 1 至 4096 |

注意：`width` 與 `height` 以 16 為步長定義，因此它們必須是 16 的倍數。

## 輸出
| 輸出名 | 描述 | 資料型別 |
| --- | --- | --- |
| `samples` | 產生的空白潛在圖像張量，填充零，形狀為 batch_size x 3 x height x width | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `870cc89fb021c258c214db153cda0a32a63da1b6bf92f09cbd3b8498c363096b`
