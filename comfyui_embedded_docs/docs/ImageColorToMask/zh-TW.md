> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorToMask/zh-TW.md)

{heading_overview}

`ImageColorToMask` 節點旨在將圖像中的指定顏色轉換為遮罩。它處理圖像和目標顏色，生成一個突出顯示指定顏色的遮罩，便於進行基於顏色的分割或物件隔離等操作。

{heading_inputs}

| 參數名稱 | 資料類型 | 描述 |
|-----------|-------------|-------------|
| `圖片`   | `IMAGE`     | 此 `image` 參數代表要處理的輸入圖像。它對於確定圖像中與指定顏色匹配的區域至關重要，這些區域將被轉換為遮罩。 |
| `顏色`   | `INT`       | 此 `color` 參數指定圖像中要轉換為遮罩的目標顏色。它在識別結果遮罩中要突出顯示的特定顏色區域方面起著關鍵作用。 |

{heading_outputs}

| 參數名稱 | 資料類型 | 描述 |
|-----------|-------------|-------------|
| `mask`    | `MASK`      | 輸出是一個遮罩，突出顯示輸入圖像中與指定顏色匹配的區域。此遮罩可用於進一步的圖像處理任務，例如分割或物件隔離。 |