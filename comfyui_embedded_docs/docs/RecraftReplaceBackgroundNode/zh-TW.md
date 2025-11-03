> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftReplaceBackgroundNode/zh-TW.md)

{heading_overview}

根據提供的提示替換圖像背景。此節點使用 Recraft API 根據您的文字描述為圖像生成新背景，讓您可以在保持主體完整的情況下完全轉換背景。

{heading_inputs}

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 要處理的輸入圖像 |
| `prompt` | STRING | 是 | - | 圖像生成的提示（預設：空） |
| `n` | INT | 是 | 1-6 | 要生成的圖像數量（預設：1） |
| `seed` | INT | 是 | 0-18446744073709551615 | 決定節點是否應重新執行的種子值；由於外部 API 的特性，實際結果無論種子為何都是非確定性的（預設：0） |
| `recraft_style` | STYLEV3 | 否 | - | 生成背景的選用樣式選擇 |
| `negative_prompt` | STRING | 否 | - | 圖像中不希望出現元素的選用文字描述（預設：空） |

**注意：** `seed` 參數控制節點何時重新執行，但由於外部 API 的特性，無法保證確定性結果。

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | 已替換背景的生成圖像 |