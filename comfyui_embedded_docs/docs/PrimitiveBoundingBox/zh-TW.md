# 邊界框

PrimitiveBoundingBox 節點會建立一個由其位置和大小定義的簡單矩形區域。它接受左上角的 X 和 Y 座標，以及寬度和高度值，並輸出一個邊界框資料結構，可供工作流程中的其他節點使用。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `x` | 邊界框左上角的 X 座標（預設值：0）。 | INT | 是 | 0 至 16384 |
| `y` | 邊界框左上角的 Y 座標（預設值：0）。 | INT | 是 | 0 至 16384 |
| `寬度` | 邊界框的寬度（預設值：512）。 | INT | 是 | 1 至 16384 |
| `高度` | 邊界框的高度（預設值：512）。 | INT | 是 | 1 至 16384 |

注意：所有最大值皆遵循 ComfyUI 的 MAX_RESOLUTION 常數，此常數定義節點可接受的最大影像尺寸。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `bounding_box` | 包含所定義矩形的 `x`、`y`、`width` 和 `height` 屬性的資料結構。 | BOUNDING_BOX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveBoundingBox/zh-TW.md)

---
**Source fingerprint (SHA-256):** `dc50286b09b8aaf7ff21eb699b9a04317f099b3deedb6cb7d4a1ec7668edeb97`
