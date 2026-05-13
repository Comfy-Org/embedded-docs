> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointSave/zh-TW.md)

`Save Checkpoint` 節點旨在將完整的 Stable Diffusion 模型（包括 UNet、CLIP 和 VAE 組件）儲存為 **.safetensors** 格式的檢查點檔案。

`Save Checkpoint` 主要用於模型合併工作流程。在透過 `ModelMergeSimple`、`ModelMergeBlocks` 等節點建立新的合併模型後，您可以使用此節點將結果儲存為可重複使用的檢查點檔案。

## 輸入

| 參數 | 資料類型 | 說明 |
|-----------|-----------|-------------|
| `model` | MODEL | `model` 參數代表要儲存狀態的主要模型。對於捕捉模型的當前狀態以供未來還原或分析至關重要。 |
| `clip` | CLIP | `clip` 參數用於指定與主要模型關聯的 CLIP 模型，允許將其狀態與主模型一同儲存。 |
| `vae` | VAE | `vae` 參數用於指定變分自編碼器（VAE）模型，允許將其狀態與主模型和 CLIP 一同儲存，以供未來使用或分析。 |
| `filename_prefix` | STRING | 此參數指定檢查點儲存時檔案名稱的前綴。 |

此外，該節點還有兩個用於元資料的隱藏輸入：

**prompt (PROMPT)**：工作流程提示資訊
**extra_pnginfo (EXTRA_PNGINFO)**：額外的 PNG 資訊

## 輸出

此節點將輸出一個檢查點檔案，對應的輸出檔案路徑為 `output/checkpoints/` 目錄

## 架構相容性

- 目前完全支援：SDXL、SD3、SVD 及其他主流架構，請參閱[原始碼](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L176-L189)
- 基本支援：其他架構可以儲存，但沒有標準化的元資料資訊

## 相關連結

相關原始碼：[nodes_model_merging.py#L227](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L227)