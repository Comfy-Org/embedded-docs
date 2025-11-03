> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImagePadForOutpaint/zh-TW.md)

{heading_overview}

此節點旨在為外繪製過程準備圖像，透過在圖像周圍添加填充區域。它會調整圖像尺寸以確保與外繪製演算法的兼容性，便於在原始邊界之外生成擴展的圖像區域。

{heading_inputs}

| 參數 | 資料類型 | 描述 |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | 'image' 輸入是要為外繪製準備的主要圖像，作為填充操作的基礎。 |
| `left`    | `INT`       | 指定在圖像左側添加的填充量，影響外繪製的擴展區域。 |
| `top`     | `INT`       | 決定在圖像頂部添加的填充量，影響外繪製的垂直擴展。 |
| `right`   | `INT`       | 定義在圖像右側添加的填充量，影響外繪製的水平擴展。 |
| `bottom`  | `INT`       | 表示在圖像底部添加的填充量，有助於外繪製的垂直擴展。 |
| `feathering` | `INT` | 控制原始圖像與添加填充區域之間過渡的平滑度，增強外繪製的視覺整合效果。 |

{heading_outputs}

| 參數 | 資料類型 | 描述 |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | 輸出的 'image' 代表已填充的圖像，準備好用於外繪製過程。 |
| `mask`    | `MASK`      | 輸出的 'mask' 標示了原始圖像和添加填充區域的範圍，有助於引導外繪製演算法。 |