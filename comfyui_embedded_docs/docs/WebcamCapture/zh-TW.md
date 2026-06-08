## 概述

WebcamCapture 節點可從網路攝影機裝置擷取影像，並將其轉換為可在 ComfyUI 工作流程中使用的格式。此節點繼承自 LoadImage 節點，並提供控制擷取尺寸與時機的選項。啟用後，該節點可在每次處理工作流程佇列時擷取新的影像。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `影像` | 用於擷取影像的網路攝影機輸入來源 | WEBCAM | 是 | - |
| `寬度` | 擷取影像的所需寬度（預設值：0，使用網路攝影機的原始解析度） | INT | 是 | 0 至 MAX_RESOLUTION |
| `高度` | 擷取影像的所需高度（預設值：0，使用網路攝影機的原始解析度） | INT | 是 | 0 至 MAX_RESOLUTION |
| `排隊時擷取` | 啟用後，每次處理工作流程佇列時都會擷取新影像（預設值：True） | BOOLEAN | 是 | - |

**注意：** 當 `width` 和 `height` 都設為 0 時，節點會使用網路攝影機的原始解析度。將任一尺寸設為非零值將會相應地調整擷取影像的大小。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `IMAGE` | 已轉換為 ComfyUI 影像格式的網路攝影機擷取影像 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WebcamCapture/zh-TW.md)

---
**Source fingerprint (SHA-256):** `551368150fc293309f917eabaa066f223b1fa1a016ffd3643b57b80c83f812cc`
