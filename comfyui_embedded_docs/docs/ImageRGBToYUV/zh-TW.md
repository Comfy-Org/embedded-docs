> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/zh-TW.md)

ImageRGBToYUV 節點將 RGB 彩色影像轉換為 YUV 色彩空間。它接收 RGB 影像作為輸入，並將其分離為三個不同的通道：Y（亮度）、U（藍色投影）和 V（紅色投影）。每個輸出通道均以獨立的灰階影像形式返回，代表對應的 YUV 分量。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 要轉換至 YUV 色彩空間的輸入 RGB 影像 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `Y` | IMAGE | YUV 色彩空間中的亮度分量 |
| `U` | IMAGE | YUV 色彩空間中的藍色投影分量 |
| `V` | IMAGE | YUV 色彩空間中的紅色投影分量 |