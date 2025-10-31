> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointSave/zh-TW.md)

`Save Checkpoint` 節點旨在將完整的 Stable Diffusion 模型（包含 UNet、CLIP 和 VAE 組件）儲存為 **.safetensors** 格式的檢查點檔案。

此節點主要用於模型合併工作流程。透過 `ModelMergeSimple`、`ModelMergeBlocks` 等節點建立新的合併模型後，您可以使用此節點將結果儲存為可重複使用的檢查點檔案。

## 輸入參數

| 參數名稱 | 資料類型 | 描述 |
|-----------|-----------|-------------|
| `model` | MODEL | 代表要儲存狀態的主要模型，對於擷取模型當前狀態以供未來恢復或分析至關重要 |
| `clip` | CLIP | 用於與主要模型關聯的 CLIP 模型，可將其狀態與主模型一同儲存 |
| `vae` | VAE | 用於變分自編碼器 (VAE) 模型，可將其狀態與主模型和 CLIP 一同儲存以供未來使用或分析 |
| `filename_prefix` | STRING | 指定檢查點儲存檔名的前綴詞 |

此外，該節點還有兩個用於元資料的隱藏輸入：

**prompt (PROMPT)**: 工作流程提示資訊
**extra_pnginfo (EXTRA_PNGINFO)**: 額外 PNG 資訊

## 輸出結果

此節點將輸出一個檢查點檔案，對應的輸出檔案路徑為 `output/checkpoints/` 目錄

## 架構相容性

- 目前完整支援：SDXL、SD3、SVD 及其他主流架構，請參閱[原始程式碼](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L176-L189)
- 基本支援：其他架構可以儲存但沒有標準化的元資料資訊

## 相關連結

相關原始程式碼：[nodes_model_merging.py#L227](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L227)