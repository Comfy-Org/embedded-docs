# 將 DA3 幾何圖形轉換為點雲

此節點將來自 DA3_GEOMETRY 物件的深度圖轉換為 3D 點雲。它會根據置信度和天空遮罩進行過濾，並將點轉換為適用於多視角場景的通用世界座標系統。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `da3_geometry` | 包含深度資料以及可選的影像、置信度和天空地圖的 DA3_GEOMETRY 物件 | DA3_GEOMETRY | 是 | - |
| `batch_index` | 要轉換的批次中的哪一張影像（預設值：0） | INT | 是 | 0 至 4096 |
| `confidence_threshold` | 排除每張影像正規化置信度低於此值的像素（0 = 保留所有）。當幾何圖形具有置信度地圖（小型/基礎模型）時使用。（預設值：0.1） | FLOAT | 是 | 0.0 至 1.0 |
| `use_sky_mask` | 排除天空機率像素（天空 >= 0.5）。當幾何圖形具有天空地圖（單目/度量模型）時使用。（預設值：True） | BOOLEAN | 是 | True 或 False |
| `downsample` | 每隔 N 個像素取一個（1 = 完整解析度）。數值越大，點數越少，處理速度越快。（預設值：1） | INT | 是 | 1 至 16 |

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `point_cloud` | 包含過濾後的 3D 點、可選顏色和可選置信度值的點雲物件 | DA3_POINT_CLOUD |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3GeometryToPointCloud/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3cf5bdbb8afdfcfc02f9832a8cbc5a3df49da755dea6df01792aa6ef9e5d7287`
