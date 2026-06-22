# 以 Alpha 通道分割影像

SplitImageWithAlpha 節點旨在分離圖像的色彩和透明度分量。它處理輸入的圖像張量，提取 RGB 通道作為色彩分量，以及 Alpha 通道作為透明度分量，以便於需要分別操作這些不同圖像方面的處理流程。

## 輸入

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `影像` | 'image' 參數代表要從中分離 RGB 和 Alpha 通道的輸入圖像張量。此參數對於操作至關重要，因為它提供了分割所需的來源資料。 | `IMAGE` |

## 輸出

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `影像` | 'image' 輸出代表輸入圖像中分離出的 RGB 通道，提供不含透明度資訊的色彩分量。 | `IMAGE` |
| `mask` | 'mask' 輸出代表輸入圖像中分離出的 Alpha 通道，提供透明度資訊。 | `MASK` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageWithAlpha/zh-TW.md)
