> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/zh-TW.md)

ImageOnlyCheckpointSave 節點會儲存包含模型、CLIP 視覺編碼器和 VAE 的檢查點檔案。它會建立帶有指定檔案名稱前綴的 safetensors 檔案，並將其儲存在輸出目錄中。此節點專門設計用於將圖像相關的模型組件一起儲存在單一檢查點檔案中。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要儲存到檢查點中的模型 |
| `clip_vision` | CLIP_VISION | 是 | - | 要儲存到檢查點中的 CLIP 視覺編碼器 |
| `vae` | VAE | 是 | - | 要儲存到檢查點中的 VAE（變分自編碼器） |
| `檔名前綴` | STRING | 是 | - | 輸出檔案名稱的前綴（預設："checkpoints/ComfyUI"） |
| `prompt` | PROMPT | 否 | - | 用於工作流程提示資料的隱藏參數 |
| `extra_pnginfo` | EXTRA_PNGINFO | 否 | - | 用於額外 PNG 元資料的隱藏參數 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| - | - | 此節點不返回任何輸出 |