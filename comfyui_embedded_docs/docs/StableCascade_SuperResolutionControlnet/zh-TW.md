> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/zh-TW.md)

{heading_overview}

StableCascade_SuperResolutionControlnet 節點為 Stable Cascade 超解析度處理準備輸入資料。它接收輸入圖像並使用 VAE 進行編碼以創建控制網路輸入，同時也為 Stable Cascade 流程的階段 C 和階段 B 生成佔位符潛在表示。

{heading_inputs}

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 要用於超解析度處理的輸入圖像 |
| `vae` | VAE | 是 | - | 用於編碼輸入圖像的 VAE 模型 |

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `controlnet_input` | IMAGE | 適合用於控制網路輸入的編碼圖像表示 |
| `stage_c` | LATENT | 用於 Stable Cascade 處理階段 C 的佔位符潛在表示 |
| `stage_b` | LATENT | 用於 Stable Cascade 處理階段 B 的佔位符潛在表示 |