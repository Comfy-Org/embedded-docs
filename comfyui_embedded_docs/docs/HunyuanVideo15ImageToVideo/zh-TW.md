> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15ImageToVideo/zh-TW.md)

### HunyuanVideo15ImageToVideo 節點

此節點基於 HunyuanVideo 1.5 模型，為影片生成準備條件化（conditioning）與潛在空間（latent space）資料。它會為影片序列建立初始的潛在表示，並可選擇性地整合起始影像或 CLIP 視覺輸出，以引導生成過程。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 正向條件化提示詞，描述影片應包含的內容。 |
| `negative` | CONDITIONING | 是 | - | 負向條件化提示詞，描述影片應避免的內容。 |
| `vae` | VAE | 是 | - | 用於將起始影像編碼至潛在空間的 VAE（變分自編碼器）模型。 |
| `width` | INT | 否 | 16 至 MAX_RESOLUTION | 輸出影片幀的寬度（像素）。必須能被 16 整除。（預設值：848） |
| `height` | INT | 否 | 16 至 MAX_RESOLUTION | 輸出影片幀的高度（像素）。必須能被 16 整除。（預設值：480） |
| `length` | INT | 否 | 1 至 MAX_RESOLUTION | 影片序列的總幀數。必須是 4 的倍數。（預設值：33） |
| `batch_size` | INT | 否 | 1 至 4096 | 單一批次中生成的影片序列數量。（預設值：1） |
| `start_image` | IMAGE | 否 | - | 可選的起始影像，用於初始化影片生成。若提供，該影像將被編碼並用於條件化前幾幀。僅使用影像的前 `length` 幀。 |
| `clip_vision_output` | CLIP_VISION_OUTPUT | 否 | - | 可選的 CLIP 視覺嵌入，為生成過程提供額外的視覺條件化。 |

**注意：** 當提供 `start_image` 時，系統會自動使用雙線性插值將其調整為指定的 `width` 與 `height`。僅使用影像批次的前 `length` 幀。編碼後的影像會以 `concat_latent_image` 形式，連同對應的 `concat_mask`，同時添加到 `positive` 與 `negative` 條件化中。起始影像所涵蓋的幀，其遮罩設為 0.0；其餘幀則設為 1.0。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `negative` | CONDITIONING | 修改後的正向條件化，可能已包含編碼後的起始影像或 CLIP 視覺輸出。 |
| `latent` | CONDITIONING | 修改後的負向條件化，可能已包含編碼後的起始影像或 CLIP 視覺輸出。 |
| `latent` | LATENT | 一個空的潛在張量，其維度已根據指定的批次大小、影片長度、寬度與高度進行配置。 |

---
**Source fingerprint (SHA-256):** `2f41bbb080672683fb1755be575f08c79ca03e324df66953eb40631581197d47`
