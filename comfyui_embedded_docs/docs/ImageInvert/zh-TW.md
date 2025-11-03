> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageInvert/zh-TW.md)

{heading_overview}

`ImageInvert` 節點旨在反轉影像的色彩，有效地將每個像素的色彩值轉換為其在色輪上的互補色。此操作適用於建立負片影像或需要色彩反轉的視覺效果。

{heading_inputs}

| 參數名稱 | 資料類型 | 描述 |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | `image` 參數代表要進行反轉的輸入影像。此參數對於指定目標影像至關重要，其色彩將被反轉，影響節點的執行過程以及反轉處理的視覺結果。 |

{heading_outputs}

| 參數名稱 | 資料類型 | 描述 |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | 輸出為輸入影像的反轉版本，其中每個像素的色彩值均已轉換為其互補色。 |