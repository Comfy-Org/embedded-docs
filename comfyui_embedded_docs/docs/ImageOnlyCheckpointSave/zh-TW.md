## 概述

ImageOnlyCheckpointSave 節點用於儲存包含模型、CLIP 視覺編碼器和 VAE 的檢查點檔案。它會以指定的檔案名稱前綴建立一個 safetensors 檔案，並將其儲存在輸出目錄中。此節點專門設計用於將與影像相關的模型組件一起儲存在單一檢查點檔案中。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要儲存在檢查點中的模型 | MODEL | 是 | - |
| `clip_vision` | 要儲存在檢查點中的 CLIP 視覺編碼器 | CLIP_VISION | 是 | - |
| `vae` | 要儲存在檢查點中的 VAE（變分自編碼器） | VAE | 是 | - |
| `檔名前綴` | 輸出檔案名稱的前綴（預設值："checkpoints/ComfyUI"） | STRING | 是 | - |
| `prompt` | 工作流程提示資料的隱藏參數 | PROMPT | 否 | - |
| `extra_pnginfo` | 額外 PNG 元資料的隱藏參數 | EXTRA_PNGINFO | 否 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| - | 此節點不返回任何輸出 | - |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d2a26933f0e2fcccf3c57f50038fb40ef5b23d00ccdd2e1d215b3cb78203b9fd`
