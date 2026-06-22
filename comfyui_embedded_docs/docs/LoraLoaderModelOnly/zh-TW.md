# LoraLoaderModelOnly

此節點會偵測位於 `ComfyUI/models/loras` 資料夾中的模型，同時也會讀取在 extra_model_paths.yaml 檔案中設定的其他路徑中的模型。有時您可能需要**重新整理 ComfyUI 介面**，以便讓它從對應的資料夾中讀取模型檔案。

此節點專門用於載入 LoRA 模型，無需 CLIP 模型，專注於根據 LoRA 參數增強或修改給定的模型。它允許透過 LoRA 參數動態調整模型的強度，從而實現對模型行為的精細控制。

## 輸入

| 欄位 | 描述 | Comfy 資料類型 |
| --- | --- | --- |
| `model` | 用於修改的基礎模型，LoRA 調整將應用於此模型。 | `MODEL` |
| `lora_name` | 要載入的 LoRA 檔案名稱，指定要應用於模型的調整。 | `COMBO[STRING]` |
| `strength_model` | 決定 LoRA 調整的強度，數值越高表示修改程度越強。 | `FLOAT` |

## 輸出

| 欄位 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用 LoRA 調整的修改後模型，反映模型行為或功能上的變化。 | `MODEL` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderModelOnly/zh-TW.md)
