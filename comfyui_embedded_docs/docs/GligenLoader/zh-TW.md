> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLIGENLoader/zh-TW.md)

{heading_overview}

此節點會偵測位於 `ComfyUI/models/gligen` 資料夾中的模型，同時也會從 extra_model_paths.yaml 檔案中設定的其他路徑讀取模型。有時您可能需要**重新整理 ComfyUI 介面**，讓它能夠從相應的資料夾讀取模型檔案。

`GLIGENLoader` 節點專為載入 GLIGEN 模型而設計，這些是專門的生成模型。它簡化了從指定路徑檢索和初始化這些模型的過程，使它們準備好用於後續的生成任務。

{heading_inputs}

| 欄位 | Comfy 資料類型 | 描述 |
|-------------|-------------------|-----------------------------------------------------------------------------------|
| `gligen_name`| `COMBO[STRING]` | 要載入的 GLIGEN 模型名稱，指定要檢索和載入的模型檔案，對於 GLIGEN 模型的初始化至關重要。 |

{heading_outputs}

| 欄位 | 資料類型 | 描述 |
|----------|-------------|--------------------------------------------------------------------------|
| `gligen` | `GLIGEN` | 已載入的 GLIGEN 模型，準備好用於生成任務，代表從指定路徑載入的完全初始化模型。 |