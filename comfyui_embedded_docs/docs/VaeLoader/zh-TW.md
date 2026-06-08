此節點會偵測位於 `ComfyUI/models/vae` 資料夾中的模型，同時也會讀取在 extra_model_paths.yaml 檔案中設定的其他路徑下的模型。有時，您可能需要**重新整理 ComfyUI 介面**，以便讓它從對應的資料夾中讀取模型檔案。

VAELoader 節點專門用於載入變分自編碼器（VAE）模型，特別針對處理標準 VAE 和近似 VAE 進行了最佳化。它支援按名稱載入 VAE，包括對 'taesd' 和 'taesdxl' 模型的特殊處理，並會根據 VAE 的特定設定動態調整。

## 輸入

| 欄位 | 說明 | Comfy 資料類型 |
| --- | --- | --- |
| `vae_name` | 指定要載入的 VAE 名稱，決定要擷取並載入哪個 VAE 模型，支援一系列預先定義的 VAE 名稱，包括 'taesd' 和 'taesdxl'。 | `COMBO[STRING]` |

## 輸出

| 欄位 | 說明 | 資料類型 |
| --- | --- | --- |
| `vae` | 回傳已載入的 VAE 模型，準備好進行編碼或解碼等後續操作。輸出是一個封裝了已載入模型狀態的模型物件。 | `VAE` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAELoader/zh-TW.md)
