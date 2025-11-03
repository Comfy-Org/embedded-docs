> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UpscaleModelLoader/zh-TW.md)

{heading_overview}

此節點會偵測位於 `ComfyUI/models/upscale_models` 資料夾中的模型，同時也會從 extra_model_paths.yaml 檔案中設定的其他路徑讀取模型。有時您可能需要**重新整理 ComfyUI 介面**，以便讓它從相應的資料夾讀取模型檔案。

UpscaleModelLoader 節點專為從指定目錄載入超解析度模型而設計。它協助擷取和準備用於影像超解析度任務的模型，確保模型正確載入並配置以進行評估。

{heading_inputs}

| 欄位          | Comfy 資料類型      | 描述                                                                       |
|---------------|--------------------|----------------------------------------------------------------------------|
| `model_name`  | `COMBO[STRING]`    | 指定要載入的超解析度模型名稱，用於從超解析度模型目錄中識別並擷取正確的模型檔案。 |

{heading_outputs}

| 欄位            | Comfy 資料類型       | 描述                                                              |
|-----------------|---------------------|-------------------------------------------------------------------|
| `upscale_model` | `UPSCALE_MODEL`     | 傳回已載入並準備就緒的超解析度模型，可用於影像超解析度任務。 |