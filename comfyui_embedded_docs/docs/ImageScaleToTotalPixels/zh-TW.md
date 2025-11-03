> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToTotalPixels/zh-TW.md)

{heading_overview}

ImageScaleToTotalPixels 節點專為將影像調整至指定總像素數而設計，同時保持原始長寬比。它提供多種放大方法來達成目標像素數量。

{heading_inputs}

| 參數             | 資料類型        | 描述                                                                 |
|------------------|-----------------|----------------------------------------------------------------------|
| `image`          | `IMAGE`         | 要放大至指定總像素數的輸入影像。                                        |
| `upscale_method` | COMBO[STRING]   | 用於放大影像的方法。這會影響放大後影像的品質和特性。                    |
| `megapixels`     | `FLOAT`         | 影像的目標大小，單位為百萬像素。這決定了放大後影像的總像素數。           |

{heading_outputs}

| 參數    | 資料類型 | 描述                                                                 |
|---------|----------|----------------------------------------------------------------------|
| `image` | `IMAGE`  | 已放大的影像，具有指定的總像素數，並保持原始長寬比。                   |