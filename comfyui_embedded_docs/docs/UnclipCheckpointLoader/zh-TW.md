此節點會偵測位於 `ComfyUI/models/checkpoints` 資料夾中的模型，並會讀取在 extra_model_paths.yaml 檔案中設定的其他路徑中的模型。有時，您可能需要**重新整理 ComfyUI 介面**，以便讓它從對應的資料夾中讀取模型檔案。

unCLIPCheckpointLoader 節點專為載入針對 unCLIP 模型量身打造的檢查點而設計。它促進了從指定檢查點中擷取並初始化模型、CLIP 視覺模組以及 VAE 的過程，簡化了後續操作或分析的設定流程。

## 輸入

| 欄位 | 說明 | Comfy 資料類型 |
| --- | --- | --- |
| `ckpt_name` | 指定要載入的檢查點名稱，從預先定義的目錄中識別並擷取正確的檢查點檔案，進而決定模型與設定的初始化。 | `COMBO[STRING]` |

## 輸出

| 欄位 | 說明 | Comfy 資料類型 | Python 資料類型 |
| --- | --- | --- | --- |
| `model` | 代表從檢查點載入的主要模型。 | `MODEL` | `torch.nn.Module` |
| `clip` | 代表從檢查點載入的 CLIP 模組（如果有的話）。 | `CLIP` | `torch.nn.Module` |
| `vae` | 代表從檢查點載入的 VAE 模組（如果有的話）。 | `VAE` | `torch.nn.Module` |
| `clip_vision` | 代表從檢查點載入的 CLIP 視覺模組（如果有的話）。 | `CLIP_VISION` | `torch.nn.Module` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/unCLIPCheckpointLoader/zh-TW.md)
