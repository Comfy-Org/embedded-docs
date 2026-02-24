> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15ImageToVideo/zh-TW.md)

HunyuanVideo15ImageToVideo 節點為基於 HunyuanVideo 1.5 模型的影片生成準備條件設定和潛在空間資料。它為影片序列創建初始的潛在表示，並可選擇性地整合起始圖像或 CLIP 視覺輸出來引導生成過程。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 描述影片應包含內容的正向條件設定提示。 |
| `negative` | CONDITIONING | 是 | - | 描述影片應避免內容的負向條件設定提示。 |
| `vae` | VAE | 是 | - | 用於將起始圖像編碼到潛在空間的 VAE（變分自編碼器）模型。 |
| `width` | INT | 否 | 16 至 MAX_RESOLUTION | 輸出影片畫面的寬度（以像素為單位）。必須能被 16 整除。（預設值：848） |
| `height` | INT | 否 | 16 至 MAX_RESOLUTION | 輸出影片畫面的高度（以像素為單位）。必須能被 16 整除。（預設值：480） |
| `length` | INT | 否 | 1 至 MAX_RESOLUTION | 影片序列的總幀數。（預設值：33） |
| `batch_size` | INT | 否 | 1 至 4096 | 單一批次中要生成的影片序列數量。（預設值：1） |
| `start_image` | IMAGE | 否 | - | 用於初始化影片生成的可選起始圖像。若提供，將被編碼並用於條件設定起始幀。 |
| `clip_vision_output` | CLIP_VISION_OUTPUT | 否 | - | 可選的 CLIP 視覺嵌入，為生成提供額外的視覺條件設定。 |

**注意：** 當提供 `start_image` 時，它會使用雙線性插值自動調整大小以匹配指定的 `width` 和 `height`。圖像批次的前 `length` 幀將被使用。編碼後的圖像隨後會作為 `concat_latent_image` 連同對應的 `concat_mask` 添加到 `positive` 和 `negative` 條件設定中。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 修改後的正向條件設定，現在可能包含編碼後的起始圖像或 CLIP 視覺輸出。 |
| `negative` | CONDITIONING | 修改後的負向條件設定，現在可能包含編碼後的起始圖像或 CLIP 視覺輸出。 |
| `latent` | LATENT | 一個空的潛在張量，其維度已根據指定的批次大小、影片長度、寬度和高度進行配置。 |
