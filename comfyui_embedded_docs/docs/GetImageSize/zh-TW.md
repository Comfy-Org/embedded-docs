> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetImageSize/zh-TW.md)

GetImageSize 節點會從輸入影像中提取尺寸與批次資訊。它會回傳影像的寬度、高度及批次大小，同時將這些資訊以進度文字的形式顯示在節點介面上。原始影像資料會保持不變地通過。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|----------|--------|-------|-------------|
| `image` | IMAGE | 是 | - | 要從中提取尺寸資訊的輸入影像 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `width` | INT | 輸入影像的寬度（以像素為單位） |
| `height` | INT | 輸入影像的高度（以像素為單位） |
| `batch_size` | INT | 批次中的影像數量 |

---
**Source fingerprint (SHA-256):** `5cd19ae762d2403c6c5d0740cd5f8c17913daea737fddcff8f0d9da2210e82ab`
