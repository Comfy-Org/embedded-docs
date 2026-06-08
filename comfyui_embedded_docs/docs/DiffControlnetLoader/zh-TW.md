此節點會偵測位於 `ComfyUI/models/controlnet` 資料夾中的模型，同時也會讀取在 extra_model_paths.yaml 檔案中設定的其他路徑中的模型。有時，您可能需要**重新整理 ComfyUI 介面**，以便讓它從對應的資料夾中讀取模型檔案。

DiffControlNetLoader 節點專門用於載入差分控制網路，這是一種特殊的模型，可以根據控制網路規格來修改另一個模型的行為。此節點允許透過應用差分控制網路來動態調整模型行為，從而協助建立自訂的模型輸出。

## 輸入

| 欄位 | 說明 | Comfy 資料類型 |
| --- | --- | --- |
| `model` | 將套用差分控制網路的基礎模型，允許自訂模型的行為。 | `MODEL` |
| `control_net_name` | 識別要載入並套用至基礎模型以修改其行為的特定差分控制網路。 | `COMBO[STRING]` |

## 輸出

| 欄位 | 說明 | Comfy 資料類型 |
| --- | --- | --- |
| `control_net` | 已載入並準備好套用至基礎模型以進行行為修改的差分控制網路。 | `CONTROL_NET` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffControlNetLoader/zh-TW.md)
