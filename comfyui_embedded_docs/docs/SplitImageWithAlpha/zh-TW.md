> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageWithAlpha/zh-TW.md)

SplitImageWithAlpha 節點專門用於分離影像的色彩與透明度元件。它會處理輸入的影像張量，提取 RGB 通道作為色彩元件，並提取 Alpha 通道作為透明度元件，方便後續需要分別處理這些影像屬性的操作。

## 輸入參數

| 參數名稱 | 資料類型 | 描述 |
|-----------|-------------|-------------|
| `影像`   | `IMAGE`     | 此 `image` 參數代表輸入的影像張量，系統將從中分離出 RGB 與 Alpha 通道。此參數對操作至關重要，因為它提供了分離處理的源數據。 |

## 輸出參數

| 參數名稱 | 資料類型 | 描述 |
|-----------|-------------|-------------|
| `影像`   | `IMAGE`     | 此 `image` 輸出代表輸入影像經分離後的 RGB 通道，提供不含透明度資訊的色彩元件。 |
| `mask`    | `MASK`      | 此 `mask` 輸出代表輸入影像經分離後的 Alpha 通道，提供透明度資訊。 |