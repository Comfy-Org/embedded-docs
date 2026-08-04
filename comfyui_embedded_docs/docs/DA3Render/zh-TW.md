# 渲染 Depth Anything 3

此節點可從 Depth Anything 3 幾何數據渲染視覺化內容。根據選擇的輸出模式，它可以輸出深度圖、置信度圖或天空遮罩。

## ## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `da3_geometry` | 包含深度資料的 Depth Anything 3 幾何數據包，可選包含天空和置信度張量 | DA3_GEOMETRY | 是 | - |
| `output` | 要渲染的視覺化類型。<br>- depth：歸一化的灰階深度影像。<br>- depth_colored：透過 Turbo 色彩映射的深度。<br>- sky_mask：天空機率，範圍 [0, 1]（僅適用於 Mono/Metric 模型）。<br>- confidence：歸一化的深度置信度（僅適用於 Small/Base 模型）。 | COMBO | 是 | "depth"<br>"depth_colored"<br>"sky_mask"<br>"confidence" |

### `output` 選項的子參數

當 `output` 設定為 `"depth"` 或 `"depth_colored"` 時：

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `normalization` | 深度正規化方法。<br>- v2_style：平均值/標準差正規化，獲得感知平衡的結果（預設）。<br>- min_max：將完整深度範圍拉伸至 [0, 1]，獲得最大對比度。<br>- raw：不進行縮放，保留 Metric 模型的公制單位。 | COMBO | 是 | "v2_style"<br>"min_max"<br>"raw" |
| `apply_sky_clip` | 在正規化前將天空區域的深度裁剪至前景深度的第 99 百分位數。需要在 da3_geometry 輸入中包含天空鍵值（僅適用於 Mono/Metric 模型）。預設：False | BOOLEAN | 是 | True<br>False |

當 `output` 設定為 `"sky_mask"` 時：

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `colored` | 對天空遮罩套用 Turbo 色彩映射。預設：False | BOOLEAN | 是 | True<br>False |

當 `output` 設定為 `"confidence"` 時：

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `colored` | 對置信度圖套用 Turbo 色彩映射。預設：False | BOOLEAN | 是 | True<br>False |

### 參數限制

- 當 `apply_sky_clip` 設定為 True 時，`da3_geometry` 輸入必須包含天空張量。此功能僅在使用 Mono 或 Metric 模型時可用。如果缺少天空張量，節點將引發錯誤。
- `sky_mask` 輸出選項需要在 `da3_geometry` 輸入中包含天空張量。此功能僅適用於 Mono 或 Metric 模型。
- `confidence` 輸出選項需要在 `da3_geometry` 輸入中包含置信度張量。此功能僅適用於 Small 或 Base 模型。

## ## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-----------|-------------|-----------|
| `IMAGE` | 渲染後的視覺化圖像張量。對於深度輸出，返回灰階或彩色深度圖。對於 sky_mask 和 confidence，根據 colored 參數返回灰階或彩色視覺化結果。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3Render/zh-TW.md)

---
**Source fingerprint (SHA-256):** `54d4cde95a916cac26c8a2e19c5623e794d46c0d7652f1c8204f9f2a0deabe0c`
