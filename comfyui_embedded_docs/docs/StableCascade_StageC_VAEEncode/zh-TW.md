> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageC_VAEEncode/zh-TW.md)

{heading_overview}

StableCascade_StageC_VAEEncode 節點透過 VAE 編碼器處理圖像，為 Stable Cascade 模型生成潛在表示。它接收輸入圖像並使用指定的 VAE 模型進行壓縮，然後輸出兩個潛在表示：一個用於 C 階段，另一個用於 B 階段的佔位符。壓縮參數控制圖像在編碼前縮小的程度。

{heading_inputs}

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 要編碼到潛在空間的輸入圖像 |
| `vae` | VAE | 是 | - | 用於編碼圖像的 VAE 模型 |
| `compression` | INT | 否 | 4-128 | 在編碼前應用於圖像的壓縮因子（預設值：42） |

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `stage_c` | LATENT | 用於 Stable Cascade 模型 C 階段的編碼潛在表示 |
| `stage_b` | LATENT | 用於 B 階段的佔位符潛在表示（目前返回零值） |