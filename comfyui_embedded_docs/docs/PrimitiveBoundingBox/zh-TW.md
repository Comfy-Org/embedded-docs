# 邊界框

PrimitiveBoundingBox 節點會建立一個由其位置和大小定義的簡單矩形區域。它接收左上角的 X 與 Y 座標，以及寬度和高度數值，並輸出一個可供工作流程中其他節點使用的邊界框資料結構。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `x` | 邊界框左上角的 X 座標（預設值：0）。 | INT | 是 | 0 至 8192 |
| `y` | 邊界框左上角的 Y 座標（預設值：0）。 | INT | 是 | 0 至 8192 |
| `width` | 邊界框的寬度（預設值：512）。 | INT | 是 | 1 至 8192 |
| `height` | 邊界框的高度（預設值：512）。 | INT | 是 | 1 至 8192 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `bounding_box` | 包含所定義矩形之 `x`、`y`、`width` 與 `height` 屬性的資料結構。 | BOUNDING_BOX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveBoundingBox/zh-TW.md)

---
**Source fingerprint (SHA-256):** `dc50286b09b8aaf7ff21eb699b9a04317f099b3deedb6cb7d4a1ec7668edeb97`
