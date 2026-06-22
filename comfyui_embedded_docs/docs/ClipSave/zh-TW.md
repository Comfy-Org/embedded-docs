# CLIP 儲存

## 概述

`CLIPSave` 節點將 CLIP 文字編碼器模型以 SafeTensors 格式儲存至磁碟。此節點專為進階模型合併工作流程設計，會根據模型的內部結構自動將 CLIP 模型分離為其組成部分（例如 CLIP-L、CLIP-G 或 T5XXL），並將每個元件儲存為單獨的檔案。

## 輸入

| 參數 | 說明 | 資料類型 | 輸入類型 | 預設值 | 範圍 |
| --- | --- | --- | --- | --- | --- |
| `clip` | 要儲存的 CLIP 模型。 | CLIP | 必要 | - | - |
| `檔名前綴` | 儲存檔案的前置路徑與檔名。節點會附加元件後綴（例如 `_clip_l`、`_clip_g`）及計數器，以產生唯一的檔案名稱。 | STRING | 必要 | `clip/ComfyUI` | - |
| `prompt` | 工作流程提示資訊，會以元資料形式儲存在輸出檔案中。 | PROMPT | 隱藏 | - | - |
| `extra_pnginfo` | 額外的元資料，會以鍵值對形式儲存在輸出檔案中。 | EXTRA_PNGINFO | 隱藏 | - | - |

## 輸出

此節點沒有輸出連線。它會直接將處理後的檔案儲存至 `ComfyUI/output/` 目錄。

### 儲存檔案詳細資訊

節點會分析 CLIP 模型的狀態字典，並為每個偵測到的元件儲存獨立的 SafeTensors 檔案。元件是透過其參數鍵的前綴來識別。系統會檢查以下前綴：

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
- 空白前綴（其他 CLIP 元件）

對於每個偵測到的元件，節點會建立一個名為 `{filename_prefix}_{counter:05}_.safetensors` 的檔案，其中元件前綴會附加在檔名前綴之後（例如 `clip/ComfyUI_clip_l_00001_.safetensors`）。在儲存過程中，`transformer.` 前綴會從參數鍵中移除。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSave/zh-TW.md)

---
**Source fingerprint (SHA-256):** `039b39cbfb9b04ccebc5fc885ebe75dfde14838530d38133d0a3a6311e392059`
