## 概述

ImageRotate 節點可將輸入影像旋轉至指定角度。它支援四種旋轉選項：不旋轉、順時針旋轉 90 度、旋轉 180 度，以及順時針旋轉 270 度。旋轉操作透過高效的張量運算執行，以確保影像資料的完整性。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `影像` | 要旋轉的輸入影像 | IMAGE | 是 | - |
| `旋轉` | 套用至影像的旋轉角度（預設值："none"） | STRING | 是 | "none"<br>"90 degrees"<br>"180 degrees"<br>"270 degrees" |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `影像` | 旋轉後的輸出影像 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRotate/zh-TW.md)

---
**Source fingerprint (SHA-256):** `068946b31ebe87b2524a1e628b5bc0a3da7367d7252fa7afafe96bcbb174747d`
