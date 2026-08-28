# 載入光流模型

從 `models/optical_flow/` 資料夾載入光流模型。目前僅支援 torchvision 的 RAFT-large 格式，即 VOIDWarpedNoise 節點所使用的模型。ComfyUI 不會自動下載光流權重；您必須手動將檢查點檔案放置在 `models/optical_flow/` 目錄中。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model_name` | 要載入的光流模型。檔案必須放置在 `optical_flow` 資料夾中。目前僅支援 torchvision 的 `raft_large.pth`。 | COMBO | 是 | `models/optical_flow/` 資料夾中的檔案列表 |

注意：所選的檢查點必須是 torchvision RAFT-large 狀態字典，其中包含以 `feature_encoder.`、`context_encoder.` 和 `update_block.` 為前綴的鍵。如果檔案不符合此格式，節點會引發 ValueError。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `OPTICAL_FLOW` | 載入的光流模型，設定為評估模式和 float32 精度，包裝在 ModelPatcher 中以供其他節點使用。 | OPTICAL_FLOW |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5e79551545ad7ee2fd4856a47da29808a404342d1d5e57da0980058db6b11c3b`
