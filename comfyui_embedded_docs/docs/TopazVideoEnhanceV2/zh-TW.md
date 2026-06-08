# Topaz Video Enhance V2

**Topaz Video Enhance V2** 節點讓您能夠使用 Topaz Labs 的 AI 模型來提升影片解析度與增強畫質。它可以增加解析度、透過插值調整影格率，並應用創意或寫實的增強效果，為您的影片素材注入新生命。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `影片` | 要處理的輸入影片。必須為 MP4 容器格式。 | VIDEO | 是 | - |
| `升頻模型` | 用於提升影片解析度的 AI 模型。選擇 "Disabled" 表示不套用任何升頻處理。 | COMBO | 是 | `"Astra 2"`<br>`"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"`<br>`"Disabled"` |
| `upscaler_model.upscaler_resolution` | 升頻器的目標輸出解析度。當選取了升頻模型（非 "Disabled"）時，此參數為必要。 | COMBO | 條件式 | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `upscaler_model.creativity` | 升頻的創意強度。僅適用於 "Astra 2" 和 "Starlight (Astra) Creative" 模型。對於 Astra 2，為滑桿（預設值：0.5）。對於 Starlight Creative，為下拉選單（預設值："low"）。 | FLOAT / COMBO | 條件式 | Astra 2: 0.0 至 1.0（間距 0.1）<br>Starlight Creative: `"low"`<br>`"middle"`<br>`"high"` |
| `upscaler_model.prompt` | 可選的描述性（非指令性）場景提示。僅適用於 "Astra 2" 模型。設定時，輸入影格上限為 500 幀（約 30fps 下的 15 秒）。預設值：空白。 | STRING | 否 | - |
| `upscaler_model.sharp` | 預增強銳利度：0.0=高斯模糊，0.5=直通（預設值），1.0=USM 銳化。僅適用於 "Astra 2" 模型。預設值：0.5。 | FLOAT | 否 | 0.0 至 1.0（間距 0.01） |
| `upscaler_model.realism` | 將輸出推向攝影寫實風格。設為 0 則使用模型預設值。僅適用於 "Astra 2" 模型。預設值：0.0。 | FLOAT | 否 | 0.0 至 1.0（間距 0.01） |
| `插值模型` | 用於影格插值的 AI 模型。選擇 "Disabled" 表示不套用任何插值處理。 | COMBO | 是 | `"Disabled"`<br>`"apo-8"` |
| `interpolation_model.interpolation_frame_rate` | 輸出影格率。當插值模型為 "apo-8" 時為必要。預設值：60。 | INT | 條件式 | 15 至 240 |
| `interpolation_model.interpolation_slowmo` | 套用至輸入影片的慢動作倍數。例如，2 會使輸出速度減半並使時長加倍。預設值：1。 | INT | 否 | 1 至 16 |
| `interpolation_model.interpolation_duplicate` | 分析輸入中是否有重複影格並將其移除。預設值：False。 | BOOLEAN | 否 | True/False |
| `interpolation_model.interpolation_duplicate_threshold` | 重複影格的偵測敏感度。預設值：0.01。 | FLOAT | 否 | 0.001 至 0.1（間距 0.001） |
| `動態壓縮等級` | 影片壓縮的 CQP 等級。預設值："Low"。 | COMBO | 否 | `"Low"`<br>`"Mid"`<br>`"High"` |

**重要限制：**
- `upscaler_model` 或 `interpolation_model` 中至少必須啟用一個（非 "Disabled"），否則會引發錯誤。
- 輸入影片必須為 MP4 容器格式。
- 帶有提示的 "Astra 2" 模型限制為 500 個輸入影格（約 30fps 下的 15 秒）。無提示時，則有更高的影格數限制。
- 當 `upscaler_model` 非 "Disabled" 時，`upscaler_resolution` 子參數為必要。
- 當 `interpolation_model` 非 "Disabled" 時，`interpolation_frame_rate` 子參數為必要。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `影片` | 套用所選升頻及/或插值濾鏡後的增強影片輸出。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhanceV2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `29b7538206327c35866126c1862c1d1ccea872ba84fbb9c84126114a06e2b00f`
