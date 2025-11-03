> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeAndPadImage/zh-TW.md)

ResizeAndPadImage 節點會將圖片調整大小以符合指定尺寸，同時保持其原始長寬比。它會按比例縮小圖片以符合目標寬度和高度，然後在邊緣周圍添加填充以填補任何剩餘空間。填充顏色和插值方法可以自定義，以控制填充區域的外觀和調整大小的品質。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 要進行調整大小和填充的輸入圖片 |
| `target_width` | INT | 是 | 1 至 MAX_RESOLUTION | 輸出圖片的期望寬度（預設值：512） |
| `target_height` | INT | 是 | 1 至 MAX_RESOLUTION | 輸出圖片的期望高度（預設值：512） |
| `padding_color` | COMBO | 是 | "white"<br>"black" | 用於調整大小後圖片周圍填充區域的顏色 |
| `interpolation` | COMBO | 是 | "area"<br>"bicubic"<br>"nearest-exact"<br>"bilinear"<br>"lanczos" | 用於調整圖片大小的插值方法 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `image` | IMAGE | 經過調整大小和填充處理後的輸出圖片 |