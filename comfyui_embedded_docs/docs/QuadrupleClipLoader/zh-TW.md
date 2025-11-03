> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuadrupleCLIPLoader/zh-TW.md)

{heading_overview}

Quadruple CLIP Loader（QuadrupleCLIPLoader）是 ComfyUI 的核心節點之一，最初是為了支援 HiDream I1 版本模型而添加。如果您發現缺少此節點，請嘗試將 ComfyUI 更新至最新版本以確保節點支援。

它需要 4 個 CLIP 模型，分別對應參數 `clip_name1`、`clip_name2`、`clip_name3` 和 `clip_name4`，並將提供 CLIP 模型輸出供後續節點使用。

此節點會偵測位於 `ComfyUI/models/text_encoders` 資料夾中的模型，
同時也會從 extra_model_paths.yaml 檔案中配置的額外路徑讀取模型。
有時在添加模型後，您可能需要**重新載入 ComfyUI 介面**，以便讓它讀取相應資料夾中的模型檔案。