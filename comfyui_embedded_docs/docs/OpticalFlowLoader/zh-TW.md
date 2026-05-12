> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/zh-TW.md)

## 概述

從 `models/optical_flow/` 資料夾載入光流模型。目前僅支援 torchvision 的 RAFT-large 格式，此格式為 VOIDWarpedNoise 節點所使用的模型。ComfyUI 不會自動下載光流權重；您必須手動將檢查點檔案放置在 `models/optical_flow/` 目錄中。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model_name` | STRING | 是 | `models/optical_flow/` 資料夾中的檔案列表 | 要載入的光流模型。檔案必須放置在 `optical_flow` 資料夾中。目前僅支援 torchvision 的 `raft_large.pth`。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `OPTICAL_FLOW` | MODEL | 已載入的光流模型，包裝在 ModelPatcher 中以供其他節點使用。 |