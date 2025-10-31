> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StyleModelLoader/zh-TW.md)

此節點會偵測位於 `ComfyUI/models/style_models` 資料夾中的模型，同時也會從 extra_model_paths.yaml 檔案中設定的其他路徑讀取模型。有時您可能需要**重新整理 ComfyUI 介面**，才能讓它從相應的資料夾讀取模型檔案。

StyleModelLoader 節點旨在從指定路徑載入風格模型。它專注於檢索和初始化可用於對影像應用特定藝術風格的風格模型，從而實現基於載入的風格模型來自訂視覺輸出。

## 輸入參數

| 參數名稱 | Comfy 資料類型 | Python 資料類型 | 描述 |
|----------|----------------|-----------------|------|
| `style_model_name` | COMBO[STRING] | `str` | 指定要載入的風格模型名稱。此名稱用於在預定義的目錄結構中定位模型檔案，從而允許根據用戶輸入或應用需求動態載入不同的風格模型。 |

## 輸出參數

| 參數名稱 | Comfy 資料類型 | Python 資料類型 | 描述 |
|----------|----------------|-----------------|------|
| `style_model` | `STYLE_MODEL` | `StyleModel` | 返回已載入的風格模型，準備好用於對影像應用風格。這使得能夠透過應用不同的藝術風格來動態自訂視覺輸出。 |