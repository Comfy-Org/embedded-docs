> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/zh-TW.md)

WanFirstLastFrameToVideo 節點透過結合起始與結束畫面及文字提示來建立影片條件。它透過編碼首尾畫面、應用遮罩來引導生成過程，並在可用時整合 CLIP 視覺特徵，從而為影片生成產生潛在表徵。此節點為影片模型準備正向與負向條件，以在指定的起始點與結束點之間生成連貫的序列。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `正向` | CONDITIONING | 是 | - | 用於引導影片生成的正向文字條件 |
| `負向` | CONDITIONING | 是 | - | 用於引導影片生成的負向文字條件 |
| `vae` | VAE | 是 | - | 用於將影像編碼至潛在空間的 VAE 模型 |
| `寬度` | INT | 否 | 16 至 MAX_RESOLUTION | 輸出影片寬度（預設值：832，間隔：16） |
| `高度` | INT | 否 | 16 至 MAX_RESOLUTION | 輸出影片高度（預設值：480，間隔：16） |
| `長度` | INT | 否 | 1 至 MAX_RESOLUTION | 影片序列中的畫面數量（預設值：81，間隔：4） |
| `批次大小` | INT | 否 | 1 至 4096 | 同時生成的影片數量（預設值：1） |
| `clip 視覺起始影像` | CLIP_VISION_OUTPUT | 否 | - | 從起始影像提取的 CLIP 視覺特徵 |
| `clip 視覺結束影像` | CLIP_VISION_OUTPUT | 否 | - | 從結束影像提取的 CLIP 視覺特徵 |
| `起始影像` | IMAGE | 否 | - | 影片序列的起始畫面影像 |
| `結束影像` | IMAGE | 否 | - | 影片序列的結束畫面影像 |

**注意：** 當同時提供 `start_image` 和 `end_image` 時，節點會建立在這兩個畫面之間轉換的影片序列。`clip_vision_start_image` 和 `clip_vision_end_image` 參數為可選，但若提供時，其 CLIP 視覺特徵將被串接並應用至正向與負向條件。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `負向` | CONDITIONING | 已應用影片畫面編碼與 CLIP 視覺特徵的正向條件 |
| `潛在空間` | CONDITIONING | 已應用影片畫面編碼與 CLIP 視覺特徵的負向條件 |
| `latent` | LATENT | 符合指定影片參數維度的空潛在張量 |