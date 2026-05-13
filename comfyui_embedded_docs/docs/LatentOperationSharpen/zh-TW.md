> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/zh-TW.md)

## 概述

LatentOperationSharpen 節點使用高斯核對潛在表示（latent representations）應用銳化效果。其運作方式是先對潛在資料進行歸一化，接著使用自訂銳化核進行卷積運算，最後還原原始亮度。此過程能增強潛在空間表示中的細節與邊緣。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `sharpen_radius` | INT | 否 | 1-31 | 銳化核的半徑（預設值：9） |
| `sigma` | FLOAT | 否 | 0.1-10.0 | 高斯核的標準差（預設值：1.0） |
| `alpha` | FLOAT | 否 | 0.0-5.0 | 銳化強度因子（預設值：0.1） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `operation` | LATENT_OPERATION | 回傳一個可應用於潛在資料的銳化運算 |

---
**Source fingerprint (SHA-256):** `542754746ab462eb27229ab9b949bb66054ab4c87c77cc59d405b35a2cc27bce`
