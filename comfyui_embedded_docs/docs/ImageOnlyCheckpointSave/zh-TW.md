# 儲存僅影像檢查點

此節點會儲存包含模型、CLIP 視覺編碼器及 VAE 的檢查點檔案。它會以指定的檔案名稱前綴建立 safetensors 檔案，並將其儲存在輸出目錄中。此節點專門用於將影像相關的模型元件一起儲存在單一檢查點檔案中。

## 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要儲存在檢查點中的模型 | MODEL | 是 | - |
| `clip_vision` | 要儲存在檢查點中的 CLIP 視覺編碼器 | CLIP_VISION | 是 | - |
| `vae` | 要儲存在檢查點中的 VAE（變分自編碼器） | VAE | 是 | - |
| `filename_prefix` | 輸出檔案名稱的前綴（預設值："checkpoints/ComfyUI"） | STRING | 是 | - |
| `prompt` | 用於工作流程提示資料的隱藏參數 | PROMPT | 否 | - |
| `extra_pnginfo` | 用於額外 PNG 中繼資料的隱藏參數 | EXTRA_PNGINFO | 否 | - |

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
| --- | --- | --- |
| - | 此節點不會回傳任何輸出 | - |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8ff4b3a78d8da523eaa5f784f847e954ba73b4d6037e748dcce592b447fcdee9`
