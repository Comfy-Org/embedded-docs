# WaveSpeed 圖像升頻

WaveSpeed 影像放大節點使用外部 AI 服務來提高影像的解析度和品質。它接收單張輸入照片，並將其放大至更高的目標解析度，例如 2K、4K 或 8K，從而產生更清晰、更細緻的結果。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於放大的 AI 模型。"SeedVR2" 和 "Ultimate" 提供不同的品質和價格等級。 | STRING | 是 | `"SeedVR2"`<br>`"Ultimate"` |
| `圖像` | 要放大的輸入影像。 | IMAGE | 是 |  |
| `目標解析度` | 放大影像所需的輸出解析度。 | STRING | 是 | `"2K"`<br>`"4K"`<br>`"8K"` |

**注意：** 此節點僅接受單張輸入影像。提供一批影像將會導致錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `圖像` | 放大後的高解析度輸出影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WavespeedImageUpscaleNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b14056f981f6e34c67d8126391acc11878f92f5f406559afbac803c86da42bcc`
