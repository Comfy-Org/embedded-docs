> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/zh-TW.md)

此節點載入專為潛在表徵放大設計的模型。它從系統指定資料夾讀取模型檔案，並自動偵測其類型（720p、1080p 或其他），以實例化並配置正確的內部模型架構。載入的模型隨後可供其他節點用於潛在空間超解析度任務。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model_name` | STRING | 是 | *`latent_upscale_models` 資料夾中的所有檔案* | 要載入的潛在放大模型檔案名稱。可用選項會根據您 ComfyUI 的 `latent_upscale_models` 目錄中的檔案動態產生。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model` | LATENT_UPSCALE_MODEL | 已載入的潛在放大模型，已配置並準備就緒可供使用。 |
