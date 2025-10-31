> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudio/zh-TW.md)

{heading_overview}

SaveAudio 節點將音訊資料以 FLAC 格式儲存至檔案。它接收音訊輸入，並使用指定的檔案名稱前綴將其寫入到指定的輸出目錄。此節點會自動處理檔案命名，並確保音訊被正確儲存以供後續使用。

{heading_inputs}

| 參數名稱 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `音訊` | AUDIO | 是 | - | 要儲存的音訊資料 |
| `檔名前綴` | STRING | 否 | - | 輸出檔名的前綴（預設值："audio/ComfyUI"） |

*注意：`prompt` 和 `extra_pnginfo` 參數為隱藏參數，由系統自動處理。*

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| *無* | - | 此節點不會返回任何輸出資料，但會將音訊檔案儲存到輸出目錄 |