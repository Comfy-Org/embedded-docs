> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/zh-TW.md)

## 概述

ModelSave 節點可將訓練或修改後的模型儲存至電腦儲存空間。此節點接收模型作為輸入，並將其寫入您指定檔案名稱的檔案中，讓您能夠保留工作成果並在未來專案中重複使用模型。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要儲存至磁碟的模型 |
| `檔名前綴` | STRING | 是 | - | 儲存模型檔案的檔案名稱與路徑前綴（預設值："diffusion_models/ComfyUI"） |
| `prompt` | PROMPT | 否 | - | 工作流程提示資訊（自動提供） |
| `extra_pnginfo` | EXTRA_PNGINFO | 否 | - | 額外的工作流程元資料（自動提供） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| *無* | - | 此節點不傳回任何輸出值 |

---
**Source fingerprint (SHA-256):** `1dda8a6d85aa19b739c1fe3e6e7f816e05011044fc8b0b91b23fa303f71d8b19`
