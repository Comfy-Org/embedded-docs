# HitPaw 影片增強

HitPaw Video Enhance 節點使用外部 API 來提升影片品質。它可將低解析度影片放大至更高解析度、移除視覺偽影，並減少雜訊。處理成本是根據輸入影片的秒數計算。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 用於影片增強功能的 AI 模型。選擇模型後會顯示巢狀的 `resolution` 參數。可用的模型及其支援的解析度會有所不同。 | DYNAMIC_COMBO | 是 | `"Portrait Restore Model (1x)"`<br>`"Portrait Restore Model (2x)"`<br>`"General Restore Model (1x)"`<br>`"General Restore Model (2x)"`<br>`"General Restore Model (4x)"`<br>`"Ultra HD Model (2x)"`<br>`"Generative Model (1x)"` |
| `影片` | 要增強的輸入影片檔案。 | VIDEO | 是 | 不適用 |

### Portrait Restore、General Restore 與 Ultra HD Model 輸入

以下解析度選項由 Portrait Restore Model (1x)、Portrait Restore Model (2x)、General Restore Model (1x)、General Restore Model (2x)、General Restore Model (4x) 與 Ultra HD Model (2x) 共用。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `解析度` | 增強後影片的目標解析度。選擇 `"original"` 會保留輸入影片的解析度。 | COMBO | 是 | `"original"`<br>`"720p"`<br>`"1080p"`<br>`"2K/QHD"`<br>`"4K/UHD"`<br>`"8K"` |

### Generative Model (1x) 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `解析度` | 增強後影片的目標解析度。選擇 `"original"` 會保留輸入影片的解析度。此模型不提供 `"8K"` 選項。 | COMBO | 是 | `"original"`<br>`"720p"`<br>`"1080p"`<br>`"2K/QHD"`<br>`"4K/UHD"` |

**注意事項：**

* 輸入的 `video` 長度必須介於 0.5 秒到 60 分鐘（3600 秒）之間。
* 所選的 `resolution` 至少必須大於或等於輸入影片的尺寸。對於方形影片，必須至少大於或等於影片的寬度和高度。對於非方形影片，必須至少大於或等於影片的較短邊。如果目標解析度較小，則會引發錯誤。選擇 `"original"` 會保留輸入影片的解析度。
* 當選擇 `"original"` 以外的解析度時，非方形影片會按比例縮放，使其較短邊符合所選解析度，同時保留長寬比。方形影片則會縮放至所選解析度的方形目標尺寸（例如 `"4K/UHD"` 會產生 2048×2048）。

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `video` | 增強後的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawVideoEnhance/zh-TW.md)

---
**Source fingerprint (SHA-256):** `42803c7137d62dbce5021cd2bd9b9fba1a89c80e7b3f237f8a0eb03858c49967`
