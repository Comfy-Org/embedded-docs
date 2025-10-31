> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplyAdvanced/zh-TW.md)

{heading_overview}

此節點根據圖像和 ControlNet 模型對條件資料應用進階的 ControlNet 轉換。它允許微調 ControlNet 對生成內容的影響程度，從而實現更精確和多樣化的條件調整。

{heading_inputs}

| 參數 | 資料類型 | 描述 |
|-----------|-------------|-------------|
| `positive` | `CONDITIONING` | 將應用 ControlNet 轉換的正面條件資料。它代表在生成內容中需要增強或保持的理想屬性或特徵。 |
| `negative` | `CONDITIONING` | 負面條件資料，代表在生成內容中需要減弱或移除的屬性或特徵。ControlNet 轉換同樣會應用於此資料，從而實現內容特徵的平衡調整。 |
| `control_net` | `CONTROL_NET` | ControlNet 模型對於定義條件資料的具體調整和增強至關重要。它解讀參考圖像和強度參數來應用轉換，透過修改正面和負面條件資料中的屬性，顯著影響最終輸出結果。 |
| `image` | `IMAGE` | 作為 ControlNet 轉換參考依據的圖像。它影響 ControlNet 對條件資料進行的調整，引導特定特徵的增強或抑制。 |
| `strength` | `FLOAT` | 決定 ControlNet 對條件資料影響強度的標量值。數值越高，調整效果越明顯。 |
| `start_percent` | `FLOAT` | ControlNet 效果開始的百分比，允許在指定範圍內逐步應用轉換。 |
| `end_percent` | `FLOAT` | ControlNet 效果結束的百分比，定義了轉換應用的範圍。這使得調整過程能夠實現更細緻的控制。 |

{heading_outputs}

| 參數 | 資料類型 | 描述 |
|-----------|-------------|-------------|
| `positive` | `CONDITIONING` | 應用 ControlNet 轉換後修改過的正面條件資料，反映了基於輸入參數所進行的增強效果。 |
| `negative` | `CONDITIONING` | 應用 ControlNet 轉換後修改過的負面條件資料，反映了基於輸入參數對特定特徵的抑制或移除效果。 |