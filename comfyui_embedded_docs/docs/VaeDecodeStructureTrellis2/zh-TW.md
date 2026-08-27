# VaeDecodeStructureTrellis2

此節點使用 VAE 的結構解碼器將 Trellis 結構潛在樣本轉換為 3D 體素網格。它僅讀取潛在向量的前 8 個通道，重建體素佔用情況，並根據請求將輸出解析度調整為 32 或 64。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `samples` | 要解碼的結構的潛在表示。僅使用潛在向量的前 8 個通道進行解碼。 | LATENT | 是 | - |
| `vae` | 其結構解碼器將潛在表示轉換為體素網格的 VAE。解碼以批次方式執行。 | VAE | 是 | - |
| `resolution` | 輸出體素網格的目標空間解析度（預設值："32"）。如果解碼後的網格具有不同解析度，則將其下採樣以匹配。 | COMBO | 是 | "32"<br>"64" |

注意：當解碼後的體素網格解析度與所選的 `resolution` 不同時，會使用 3D 最大池化將網格下採樣到請求的大小。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `voxel` | 一個二進制體素佔用網格，作為形狀為 [batch, depth, height, width] 的浮點張量。佔用體素的值為 1.0，空體素的值為 0.0。 | VOXEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeStructureTrellis2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `37764ef7351b3619d4cddb57b11d9a0da24dadeedc0fc0f70d089038d37e03b0`
