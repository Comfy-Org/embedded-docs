> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToMaxDimension/zh-TW.md)

ImageScaleToMaxDimension 節點可將圖像調整尺寸以符合指定的最大維度，同時保持原始長寬比。它會計算圖像是直向還是橫向取向，然後將較大的維度縮放至目標尺寸，並按比例調整較小的維度。此節點支援多種放大方法，以滿足不同的品質和效能需求。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 要進行縮放的輸入圖像 |
| `upscale_method` | STRING | 是 | "area"<br>"lanczos"<br>"bilinear"<br>"nearest-exact"<br>"bicubic" | 用於圖像縮放的插值方法 |
| `largest_size` | INT | 是 | 0 至 16384 | 縮放後圖像的最大維度（預設值：512） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `image` | IMAGE | 最大維度符合指定尺寸的縮放後圖像 |