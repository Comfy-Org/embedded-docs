# 載入光流模型

## 概述

從 `models/optical_flow/` 資料夾載入光流模型。目前僅支援 torchvision 的 RAFT-large 格式，此格式是 VOIDWarpedNoise 節點所使用的模型。ComfyUI 不會自動下載光流權重；您必須手動將檢查點檔案放置在 `models/optical_flow/` 目錄中。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model_name` | 要載入的光流模型。檔案必須放置在 `optical_flow` 資料夾中。目前僅支援 torchvision 的 `raft_large.pth`。 | COMBO | 是 | `models/optical_flow/` 資料夾中的檔案列表 |

選取的檔案必須是 torchvision RAFT-large 檢查點。節點會檢查檔案是否包含預期的 RAFT 鍵（`feature_encoder.*`、`context_encoder.*` 和 `update_block.*`），如果格式無法辨識，則拋出 ValueError。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `OPTICAL_FLOW` | 已載入的光流模型，包裝在 ModelPatcher 中以供其他節點使用。 | OPTICAL_FLOW |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5e79551545ad7ee2fd4856a47da29808a404342d1d5e57da0980058db6b11c3b`
