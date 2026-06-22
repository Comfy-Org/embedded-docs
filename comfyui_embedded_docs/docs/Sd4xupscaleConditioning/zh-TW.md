# Sd4xupscaleConditioning

此節點專門負責透過 4 倍放大流程來提升影像解析度，並結合條件控制元素來優化輸出結果。它利用擴散技術進行影像放大，同時允許調整縮放比例和噪聲增強參數，以微調強化過程。

## 輸入

| 參數 | 說明 | Comfy 資料類型 |
| --- | --- | --- |
| `images` | 待放大的輸入影像。此參數至關重要，會直接影響輸出影像的品質與解析度。 | `IMAGE` |
| `positive` | 引導放大流程趨向輸出影像中理想屬性或特徵的正面條件控制元素。 | `CONDITIONING` |
| `negative` | 放大流程應避免的負面條件控制元素，有助於使輸出結果遠離不理想的屬性或特徵。 | `CONDITIONING` |
| `scale_ratio` | 決定影像解析度提升的倍率。較高的縮放比例會產生更大的輸出影像，從而呈現更多細節與清晰度。 | `FLOAT` |
| `noise_augmentation` | 控制放大過程中應用的噪聲增強程度。可用於引入變異性，並提升輸出影像的穩健性。 | `FLOAT` |

## 輸出

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `positive` | 經放大流程處理後，經過優化的正面條件控制元素。 | `CONDITIONING` |
| `negative` | 經放大流程處理後，經過優化的負面條件控制元素。 | `CONDITIONING` |
| `latent` | 放大過程中產生的潛在表示，可用於後續處理或模型訓練。 | `LATENT` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Sd4xupscaleConditioning/zh-TW.md)
