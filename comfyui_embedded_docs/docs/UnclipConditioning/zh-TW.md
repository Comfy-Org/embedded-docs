此節點旨在將 CLIP 視覺輸出整合到條件化過程中，並根據指定的強度與噪聲增強參數調整這些輸出的影響力。它透過視覺上下文豐富條件化內容，從而強化生成過程。

## 輸入

| 參數 | 說明 | Comfy 資料類型 |
| --- | --- | --- |
| `條件設定` | 基礎條件化數據，CLIP 視覺輸出將被添加至此數據中，作為後續修改的基礎。 | `CONDITIONING` |
| `clip_vision_output` | 來自 CLIP 視覺模型的輸出，提供整合至條件化過程中的視覺上下文。 | `CLIP_VISION_OUTPUT` |
| `強度` | 決定 CLIP 視覺輸出對條件化過程的影響強度。 | `FLOAT` |
| `雜訊增強` | 指定在將 CLIP 視覺輸出整合至條件化過程之前，要應用的噪聲增強程度。 | `FLOAT` |

## 輸出

| 參數 | 說明 | Comfy 資料類型 |
| --- | --- | --- |
| `條件設定` | 經過強化的條件化數據，現已包含整合後的 CLIP 視覺輸出，並應用了指定的強度與噪聲增強。 | `CONDITIONING` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/unCLIPConditioning/zh-TW.md)
