## 概述

Topaz Video Enhance 節點使用外部 API 來提升影片品質。它可以放大影片解析度、透過插值提高影格率，以及套用壓縮。此節點會處理輸入的 MP4 影片，並根據所選設定回傳增強後的版本。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `影片` | 要增強的輸入影片檔案。 | VIDEO | 是 | - |
| `啟用升頻` | 啟用或停用影片放大功能（預設值：True）。 | BOOLEAN | 是 | - |
| `升頻模型` | 用於放大影片的 AI 模型。 | COMBO | 是 | `"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"` |
| `升頻解析度` | 放大影片的目標解析度。 | COMBO | 是 | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `創意程度` | 創意程度（僅適用於 Starlight (Astra) Creative）。（預設值："low"） | COMBO | 否 | `"low"`<br>`"middle"`<br>`"high"` |
| `啟用插幀` | 啟用或停用影格插值功能（預設值：False）。 | BOOLEAN | 否 | - |
| `插幀模型` | 用於影格插值的模型（預設值："apo-8"）。 | COMBO | 否 | `"apo-8"` |
| `慢動作倍數` | 套用至輸入影片的慢動作倍數。例如，2 會使輸出速度減半並使時長加倍。（預設值：1） | INT | 否 | 1 到 16 |
| `輸出幀率` | 輸出影格率。（預設值：60） | INT | 否 | 15 到 240 |
| `移除重複幀` | 分析輸入中的重複影格並將其移除。（預設值：False） | BOOLEAN | 否 | - |
| `重複幀靈敏度` | 重複影格的偵測敏感度。（預設值：0.01） | FLOAT | 否 | 0.001 到 0.1 |
| `CQP 等級` | CQP 等級。（預設值："Low"） | COMBO | 否 | `"Low"`<br>`"Mid"`<br>`"High"` |

**注意：** 至少必須啟用一項增強功能。如果 `upscaler_enabled` 和 `interpolation_enabled` 都設為 `False`，節點將會報錯。輸入影片必須為 MP4 格式。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `影片` | 增強後的輸出影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/zh-TW.md)

---
**Source fingerprint (SHA-256):** `70e1a6e0d7bd250f58c43beefe070fd83af19d11ac08cb9a6ac9655a9bfa839f`
