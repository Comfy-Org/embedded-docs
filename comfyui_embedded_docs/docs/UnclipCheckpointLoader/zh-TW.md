> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/unCLIPCheckpointLoader/zh-TW.md)

此節點會偵測位於 `ComfyUI/models/checkpoints` 資料夾中的模型，同時也會從 extra_model_paths.yaml 檔案中設定的額外路徑讀取模型。有時您可能需要**重新整理 ComfyUI 介面**，才能讓它從相應的資料夾讀取模型檔案。

unCLIPCheckpointLoader 節點專為載入特別為 unCLIP 模型設計的檢查點而開發。它能從指定的檢查點中擷取並初始化模型、CLIP 視覺模組和 VAE，簡化後續操作或分析的設定流程。

## 輸入參數

| 欄位名稱 | Comfy 資料類型 | 描述 |
|----------|----------------|------|
| `ckpt_name` | `COMBO[STRING]` | 指定要載入的檢查點名稱，從預定義目錄中識別並擷取正確的檢查點檔案，決定模型和配置的初始化。 |

## 輸出參數

| 欄位名稱 | Comfy 資料類型 | 描述 | Python 資料類型 |
|----------|----------------|------|----------------|
| `model` | `MODEL` | 代表從檢查點載入的主要模型。 | `torch.nn.Module` |
| `clip` | `CLIP` | 代表從檢查點載入的 CLIP 模組（如果可用）。 | `torch.nn.Module` |
| `vae` | `VAE` | 代表從檢查點載入的 VAE 模組（如果可用）。 | `torch.nn.Module` |
| `clip_vision` | `CLIP_VISION` | 代表從檢查點載入的 CLIP 視覺模組（如果可用）。 | `torch.nn.Module` |