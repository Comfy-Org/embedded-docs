# 潛空間銳化操作

LatentOperationSharpen 節點使用高斯核對潛在表示套用銳化效果。其運作方式是將潛在資料標準化，使用自訂銳化核進行卷積，然後還原原始亮度。這能增強潛在空間表示中的細節與邊緣。

## 輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `sharpen_radius` | 銳化核的半徑。完整核大小計算為此值的兩倍加一（預設值：9）。 | INT | 是 | 1-31 |
| `sigma` | 高斯核的標準差（預設值：1.0）。 | FLOAT | 是 | 0.1-10.0 |
| `alpha` | 銳化強度因數，控制效果強度（預設值：0.1）。 | FLOAT | 是 | 0.0-5.0 |

所有輸入均為進階參數。此節點標記為實驗性。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
| --- | --- | --- |
| `operation` | 可套用至潛在資料的銳化操作。將其套用至潛在表示時，會回傳保留原始亮度的銳化版本。 | LATENT_OPERATION |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8f49b7e47d35547a7169e9ec209328adbe084ee861ac26b9f26e4e644ac14d6d`
