> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/zh-TW.md)

## 概述

此節點將 LATENT（例如來自 VOIDWarpedNoise 節點的輸出）轉換為 NOISE 來源。這讓您能將扭曲噪聲與 SamplerCustomAdvanced 節點搭配使用，以實現更可控的影像生成。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `warped_noise` | LATENT | 是 | N/A | 來自 VOIDWarpedNoise 的扭曲噪聲潛在空間 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `NOISE` | NOISE | 可與 SamplerCustomAdvanced 搭配使用的噪聲來源 |