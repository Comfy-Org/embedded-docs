# 邊界框

## 概述

PrimitiveBoundingBox 節點會建立一個由位置和大小定義的簡單矩形區域。它接收左上角的 X 和 Y 座標，以及寬度和高度值，並輸出一個可供工作流程中其他節點使用的邊界框資料結構。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `x` | 邊界框左上角的 X 座標（預設值：0）。 | INT | 是 | 0 到 8192 |
| `y` | 邊界框左上角的 Y 座標（預設值：0）。 | INT | 是 | 0 到 8192 |
| `寬度` | 邊界框的寬度（預設值：512）。 | INT | 是 | 1 到 8192 |
| `高度` | 邊界框的高度（預設值：512）。 | INT | 是 | 1 到 8192 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `bounding_box` | 包含所定義矩形之 `x`、`y`、`寬度` 和 `高度` 屬性的資料結構。 | BOUNDING_BOX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveBoundingBox/zh-TW.md)

---
**Source fingerprint (SHA-256):** `715f1a2bd650ecd6ba2ea3c1d54636bc32dff4fb4aec8f088ee9b0994809412c`
