## 概述

ModelSave 節點可將訓練或修改後的模型儲存至電腦儲存空間。此節點接收模型作為輸入，並將其寫入您指定檔案名稱的檔案中，讓您能夠保留工作成果並在未來專案中重複使用模型。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要儲存至磁碟的模型 | MODEL | 是 | - |
| `檔名前綴` | 儲存模型檔案的檔案名稱與路徑前綴（預設值："diffusion_models/ComfyUI"） | STRING | 是 | - |
| `prompt` | 工作流程提示資訊（自動提供） | PROMPT | 否 | - |
| `extra_pnginfo` | 額外的工作流程元資料（自動提供） | EXTRA_PNGINFO | 否 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| *無* | 此節點不傳回任何輸出值 | - |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1dda8a6d85aa19b739c1fe3e6e7f816e05011044fc8b0b91b23fa303f71d8b19`
