此節點會偵測位於 `ComfyUI/models/gligen` 資料夾中的模型，同時也會讀取在 extra_model_paths.yaml 檔案中設定的其他路徑中的模型。有時，您可能需要**重新整理 ComfyUI 介面**，讓它能夠從對應的資料夾中讀取模型檔案。

`GLIGENLoader` 節點專門用於載入 GLIGEN 模型，這是一種專門的生成式模型。它簡化了從指定路徑擷取並初始化這些模型的流程，使其準備好用於後續的生成任務。

## 輸入

| 欄位 | 說明 | Comfy dtype |
| --- | --- | --- |
| `gligen_name` | 要載入的 GLIGEN 模型名稱，指定要擷取和載入的模型檔案，這對於 GLIGEN 模型的初始化至關重要。 | `COMBO[STRING]` |

## 輸出

| 欄位 | 說明 | 資料類型 |
| --- | --- | --- |
| `gligen` | 已載入的 GLIGEN 模型，可用於生成任務，代表從指定路徑載入的完整初始化模型。 | `GLIGEN` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLIGENLoader/zh-TW.md)
