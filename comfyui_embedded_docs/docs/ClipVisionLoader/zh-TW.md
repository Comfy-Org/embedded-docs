此節點會自動偵測位於 `ComfyUI/models/clip_vision` 資料夾中的模型，以及 `extra_model_paths.yaml` 檔案中設定的任何其他模型路徑。如果您在啟動 ComfyUI 後新增模型，請**重新整理 ComfyUI 介面**，以確保列出最新的模型檔案。

## 輸入

| 欄位 | 說明 | 資料類型 |
| --- | --- | --- |
| `clip_name` | 列出 `ComfyUI/models/clip_vision` 資料夾中所有支援的模型檔案。 | COMBO[STRING] |

## 輸出

| 欄位 | 說明 | 資料類型 |
| --- | --- | --- |
| `clip_vision` | 已載入的 CLIP Vision 模型，可用於編碼影像或其他與視覺相關的任務。 | CLIP_VISION |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPVisionLoader/zh-TW.md)
