> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleCreativeNode/zh-TW.md)

{heading_overview}

將影像以最小變動的方式放大至 4K 解析度。此節點使用 Stability AI 的創意放大技術來提升影像解析度，同時保留原始內容並添加細微的創意細節。

{heading_inputs}

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 要進行放大的輸入影像 |
| `prompt` | STRING | 是 | - | 您希望在輸出影像中看到的內容。一個強而有力、描述性的提示，能明確定義元素、顏色和主體，將帶來更好的結果。（預設值：空字串） |
| `creativity` | FLOAT | 是 | 0.1-0.5 | 控制建立不受初始影像強烈制約之額外細節的可能性。（預設值：0.3） |
| `style_preset` | COMBO | 是 | 提供多個選項 | 生成影像的選定風格。選項包含 Stability AI 提供的各種風格預設集。 |
| `seed` | INT | 是 | 0-4294967294 | 用於建立雜訊的隨機種子。（預設值：0） |
| `negative_prompt` | STRING | 否 | - | 您不希望出現在輸出影像中的關鍵字。這是一項進階功能。（預設值：空字串） |

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `image` | IMAGE | 放大至 4K 解析度的影像 |