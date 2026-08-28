# Topaz Video Enhance

### Topaz Video Enhance 節點

Topaz Video Enhance 節點利用強大的升頻與恢復技術，透過外部 API 提升影片品質，為影片注入新的生命力。它能提升影片解析度、透過影格插值增加幀率，並套用壓縮。此節點處理輸入的 MP4 影片，並根據所選設定回傳增強後的版本。此節點已標記為過時（舊版）。

## 輸入

| 參數 | 描述 | 資料型態 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影片` | 要增強的輸入影片檔案。 | VIDEO | 是 | - |
| `啟用升頻` | 啟用或停用影片升頻功能（預設值：True）。 | BOOLEAN | 是 | - |
| `升頻模型` | 用於影片升頻的 AI 模型。 | COMBO | 是 | `"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"` |
| `升頻解析度` | 升頻後影片的目標解析度。 | COMBO | 是 | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `創意程度` | 創意等級（僅適用於 Starlight (Astra) Creative）。（預設值："low"） | COMBO | 否 | `"low"`<br>`"middle"`<br>`"high"` |
| `啟用插幀` | 啟用或停用影格插值功能（預設值：False）。 | BOOLEAN | 否 | - |
| `插幀模型` | 用於影格插值的模型（預設值："apo-8"）。 | COMBO | 否 | `"apo-8"` |
| `慢動作倍數` | 套用於輸入影片的慢動作倍率。例如，設定為 2 會使輸出影片的速度減半，並使持續時間加倍。（預設值：1） | INT | 否 | 1 至 16 |
| `輸出幀率` | 輸出幀率。（預設值：60） | INT | 否 | 15 至 240 |
| `移除重複幀` | 分析輸入中是否有重複影格並將其移除。（預設值：False） | BOOLEAN | 否 | - |
| `重複幀靈敏度` | 重複影格的偵測靈敏度。（預設值：0.01） | FLOAT | 否 | 0.001 至 0.1 |
| `CQP 等級` | CQP 等級。（預設值："Low"） | COMBO | 否 | `"Low"`<br>`"Mid"`<br>`"High"` |

**注意：** 至少必須啟用一個增強功能。如果 `upscaler_enabled` 和 `interpolation_enabled` 皆設為 False，節點將引發錯誤。輸入影片必須為 MP4 格式。`upscaler_creativity` 設定僅在 `upscaler_model` 設為 "Starlight (Astra) Creative" 時適用。不支援需要分段上傳的非常大的影片檔案。

## 輸出

| 輸出名稱 | 描述 | 資料型態 |
|-------------|-------------|-----------|
| `video` | 增強後的輸出影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b3b14a301b529256ddf04b7e3a9b99814ad5bfa149366b2a5c51c396dbffb190`
