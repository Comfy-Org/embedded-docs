> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageSharpen/zh-TW.md)

{heading_overview}

ImageSharpen 節點透過強化影像邊緣和細節來提升影像清晰度。它對影像應用銳化濾鏡，可調整強度和半徑，使影像看起來更加清晰銳利。

{heading_inputs}

| 欄位名稱 | 資料類型 | 描述 |
|----------|-----------|-------|
| `image` | `IMAGE` | 要進行銳化處理的輸入影像。此參數至關重要，因為它決定了將應用銳化效果的基礎影像。 |
| `sharpen_radius` | `INT` | 定義銳化效果的半徑。較大的半徑意味著邊緣周圍的更多像素將受到影響，從而產生更明顯的銳化效果。 |
| `sigma` | `FLOAT` | 控制銳化效果的擴散範圍。較高的 sigma 值會使邊緣過渡更平滑，而較低的 sigma 則會使銳化效果更加局部化。 |
| `alpha` | `FLOAT` | 調整銳化效果的強度。較高的 alpha 值會產生更強的銳化效果。 |

{heading_outputs}

| 欄位名稱 | 資料類型 | 描述 |
|----------|-----------|-------|
| `image` | `IMAGE` | 經過銳化處理的影像，具有增強後的邊緣和細節，可進行後續處理或顯示。 |