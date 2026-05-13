> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveBoundingBox/zh-TW.md)

## 概述

PrimitiveBoundingBox 節點會建立一個由位置和大小定義的簡單矩形區域。它接收左上角的 X 和 Y 座標，以及寬度和高度值，並輸出一個可供工作流程中其他節點使用的邊界框資料結構。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `x` | INT | 是 | 0 到 8192 | 邊界框左上角的 X 座標（預設值：0）。 |
| `y` | INT | 是 | 0 到 8192 | 邊界框左上角的 Y 座標（預設值：0）。 |
| `width` | INT | 是 | 1 到 8192 | 邊界框的寬度（預設值：512）。 |
| `height` | INT | 是 | 1 到 8192 | 邊界框的高度（預設值：512）。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `bounding_box` | BOUNDING_BOX | 包含所定義矩形之 `x`、`y`、`width` 和 `height` 屬性的資料結構。 |

---
**Source fingerprint (SHA-256):** `715f1a2bd650ecd6ba2ea3c1d54636bc32dff4fb4aec8f088ee9b0994809412c`
