> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolationModelLoader/zh-TW.md)

## 概述

此節點從檔案載入影格插值模型，並將其準備好以供工作流程使用。它會自動偵測模型類型（FILM 或 RIFE），並為您的硬體配置最佳效能。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model_name` | STRING | 是 | `frame_interpolation` 資料夾中的模型檔案清單 | 選擇要載入的影格插值模型。模型必須放置在 'frame_interpolation' 資料夾中。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `FRAME_INTERPOLATION_MODEL` | MODEL | 已載入並配置完成的影格插值模型，可供其他節點使用。 |