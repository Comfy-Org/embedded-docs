# 依較長邊調整圖片尺寸

## 概述

依較長邊調整影像大小節點可將一張或多張影像調整大小，使其最長邊符合指定的目標長度。此節點會自動判斷寬度或高度何者較長，並按比例縮放另一邊，以保留原始長寬比。這對於根據影像的最大尺寸來標準化影像大小非常實用。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `image` | 要調整大小的輸入影像或影像批次。 | IMAGE | 是 | - |
| `longer_edge` | 較長邊的目標長度。較短邊將按比例縮放。（預設值：1024） | INT | 是 | 1 - 8192 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `images` | 調整大小後的影像或影像批次。輸出影像數量與輸入相同，且每張影像的較長邊都符合指定的 `longer_edge` 長度。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByLongerEdge/zh-TW.md)

---
**Source fingerprint (SHA-256):** `687d5f159967eccbf64f0ec529ae6edeb94f4707ae10a3c75a5d0b08c86dd828`
