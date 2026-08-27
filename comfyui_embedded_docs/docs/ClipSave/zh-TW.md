# ClipSave

`CLIPSave` 節點將 CLIP 文字編碼器模型以 SafeTensors 格式儲存到磁碟。它專為進階模型合併工作流程設計，會根據模型的內部結構自動將 CLIP 模型分離為其組成部分（例如 CLIP-L、CLIP-G 或 T5XXL），並將每個組成部分儲存為單獨的檔案。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 要儲存的 CLIP 模型。 | CLIP | 是 | - |
| `檔名前綴` | 儲存檔案的前置路徑與檔名。節點會附加元件後綴（例如 `_clip_l`、`_clip_g`）與計數器，以產生唯一的檔名（預設值：`clip/ComfyUI`）。 | STRING | 是 | - |
| `prompt` | 工作流程提示資訊，會作為中繼資料儲存在輸出檔案中。此參數在 UI 中隱藏。 | PROMPT | 否 | - |
| `extra_pnginfo` | 額外的中繼資料，會以鍵值對的形式儲存在輸出檔案中。此參數在 UI 中隱藏。 | EXTRA_PNGINFO | 否 | - |

## 輸出

此節點沒有輸出連線。它會將處理後的檔案直接儲存到 `ComfyUI/output/` 目錄。儲存的檔案包含中繼資料（格式設定為 "pt"，加上工作流程提示與任何額外的 PNG 資訊），除非以 `--disable-metadata` 參數啟動 ComfyUI。

### 已儲存檔案詳情

此節點會分析 CLIP 模型的狀態字典，並為每個偵測到的元件儲存單獨的 SafeTensors 檔案。元件是透過其參數鍵的前綴來識別。會檢查以下前綴：

- `clip_l.`（CLIP-L 文字編碼器）
- `clip_g.`（CLIP-G 文字編碼器）
- `clip_h.`（CLIP-H 文字編碼器）
- `t5xxl.`（T5-XXL 文字編碼器）
- `pile_t5xl.`（Pile-T5-XL 文字編碼器）
- `mt5xl.`（mT5-XL 文字編碼器）
- `umt5xxl.`（UMT5-XXL 文字編碼器）
- `t5base.`（T5-Base 文字編碼器）
- `gemma2_2b.`（Gemma 2 2B 文字編碼器）
- `llama.`（LLaMA 文字編碼器）
- `hydit_clip.`（Hydit CLIP 文字編碼器）
- 空前綴（其他 CLIP 元件）

對於每個偵測到的元件，節點會建立一個名為 `{filename_prefix}_{counter:05}_.safetensors` 的檔案，其中元件前綴會附加到檔名前綴之後（例如 `clip/ComfyUI_clip_l_00001_.safetensors`）。在儲存過程中，`transformer.` 前綴會從參數鍵中移除。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipSave/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4ab9171e4245b10f738f78bac8a5b564c0957dde352e207ec3f9865e4fac0cab`
