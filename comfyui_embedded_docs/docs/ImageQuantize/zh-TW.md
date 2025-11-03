> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageQuantize/zh-TW.md)

{heading_overview}

ImageQuantize 節點旨在將影像中的顏色數量減少到指定數量，並可選擇性地應用抖動技術以維持視覺品質。此處理程序對於建立基於調色盤的影像或為特定應用降低色彩複雜度非常有用。

{heading_inputs}

| 欄位 | 資料類型 | 描述 |
|------|-----------|-------------|
| `image` | `IMAGE` | 要進行量化的輸入影像張量。它作為色彩減少處理的主要資料，影響節點的執行。 |
| `colors` | `INT` | 指定要將影像減少到的顏色數量。它通過決定調色盤大小直接影響量化過程。 |
| `dither` | COMBO[STRING] | 決定在量化過程中要應用的抖動技術，影響輸出影像的視覺品質和外觀。 |

{heading_outputs}

| 欄位 | 資料類型 | 描述 |
|------|-----------|-------------|
| `image` | `IMAGE` | 輸入影像的量化版本，具有降低的色彩複雜度，並可選擇性地應用抖動以維持視覺品質。 |