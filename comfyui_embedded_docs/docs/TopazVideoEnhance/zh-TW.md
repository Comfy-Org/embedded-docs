> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/zh-TW.md)

Topaz Video Enhance 節點使用外部 API 來提升影片品質。它可以放大影片解析度、透過插幀提高幀率，並應用壓縮。此節點會處理輸入的 MP4 影片，並根據所選設定返回增強後的版本。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | 是 | - | 要進行增強處理的輸入影片檔案。 |
| `upscaler_enabled` | BOOLEAN | 是 | - | 啟用或停用影片放大功能（預設值：True）。 |
| `upscaler_model` | COMBO | 是 | `"Proteus v3"`<br>`"Artemis v13"`<br>`"Artemis v14"`<br>`"Artemis v15"`<br>`"Gaia v6"`<br>`"Theia v3"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight (Astra) Optimized"`<br>`"Starlight (Astra) Balanced"`<br>`"Starlight (Astra) Quality"`<br>`"Starlight (Astra) Speed"` | 用於影片放大的 AI 模型。 |
| `upscaler_resolution` | COMBO | 是 | `"FullHD (1080p)"`<br>`"4K (2160p)"` | 放大影片的目標解析度。 |
| `upscaler_creativity` | COMBO | 否 | `"low"`<br>`"middle"`<br>`"high"` | 創意等級（僅適用於 Starlight (Astra) Creative 模型）。（預設值："low"） |
| `interpolation_enabled` | BOOLEAN | 否 | - | 啟用或停用幀插值功能（預設值：False）。 |
| `interpolation_model` | COMBO | 否 | `"apo-8"` | 用於幀插值的模型（預設值："apo-8"）。 |
| `interpolation_slowmo` | INT | 否 | 1 到 16 | 應用於輸入影片的慢動作係數。例如，2 會使輸出速度減半，並使持續時間加倍。（預設值：1） |
| `interpolation_frame_rate` | INT | 否 | 15 到 240 | 輸出幀率。（預設值：60） |
| `interpolation_duplicate` | BOOLEAN | 否 | - | 分析輸入影片中的重複幀並將其移除。（預設值：False） |
| `interpolation_duplicate_threshold` | FLOAT | 否 | 0.001 到 0.1 | 重複幀的檢測靈敏度。（預設值：0.01） |
| `dynamic_compression_level` | COMBO | 否 | `"Low"`<br>`"Mid"`<br>`"High"` | CQP 等級。（預設值："Low"） |

**注意：** 必須至少啟用一項增強功能。如果 `upscaler_enabled` 和 `interpolation_enabled` 均設為 `False`，節點將引發錯誤。輸入影片必須為 MP4 格式。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `video` | VIDEO | 增強後的輸出影片檔案。 |
