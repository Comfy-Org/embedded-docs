# EmptyCosmosLatentVideo

The EmptyCosmosLatentVideo node creates an empty latent video tensor with specified dimensions. It generates a zero-filled latent representation that can be used as a starting point for video generation workflows, with configurable width, height, length, and batch size parameters. The spatial dimensions of the latent are downsampled by a factor of 8.

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `width` | 潛在影片的寬度（像素）（預設值：1280，必須能被 16 整除） | INT | 是 | 16 to MAX_RESOLUTION |
| `height` | 潛在影片的高度（像素）（預設值：704，必須能被 16 整除） | INT | 是 | 16 to MAX_RESOLUTION |
| `length` | 潛在影片的幀數（預設值：121，必須能被 8 整除） | INT | 是 | 1 to MAX_RESOLUTION |
| `batch_size` | 一批次中要生成的潛在影片數量（預設值：1） | INT | 是 | 1 to 4096 |

潛在張量使用 16 個通道。空間維度相對於像素維度除以 8（height // 8, width // 8），幀數則壓縮為 ((length - 1) // 8) + 1 個潛在幀。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `samples` | 生成的零值空潛在影片張量。形狀：(batch_size, 16, ((length - 1) // 8) + 1, height // 8, width // 8) | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyCosmosLatentVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7ee194324b02367ed853f6d36bc51742081bac6a9469c4a619586e0560a1b33b`
