# 儲存模型

ModelSave 節點會將訓練或修改過的模型儲存至您的電腦儲存空間。它以模型作為輸入，並使用您指定的檔案名稱前綴，將模型寫入輸出資料夾中的 safetensors 檢查點檔案。當工作流程提示與中繼資料可用時，會一併嵌入至已儲存的檔案中。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要儲存至磁碟的模型 | MODEL | 是 | - |
| `filename_prefix` | 已儲存模型檔案的檔案名稱與路徑前綴（預設："diffusion_models/ComfyUI"）。儲存時會在名稱後面附加遞增編號（例如 `ComfyUI_00000_.safetensors`）。 | STRING | 是 | - |
| `prompt` | 工作流程提示資訊（自動提供） | PROMPT | 否 | - |
| `extra_pnginfo` | 額外的工作流程中繼資料（自動提供） | EXTRA_PNGINFO | 否 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| *None* | 此節點不會回傳任何輸出值 | - |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/zh-TW.md)

---
**Source fingerprint (SHA-256):** `943e60f2c596d9cbcaabe95029fd9d443df5b61c6137736a8b1b81ab78f200ea`
