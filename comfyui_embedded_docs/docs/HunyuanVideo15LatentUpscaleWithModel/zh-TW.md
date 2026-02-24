> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/zh-TW.md)

Hunyuan Video 15 Latent Upscale With Model 節點用於提升潛空間影像表徵的解析度。它首先使用選定的插值方法將潛空間樣本放大到指定尺寸，然後使用專門的 Hunyuan Video 1.5 放大模型來精煉放大後的結果，以提升品質。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | LATENT_UPSCALE_MODEL | 是 | N/A | 用於精煉放大後樣本的 Hunyuan Video 1.5 潛空間放大模型。 |
| `samples` | LATENT | 是 | N/A | 待放大的潛空間影像表徵。 |
| `upscale_method` | COMBO | 否 | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` | 用於初始放大步驟的插值演算法（預設：`"bilinear"`）。 |
| `width` | INT | 否 | 0 至 16384 | 放大後潛空間影像的目標寬度，單位為像素。設為 0 時，將根據目標高度和原始長寬比自動計算寬度。最終輸出寬度將是 16 的倍數（預設：1280）。 |
| `height` | INT | 否 | 0 至 16384 | 放大後潛空間影像的目標高度，單位為像素。設為 0 時，將根據目標寬度和原始長寬比自動計算高度。最終輸出高度將是 16 的倍數（預設：720）。 |
| `crop` | COMBO | 否 | `"disabled"`<br>`"center"` | 決定如何裁剪放大後的潛空間影像以符合目標尺寸。 |

**關於尺寸的注意事項：** 如果 `width` 和 `height` 均設為 0，節點將返回未經更改的輸入 `samples`。如果僅有一個維度設為 0，則另一個維度會被計算以保持原始長寬比。最終尺寸總會被調整為至少 64 像素，並且是 16 的倍數。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `LATENT` | LATENT | 經過放大和模型精煉後的潛空間影像表徵。 |
