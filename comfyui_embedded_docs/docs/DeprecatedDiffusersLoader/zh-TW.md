> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DeprecatedDiffusersLoader/zh-TW.md)

DiffusersLoader 節點專為從 diffusers 函式庫載入模型而設計，特別處理根據提供的模型路徑載入 UNet、CLIP 和 VAE 模型。此節點有助於將這些模型整合到 ComfyUI 框架中，實現進階功能，例如文字轉圖像生成、圖像處理等。

## 輸入

| 參數 | 資料類型 | 說明 |
|--------------|--------------|-------------|
| `model_path` | COMBO[STRING] | 指定要載入的模型路徑。此路徑至關重要，因為它決定了後續操作將使用哪個模型，進而影響節點的輸出與功能。 |

## 輸出

| 參數 | 資料類型 | 說明 |
|-----------|-------------|-------------|
| `model`   | MODEL     | 已載入的 UNet 模型，為輸出元組的一部分。此模型對於在 ComfyUI 框架內進行圖像合成與處理任務至關重要。 |
| `clip`    | CLIP      | 已載入的 CLIP 模型，若請求則包含在輸出元組中。此模型可實現進階的文字與圖像理解及處理能力。 |
| `vae`     | VAE       | 已載入的 VAE 模型，若請求則包含在輸出元組中。此模型對於涉及潛在空間操作與圖像生成的任務至關重要。 |