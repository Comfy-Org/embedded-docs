> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointLoader/zh-TW.md)

此節點會偵測位於 `ComfyUI/models/checkpoints` 資料夾中的模型，同時也會從 extra_model_paths.yaml 檔案中設定的其他路徑讀取模型。有時您可能需要**重新整理 ComfyUI 介面**，才能讓它從相應的資料夾讀取模型檔案。

此節點專門在影片生成工作流程中載入專用於影像模型的檢查點。它能有效率地從指定檢查點中擷取並配置必要元件，專注於模型的影像相關方面。

## 輸入參數

| 欄位 | 資料類型 | 描述 |
|------|-----------|------|
| `ckpt_name` | COMBO[STRING] | 指定要載入的檢查點名稱，對於從預定義列表中識別和擷取正確的檢查點檔案至關重要。 |

## 輸出參數

| 欄位 | 資料類型 | 描述 |
|------|-----------|------|
| `model` | MODEL | 傳回從檢查點載入的主要模型，配置用於影片生成情境中的影像處理。 |
| `clip_vision` | CLIP_VISION | 提供來自檢查點的 CLIP 視覺元件，專為影像理解和特徵提取而設計。 |
| `vae` | VAE | 提供變分自編碼器（VAE）元件，對於影像操作和生成任務至關重要。 |