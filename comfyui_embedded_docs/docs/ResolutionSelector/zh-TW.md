> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionSelector/zh-TW.md)

Resolution Selector 節點會根據選擇的長寬比和以百萬像素為單位的目標總解析度，計算圖像的像素寬度和高度。它對於為其他節點（例如 Empty Latent Image 節點）生成一致的尺寸非常有用。輸出的尺寸總是會四捨五入到最接近的 8 的倍數。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `aspect_ratio` | COMBO | 是 | `"SQUARE"`<br>`"PORTRAIT_2_3"`<br>`"PORTRAIT_3_4"`<br>`"PORTRAIT_9_16"`<br>`"LANDSCAPE_3_2"`<br>`"LANDSCAPE_4_3"`<br>`"LANDSCAPE_16_9"` | 輸出尺寸的長寬比（預設值：`"SQUARE"`）。 |
| `megapixels` | FLOAT | 是 | 0.1 - 16.0 | 目標總百萬像素數。對於正方形長寬比，1.0 MP 約等於 1024×1024（預設值：1.0）。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `width` | INT | 計算出的像素寬度，為 8 的倍數。 |
| `height` | INT | 計算出的像素高度，為 8 的倍數。 |