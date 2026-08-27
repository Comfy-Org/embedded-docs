# 繪製損失圖表

LossGraphNode 會建立一張折線圖，顯示訓練步驟中的訓練損失值，並將其作為預覽影像顯示。它從訓練節點讀取損失值，將它們繪製在帶有標籤軸及最小/最大損失值的圖表上，然後將圖表作為影像預覽回傳至 UI。

## 輸入
| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `損失` | 來自訓練節點的損失對應表（Loss map）。它必須包含一個 `loss` 鍵，其值為數值損失值的清單。 | LOSS_MAP | 是 | - |
| `檔案名稱前綴` | 已儲存損失圖影像的檔案名稱前綴。（預設值："loss_graph"） | STRING | 是 | - |

## 輸出
| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `ui.images` | 生成的損失圖影像，以預覽方式顯示。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LossGraphNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b1f0b72a03d4ce2d9461fc6e312bd1e847455f7dd5227667876a945494ea8cdb`
