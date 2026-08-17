# 繪製損失圖表

LossGraphNode 會建立訓練損失值隨時間變化的視覺圖表，並將其顯示為預覽影像。它從訓練流程中取得損失資料，並產生一條折線圖，顯示損失在訓練步驟中的變化。產生的圖表包含軸標籤以及最小/最大損失值。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `loss` | 來自訓練節點的損失對應。必須包含一個 `loss` 鍵，其中包含用於繪製圖表的損失值清單。 | LOSS_MAP | 是 | - |
| `filename_prefix` | 已儲存損失圖表影像的前置詞。(預設值："loss_graph") | STRING | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `ui.images` | 產生的損失圖表影像，以預覽方式顯示。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LossGraphNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b1f0b72a03d4ce2d9461fc6e312bd1e847455f7dd5227667876a945494ea8cdb`
