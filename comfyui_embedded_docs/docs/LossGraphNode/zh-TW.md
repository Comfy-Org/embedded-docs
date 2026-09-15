# 繪製損失圖表

LossGraphNode 會建立訓練損失值隨訓練步數變化的折線圖，並將其顯示為預覽影像。它會從訓練節點讀取損失值，將其繪製到具有標示軸及最小/最大損失值的圖表上，並在 UI 中將圖表作為影像預覽傳回。此節點標記為實驗性，且為輸出節點。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `損失` | 來自訓練節點的損失映射。必須包含一個 `loss` 鍵，其值為數值損失值清單。 | LOSS_MAP | 是 | - |
| `檔案名稱前綴` | 儲存的損失圖表影像之檔名前綴。（預設："loss_graph"） | STRING | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `ui.images` | 產生的損失圖表影像，會顯示為預覽。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LossGraphNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b1f0b72a03d4ce2d9461fc6e312bd1e847455f7dd5227667876a945494ea8cdb`
