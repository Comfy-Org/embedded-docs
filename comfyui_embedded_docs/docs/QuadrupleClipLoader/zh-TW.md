> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuadrupleCLIPLoader/zh-TW.md)

## 概述

Quadruple CLIP Loader（四重 CLIP 載入器）是 ComfyUI 的核心節點之一，最初為支援 HiDream I1 版本模型而新增。若您發現此節點缺失，請嘗試將 ComfyUI 更新至最新版本以確保節點支援。

此節點需要 4 個 CLIP 模型，分別對應參數 `clip_name1`、`clip_name2`、`clip_name3` 和 `clip_name4`，並將提供一個 CLIP 模型輸出供後續節點使用。

此節點會偵測位於 `ComfyUI/models/text_encoders` 資料夾中的模型，同時也會讀取在 extra_model_paths.yaml 檔案中設定的其他路徑中的模型。有時在新增模型後，您可能需要**重新載入 ComfyUI 介面**，以便讓它讀取對應資料夾中的模型檔案。