使用 controlNet 需要對輸入圖像進行預處理。由於 ComfyUI 初始節點不附帶預處理器和 controlNet 模型，請先安裝 ControlNet 預處理器 [在此處下載預處理器](https://github.com/Fannovel16/comfy_controlnet_preprocessors) 以及相應的 controlNet 模型。

## 輸入

| 參數 | 功能說明 | 資料類型 |
| --- | --- | --- |
| `positive` | 正向條件資料，來自 CLIP 文字編碼器或其他條件輸入 | `CONDITIONING` |
| `negative` | 負向條件資料，來自 CLIP 文字編碼器或其他條件輸入 | `CONDITIONING` |
| `control_net` | 要套用的 controlNet 模型，通常從 ControlNet 載入器輸入 | `CONTROL_NET` |
| `影像` | 用於 controlNet 套用的圖像，需經預處理器處理 | `IMAGE` |
| `vae` | VAE 模型輸入 | `VAE` |
| `強度` | 控制網路調整的強度，數值範圍 0~10。建議值在 0.5~1.5 之間較為合理。較低的值允許模型有更多自由度，較高的值則施加更嚴格的限制。過高的值可能導致圖像異常。您可以測試並調整此數值，以微調控制網路的影響力。 | `FLOAT` |
| `start_percent` | 數值 0.000~1.000，以百分比決定何時開始套用 controlNet，例如 0.2 表示 ControlNet 引導將在擴散過程的 20% 時開始影響圖像生成 | `FLOAT` |
| `end_percent` | 數值 0.000~1.000，以百分比決定何時停止套用 controlNet，例如 0.8 表示 ControlNet 引導將在擴散過程的 80% 時停止影響圖像生成 | `FLOAT` |

### 輸出

| 參數 | 功能說明 | 資料類型 |
| --- | --- | --- |
| `positive` | 經 ControlNet 處理後的正向條件資料，可輸出至下一個 ControlNet 或 K 取樣器節點 | `CONDITIONING` |
| `negative` | 經 ControlNet 處理後的負向條件資料，可輸出至下一個 ControlNet 或 K 取樣器節點 | `CONDITIONING` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApply/zh-TW.md)
