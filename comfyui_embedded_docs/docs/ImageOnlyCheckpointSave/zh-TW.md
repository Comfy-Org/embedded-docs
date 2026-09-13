# 儲存僅影像檢查點

此節點會儲存一個檢查點檔案，該檔案將模型與其 CLIP 視覺編碼器和 VAE 一起打包。該檔案會以 safetensors 格式寫入輸出目錄，並使用指定的檔名前綴，因此模型的影像相關元件可以儲存為單一檢查點。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要儲存在檢查點中的模型 | MODEL | 是 | - |
| `clip_vision` | 要儲存在檢查點中的 CLIP 視覺編碼器 | CLIP_VISION | 是 | - |
| `vae` | 要儲存在檢查點中的 VAE（變分自編碼器） | VAE | 是 | - |
| `檔名前綴` | 輸出檔名的前綴（預設："checkpoints/ComfyUI"） | STRING | 是 | - |
| `prompt` | 接收工作流程 prompt 資料的隱藏參數 | PROMPT | 否 | - |
| `extra_pnginfo` | 接收額外 PNG 中繼資料的隱藏參數 | EXTRA_PNGINFO | 否 | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| - | 此節點不會傳回任何輸出 | - |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8ff4b3a78d8da523eaa5f784f847e954ba73b4d6037e748dcce592b447fcdee9`
