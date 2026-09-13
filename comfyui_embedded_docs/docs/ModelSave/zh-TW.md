# 儲存模型

ModelSave 節點會將 MODEL 儲存到您的電腦儲存空間，作為 `.safetensors` 檢查點檔案。它會使用您提供的檔名前置字元，將檔案寫入 ComfyUI 的輸出目錄，並在可用時將工作流程提示資訊與模型中繼資料內嵌到儲存的檔案中。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要儲存到磁碟的模型 | MODEL | 是 | - |
| `檔名前綴` | 儲存模型檔案的檔名與路徑前置字元（預設值："diffusion_models/ComfyUI"） | STRING | 是 | - |
| `prompt` | 工作流程提示資訊（自動提供） | PROMPT | 否 | - |
| `extra_pnginfo` | 額外的工作流程中繼資料（自動提供） | EXTRA_PNGINFO | 否 | - |

注意：儲存的檔名由 `filename_prefix` 的值加上五位數計數器組成（例如：`diffusion_models/ComfyUI_00001_.safetensors`）。如果相同前置字元的檔案已存在，計數器會遞增，讓新檔案取得唯一名稱。當可用時，工作流程提示、額外中繼資料與模型架構資訊（例如 Stable Diffusion XL、SDXL Refiner、Stable Video Diffusion 或 Stable Diffusion 3）會內嵌到儲存的檔案中。如果透過 ComfyUI 的命令列設定停用中繼資料儲存，提示與額外中繼資料就不會寫入檔案。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| *None* | 此節點不會回傳任何輸出值 | - |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/zh-TW.md)

---
**Source fingerprint (SHA-256):** `943e60f2c596d9cbcaabe95029fd9d443df5b61c6137736a8b1b81ab78f200ea`
