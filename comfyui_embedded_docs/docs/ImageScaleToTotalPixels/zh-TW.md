> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToTotalPixels/zh-TW.md)

# ImageScaleToTotalPixels 節點

ImageScaleToTotalPixels 節點專為將圖像調整至指定總像素數而設計，同時保持原始寬高比。它提供多種放大方法來達到所需的像素數量。

## 輸入參數

| 參數名稱 | 資料類型 | 描述 |
|----------|-----------|------|
| `影像` | IMAGE | 要放大至指定總像素數的輸入圖像。 |
| `放大方法` | COMBO[STRING] | 用於放大圖像的方法。這會影響放大後圖像的品質和特性。 |
| `百萬像素` | FLOAT | 以百萬像素為單位的目標圖像尺寸。這決定了放大後圖像的總像素數。 |

## 輸出參數

| 參數名稱 | 資料類型 | 描述 |
|----------|-----------|------|
| `影像` | IMAGE | 放大後的圖像，具有指定的總像素數並保持原始寬高比。 |