> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPVisionLoader/zh-TW.md)

此節點會自動偵測位於 `ComfyUI/models/clip_vision` 資料夾中的模型，以及任何在 `extra_model_paths.yaml` 檔案中設定的額外模型路徑。如果您在啟動 ComfyUI 後新增了模型，請**重新整理 ComfyUI 介面**以確保列出最新的模型檔案。

## 輸入參數

| 欄位名稱    | 資料類型       | 描述 |
|-------------|---------------|-------------|
| `clip_name` | COMBO[STRING]  | 列出 `ComfyUI/models/clip_vision` 資料夾中所有支援的模型檔案。 |

## 輸出參數

| 欄位名稱      | 資料類型     | 描述 |
|--------------|--------------|-------------|
| `clip_vision` | CLIP_VISION  | 已載入的 CLIP Vision 模型，準備好用於圖像編碼或其他視覺相關任務。 |