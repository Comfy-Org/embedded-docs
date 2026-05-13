> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByShorterEdge/zh-TW.md)

此節點會調整影像尺寸，使較短邊符合指定的長度，同時保留原始長寬比。它根據較短邊的目標長度計算新尺寸，並傳回調整後的影像。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 要調整尺寸的輸入影像。 |
| `shorter_edge` | INT | 否 | 1 至 8192 | 較短邊的目標長度。（預設值：512） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `image` | IMAGE | 調整後的影像，其較短邊符合指定的目標長度。 |

---
**Source fingerprint (SHA-256):** `011949390faa9032587aec210d9e38d55b79e474c7a6dcd5d3c0e75594a1fc29`
