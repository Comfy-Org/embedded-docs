此節點會偵測位於 `ComfyUI/models/upscale_models` 資料夾中的模型，同時也會讀取在 extra_model_paths.yaml 檔案中設定的其他路徑中的模型。有時您可能需要**重新整理 ComfyUI 介面**，讓它能夠從對應的資料夾中讀取模型檔案。

UpscaleModelLoader 節點專門用於從指定目錄載入放大模型。它負責擷取並準備放大模型，以執行影像放大任務，確保模型能正確載入並設定為可評估狀態。

## 輸入

| 欄位 | 說明 | Comfy dtype |
| --- | --- | --- |
| `model_name` | 指定要載入的放大模型名稱，用於從放大模型目錄中識別並擷取正確的模型檔案。 | `COMBO[STRING]` |

## 輸出

| 欄位 | 說明 | Comfy dtype |
| --- | --- | --- |
| `upscale_model` | 回傳已載入並準備好的放大模型，可用於影像放大任務。 | `UPSCALE_MODEL` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UpscaleModelLoader/zh-TW.md)
