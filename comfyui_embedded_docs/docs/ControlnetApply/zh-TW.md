> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApply/zh-TW.md)

## ## 概述

使用 ControlNet 需要對輸入圖像進行預處理。由於 ComfyUI 初始節點不包含預處理器和 ControlNet 模型，請先安裝 ControlNet 預處理器[在此下載預處理器](https://github.com/Fannovel16/comfy_controlnet_preprocessors)以及相應的 ControlNet 模型。

## ## 輸入

| 參數 | 資料類型 | 功能說明 |
| --- | --- | --- |
| `positive` | `CONDITIONING` | 正面條件資料，來自 CLIP 文字編碼器或其他條件輸入 |
| `negative` | `CONDITIONING` | 負面條件資料，來自 CLIP 文字編碼器或其他條件輸入 |
| `control_net` | `CONTROL_NET` | 要應用的 ControlNet 模型，通常從 ControlNet 載入器輸入 |
| `影像` | `IMAGE` | 用於 ControlNet 應用的圖像，需要經過預處理器處理 |
| `vae` | `VAE` | VAE 模型輸入 |
| `強度` | `FLOAT` | 控制網路調整的強度，數值範圍 0~10。建議值在 0.5~1.5 之間較為合理。較低的值允許模型有更多自由度，較高的值則施加更嚴格的約束。過高的值可能導致圖像異常。您可以測試並調整此值來微調控制網路的影響程度。 |
| `start_percent` | `FLOAT` | 數值 0.000~1.000，決定何時開始應用 ControlNet 的百分比，例如 0.2 表示 ControlNet 引導將在擴散過程的 20% 時開始影響圖像生成 |
| `end_percent` | `FLOAT` | 數值 0.000~1.000，決定何時停止應用 ControlNet 的百分比，例如 0.8 表示 ControlNet 引導將在擴散過程的 80% 時停止影響圖像生成 |

## ## 輸出

| 參數 | 資料類型 | 功能說明 |
| --- | --- | --- |
| `positive` | `CONDITIONING` | 經 ControlNet 處理後的正面條件資料，可輸出到下一個 ControlNet 或 K Sampler 節點 |
| `negative` | `CONDITIONING` | 經 ControlNet 處理後的負面條件資料，可輸出到下一個 ControlNet 或 K Sampler 節點 |