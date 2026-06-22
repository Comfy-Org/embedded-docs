# 僅影像權重載入器（img2vid 模型）

此節點會偵測位於 `ComfyUI/models/checkpoints` 資料夾中的模型，同時也會讀取在 extra_model_paths.yaml 檔案中設定的其他路徑中的模型。有時，您可能需要**重新整理 ComfyUI 介面**，以便讓它從對應的資料夾中讀取模型檔案。

此節點專門用於在影片生成工作流程中載入基於影像的模型的檢查點。它能有效率地從指定的檢查點中擷取並設定必要的元件，專注於模型的影像相關層面。

## 輸入

| 欄位 | 說明 | 資料類型 |
| --- | --- | --- |
| `ckpt_name` | 指定要載入的檢查點名稱，對於從預定義清單中識別和擷取正確的檢查點檔案至關重要。 | COMBO[STRING] |

## 輸出

| 欄位 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 傳回從檢查點載入的主要模型，該模型已配置為在影片生成環境中進行影像處理。 | MODEL |
| `clip_vision` | 提供來自檢查點的 CLIP 視覺元件，專為影像理解與特徵提取而設計。 | `CLIP_VISION` |
| `vae` | 提供變分自編碼器（VAE）元件，對於影像操作與生成任務至關重要。 | VAE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointLoader/zh-TW.md)
