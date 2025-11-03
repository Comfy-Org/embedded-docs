> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DeprecatedDiffusersLoader/zh-TW.md)

DiffusersLoader 節點專為從 diffusers 庫加載模型而設計，特別處理基於提供的模型路徑加載 UNet、CLIP 和 VAE 模型。它促進這些模型在 ComfyUI 框架中的整合，實現如文字生成圖像、圖像處理等高級功能。

## 輸入參數

| 參數名稱       | 資料類型       | 描述 |
|----------------|----------------|------|
| `model_path`   | COMBO[STRING] | 指定要加載的模型路徑。此路徑至關重要，因為它決定了後續操作將使用哪個模型，影響節點的輸出和功能。 |

## 輸出參數

| 參數名稱 | 資料類型 | 描述 |
|----------|----------|------|
| `model`  | MODEL    | 已加載的 UNet 模型，這是輸出元組的一部分。該模型對於 ComfyUI 框架內的圖像合成和處理任務至關重要。 |
| `clip`   | CLIP     | 已加載的 CLIP 模型，如果請求則包含在輸出元組中。該模型能夠實現高級的文字和圖像理解與處理功能。 |
| `vae`    | VAE      | 已加載的 VAE 模型，如果請求則包含在輸出元組中。該模型對於涉及潛在空間操作和圖像生成的任務至關重要。 |