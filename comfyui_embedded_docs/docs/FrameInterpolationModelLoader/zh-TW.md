# 載入影格插值模型

## 概述

此節點從檔案載入幀插值模型，並為工作流程做好使用準備。它會自動偵測模型類型（FILM 或 RIFE），並針對您的硬體設定模型以獲得最佳效能。

## 輸入

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model_name` | 選擇要載入的幀插值模型。模型必須放置在 `frame_interpolation` 資料夾中。 | COMBO | 是 | `frame_interpolation` 資料夾中的模型檔案清單 |

注意：如果所選檔案不是可辨識的 FILM 或 RIFE 幀插值模型，此節點會引發錯誤。

## 輸出

| 輸出名 | 說明 | 資料型別 |
| --- | --- | --- |
| `FRAME_INTERPOLATION_MODEL` | 已載入並設定完成的幀插值模型，可供其他節點使用。 | INTERP_MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolationModelLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `21f470ee2852dbd1b332ac4a506eaa20dc8578c04b63c4fe1a072878b57beaba`
