# 載入影格插值模型

此節點會載入影格插值模型檔案，並將其準備好以供工作流程使用。它會自動偵測該檔案是 FILM 還是 RIFE 模型，並針對可用硬體設定模型。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型名稱` | 選擇要載入的影格插值模型。模型必須放在 `frame_interpolation` 資料夾中。 | COMBO | 是 | `frame_interpolation` 資料夾中的模型檔案清單 |

注意：此節點支援 FILM 與 RIFE 模型格式。若選取的檔案不是可辨識的格式，將會引發錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `FRAME_INTERPOLATION_MODEL` | 已載入並設定完成的影格插值模型，可供其他節點使用。 | INTERP_MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolationModelLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `21f470ee2852dbd1b332ac4a506eaa20dc8578c04b63c4fe1a072878b57beaba`
