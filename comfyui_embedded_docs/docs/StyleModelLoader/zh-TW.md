此節點會偵測位於 `ComfyUI/models/style_models` 資料夾中的模型，同時也會讀取在 extra_model_paths.yaml 檔案中設定的其他路徑中的模型。有時，您可能需要**重新整理 ComfyUI 介面**，以便讓它從對應的資料夾中讀取模型檔案。

StyleModelLoader 節點旨在從指定路徑載入風格模型。它專注於擷取並初始化風格模型，這些模型可用於將特定的藝術風格套用至影像，從而根據載入的風格模型實現視覺輸出的自訂化。

## 輸入

| 參數名稱 | 說明 | Comfy 資料型別 | Python 資料型別 |
| --- | --- | --- | --- |
| `style_model_name` | 指定要載入的風格模型名稱。此名稱用於在預定義的目錄結構中定位模型檔案，允許根據使用者輸入或應用程式需求動態載入不同的風格模型。 | COMBO[STRING] | `str` |

## 輸出

| 參數名稱 | 說明 | Comfy 資料型別 | Python 資料型別 |
| --- | --- | --- | --- |
| `style_model` | 傳回已載入的風格模型，準備好用於將風格套用至影像。這使得能夠透過套用不同的藝術風格來動態自訂視覺輸出。 | `STYLE_MODEL` | `StyleModel` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StyleModelLoader/zh-TW.md)
