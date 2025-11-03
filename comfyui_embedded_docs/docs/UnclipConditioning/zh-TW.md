> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/unCLIPConditioning/zh-TW.md)

此節點旨在將 CLIP 視覺輸出整合到條件化過程中，根據指定的強度和噪聲增強參數調整這些輸出的影響力。它透過視覺上下文豐富了條件化數據，從而增強生成過程。

## 輸入參數

| 參數名稱               | Comfy 資料類型          | 描述 |
|------------------------|------------------------|-------------|
| `conditioning`         | `CONDITIONING`         | 基礎條件化數據，將在此基礎上添加 CLIP 視覺輸出，作為後續修改的基礎。 |
| `clip_vision_output`   | `CLIP_VISION_OUTPUT`   | 來自 CLIP 視覺模型的輸出，提供將被整合到條件化中的視覺上下文。 |
| `strength`             | `FLOAT`                | 決定 CLIP 視覺輸出對條件化影響的強度。 |
| `noise_augmentation`   | `FLOAT`                | 指定在將 CLIP 視覺輸出整合到條件化之前，對其應用的噪聲增強程度。 |

## 輸出參數

| 參數名稱              | Comfy 資料類型          | 描述 |
|-----------------------|------------------------|-------------|
| `conditioning`         | `CONDITIONING`         | 經過增強的條件化數據，現在包含已應用強度和噪聲增強的整合 CLIP 視覺輸出。 |