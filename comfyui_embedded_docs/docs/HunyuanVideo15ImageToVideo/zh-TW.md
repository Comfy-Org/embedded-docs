# HunyuanVideo15ImageToVideo

### HunyuanVideo15ImageToVideo 節點

此節點根據 HunyuanVideo 1.5 模型，為影片生成準備 conditioning 與潛在空間資料。它會為影片序列建立初始潛在表示，並可選擇性地整合起始影像或 CLIP 視覺輸出，以引導生成過程。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 正向 conditioning 提示，用於描述影片應包含的內容。 | CONDITIONING | 是 | - |
| `negative` | 負向 conditioning 提示，用於描述影片應避免的內容。 | CONDITIONING | 是 | - |
| `vae` | 用於將起始影像編碼至潛在空間的 VAE（變分自編碼器）模型。 | VAE | 是 | - |
| `width` | 輸出影片影格的寬度（像素）。必須能被 16 整除。（預設值：848） | INT | 是 | 16 至 MAX_RESOLUTION，步長：16 |
| `height` | 輸出影片影格的高度（像素）。必須能被 16 整除。（預設值：480） | INT | 是 | 16 至 MAX_RESOLUTION，步長：16 |
| `length` | 影片序列中的總影格數。此值以 4 為步長增加。（預設值：33） | INT | 是 | 1 至 MAX_RESOLUTION，步長：4 |
| `batch_size` | 單一批次中要生成的影片序列數量。（預設值：1） | INT | 是 | 1 至 4096 |
| `start_image` | 可選的起始影像，用於初始化影片生成。若提供，則會對其進行編碼，並用於條件化前幾個影格。僅使用影像的前 `length` 個影格。 | IMAGE | 否 | - |
| `clip_vision_output` | 可選的 CLIP 視覺嵌入，用於為生成過程提供額外的視覺條件化。 | CLIP_VISION_OUTPUT | 否 | - |

**注意：** 當提供 `start_image` 時，它會自動使用雙線性插值調整大小，以符合指定的 `width` 和 `height`，且僅使用其 RGB 色頻。系統會使用影像批次的前 `length` 個影格。然後，編碼後的影像會以 `concat_latent_image` 的形式，並搭配對應的 `concat_mask`，同時添加到 `positive` 和 `negative` conditioning 中。對於起始影像涵蓋的影格，遮罩設為 0.0；對於其餘影格，遮罩設為 1.0。當提供 `clip_vision_output` 時，它也會同時添加到 `positive` 和 `negative` conditioning 中。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `positive` | 修改後的 positive conditioning，現在可能包含編碼後的起始影像或 CLIP 視覺輸出。 | CONDITIONING |
| `negative` | 修改後的 negative conditioning，現在可能包含編碼後的起始影像或 CLIP 視覺輸出。 | CONDITIONING |
| `latent` | 一個空的潛在張量，其維度已針對指定的批次大小、影片長度、寬度和高度進行設定。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15ImageToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `dbedf7f378ae9613c8f47fe9876a4576c815055b4cdb6bf687b7575fcd7ea80a`
