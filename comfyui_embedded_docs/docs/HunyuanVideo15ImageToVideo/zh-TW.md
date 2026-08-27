# HunyuanVideo15ImageToVideo

HunyuanVideo15ImageToVideo 節點基於 HunyuanVideo 1.5 模型，為影片生成準備條件化（conditioning）與潛在空間資料。它會建立影片序列的初始潛在表示，並可選擇性地整合起始影像或 CLIP 視覺輸出，以引導生成過程。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 描述影片應包含內容的正向條件化提示。 | CONDITIONING | 是 | - |
| `negative` | 描述影片應避免內容的負向條件化提示。 | CONDITIONING | 是 | - |
| `vae` | 用於將起始影像編碼到潛在空間的 VAE（變分自編碼器）模型。 | VAE | 是 | - |
| `width` | 輸出影片幀的寬度（像素）。必須能被 16 整除。（預設值：848） | INT | 是 | 16 to MAX_RESOLUTION, step: 16 |
| `height` | 輸出影片幀的高度（像素）。必須能被 16 整除。（預設值：480） | INT | 是 | 16 to MAX_RESOLUTION, step: 16 |
| `length` | 影片序列中的總幀數。數值從 1 開始，以 4 為步長遞增（1, 5, 9, 13, ...）。（預設值：33） | INT | 是 | 1 to MAX_RESOLUTION, step: 4 |
| `batch_size` | 單一批次中要生成的影片序列數量。（預設值：1） | INT | 是 | 1 至 4096 |
| `start_image` | 可選的起始影像，用於初始化影片生成。若提供，則會編碼該影像並用於條件化前幾個幀。僅使用影像的前 `length` 個幀。 | IMAGE | No | - |
| `clip_vision_output` | 可選的 CLIP 視覺嵌入，可為生成提供額外的視覺條件化。 | CLIP_VISION_OUTPUT | No | - |

**附註：** 當提供 `start_image` 時，它會自動使用雙線性插值調整大小，以符合指定的 `width` 和 `height`。會使用影像批次的前 `length` 個幀，且每個幀僅編碼前 3 個色彩通道。接著，編碼後的影像會以 `concat_latent_image` 的形式及對應的 `concat_mask` 新增到 `positive` 和 `negative` 條件化中。對於起始影像所涵蓋的幀，遮罩設為 0.0；其餘幀則設為 1.0。當提供 `clip_vision_output` 時，它也會新增到 `positive` 和 `negative` 條件化中。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 修改後的正向條件化，現在可能包含已編碼的起始影像或 CLIP 視覺輸出。 | CONDITIONING |
| `negative` | 修改後的負向條件化，現在可能包含已編碼的起始影像或 CLIP 視覺輸出。 | CONDITIONING |
| `latent` | 一個空的潛在張量，其維度依據指定的批次大小、影片長度、寬度和高度配置。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15ImageToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `dbedf7f378ae9613c8f47fe9876a4576c815055b4cdb6bf687b7575fcd7ea80a`
