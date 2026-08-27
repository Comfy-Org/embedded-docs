# 儲存模型

ModelSave 節點將模型以 `.safetensors` 檢查點檔案格式儲存到您的電腦儲存空間。它接收模型作為輸入，並使用您指定的檔名前綴將其寫入輸出目錄。當可用時，它也會將工作流程提示資訊與其他中繼資料嵌入到儲存檔案中。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要儲存到磁碟的模型 | MODEL | 是 | - |
| `檔名前綴` | 儲存模型檔案的檔案名稱與路徑前綴（預設值："diffusion_models/ComfyUI"） | STRING | 是 | - |
| `prompt` | 工作流程提示資訊（自動提供） | PROMPT | 否 | - |
| `extra_pnginfo` | 額外的工作流程中繼資料（自動提供） | EXTRA_PNGINFO | 否 | - |

注意：儲存檔案名稱由 `filename_prefix` 的值加上五位數計數器組成（例如：`diffusion_models/ComfyUI_00001_.safetensors`）。如果相同前綴的檔案已存在，計數器會遞增，使新檔案獲得唯一名稱。當可用時，工作流程提示、額外中繼資料與模型架構資訊會嵌入儲存檔案中。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| *None* | 此節點不會回傳任何輸出值 | - |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/zh-TW.md)

---
**Source fingerprint (SHA-256):** `943e60f2c596d9cbcaabe95029fd9d443df5b61c6137736a8b1b81ab78f200ea`
