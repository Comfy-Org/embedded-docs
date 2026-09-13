# 潛空間銳化操作

LatentOperationSharpen 節點會使用基於高斯的卷積核，為潛在表示建立銳化操作。它會將潛在資料標準化，透過卷積套用自訂銳化核，然後還原原始亮度，從而增強潛在空間表示中的細節與邊緣。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `sharpen_radius` | 銳化核的半徑，用於控制銳化區域的大小（預設值：9） | INT | 是 | 1-31 |
| `sigma` | 用於建構銳化核的高斯核標準差（預設值：1.0） | FLOAT | 是 | 0.1-10.0 |
| `alpha` | 銳化強度係數；數值越高，銳化效果越強（預設值：0.1） | FLOAT | 是 | 0.0-5.0 |

這三個輸入皆為進階參數，且具有預設值，因此可以直接使用此節點而無需修改它們。此節點標記為實驗性。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `operation` | 傳回可套用至潛在資料的銳化操作 | LATENT_OPERATION |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8f49b7e47d35547a7169e9ec209328adbe084ee861ac26b9f26e4e644ac14d6d`
