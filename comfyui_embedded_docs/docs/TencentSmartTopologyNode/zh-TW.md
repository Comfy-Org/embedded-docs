> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentSmartTopologyNode/zh-TW.md)

此節點對 3D 模型執行智慧型重新拓撲，自動建立一個具有最佳化多邊形數量的全新、更乾淨的網格。它連接到騰訊混元 3D API 來處理模型，支援最大 200MB 的 GLB 和 OBJ 檔案格式。該節點以 OBJ 檔案形式返回處理後的模型。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `3D 模型` | FILE3D | 是 | - | 輸入的 3D 模型（GLB 或 OBJ）。檔案必須為 GLB 或 OBJ 格式，且不得超過 200MB。 |
| `面組成類型` | STRING | 是 | `"triangle"`<br>`"quadrilateral"` | 表面構成類型。 |
| `面數等級` | STRING | 是 | `"medium"`<br>`"high"`<br>`"low"` | 多邊形簡化程度。 |
| `種子` | INT | 否 | 0 到 2147483647 | 種子值控制節點是否應重新執行；無論種子值為何，結果皆為非確定性。（預設值：0） |

**注意：** `seed` 參數用於觸發節點重新執行，但即使使用相同的種子值，也無法保證最終輸出相同。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `OBJ` | FILE3D | 經過最佳化拓撲處理後的 3D 模型，以 OBJ 格式返回。 |

---
**Source fingerprint (SHA-256):** `13c2dce5f5fbc46a505d0366d8da1c4e762d3a64d11fae1bcceebd510b273f62`
