# EmptySD3LatentImage

EmptySD3LatentImage 會在 Stable Diffusion 3 模型預期的佈局中建立一個空白（全零）的潛在影像。由於此潛在表示為空，它通常會作為生成工作流程填入影像的起始點。您選擇的 `width` 與 `height` 會決定最終影像的尺寸。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `寬度` | 潛在影像的寬度，以像素為單位（預設：1024）。數值以 16 為增量。 | INT | 是 | 16 到 MAX_RESOLUTION（步長：16） |
| `高度` | 潛在影像的高度，以像素為單位（預設：1024）。數值以 16 為增量。 | INT | 是 | 16 到 MAX_RESOLUTION（步長：16） |
| `批次大小` | 批次中要產生的潛在影像數量（預設：1）。 | INT | 是 | 1 到 4096 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 一個潛在張量，包含 SD3 相容格式的空白（全零）樣本。此張量具有 16 個通道，相對於 `width` 和 `height` 縮小 8 倍，並帶有 8 的空間下採樣比例。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptySD3LatentImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `694ede56f43e3f3889b4d23e636fa6b33b490bcbd214584557f0dc883fa0a32d`
