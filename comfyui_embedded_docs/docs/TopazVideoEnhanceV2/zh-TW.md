> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhanceV2/zh-TW.md)

# Topaz Video Enhance V2

**Topaz Video Enhance V2** 節點可讓您使用 Topaz Labs 的 AI 模型來提升影片解析度與增強畫質。它能增加解析度、透過插幀調整影格率，並應用創意或寫實的增強效果，為您的影片素材注入新生命。

## ## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | 是 | - | 要處理的輸入影片。必須為 MP4 容器格式。 |
| `upscaler_model` | COMBO | 是 | `"Astra 2"`<br>`"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"`<br>`"Disabled"` | 用於提升影片解析度的 AI 模型。選擇 "Disabled" 表示不套用任何升頻處理。 |
| `upscaler_model.upscaler_resolution` | COMBO | 條件式 | `"FullHD (1080p)"`<br>`"4K (2160p)"` | 升頻器的目標輸出解析度。當選取了升頻模型（非 "Disabled"）時，此參數為必填。 |
| `upscaler_model.creativity` | FLOAT | 條件式 | 0.0 至 1.0（步進 0.1） | 升頻的創意強度。僅適用於 "Astra 2" 和 "Starlight (Astra) Creative" 模型。預設值：Astra 2 為 0.5，Starlight Creative 為 "low"。 |
| `upscaler_model.prompt` | STRING | 否 | - | 可選的描述性（非指令性）場景提示。僅適用於 "Astra 2" 模型。設定後最多處理 500 個輸入影格（約 30fps 下的 15 秒）。預設值：空白。 |
| `upscaler_model.sharp` | FLOAT | 否 | 0.0 至 1.0（步進 0.01） | 預增強銳利度：0.0=高斯模糊，0.5=直通（預設），1.0=USM 銳化。僅適用於 "Astra 2" 模型。預設值：0.5。 |
| `upscaler_model.realism` | FLOAT | 否 | 0.0 至 1.0（步進 0.01） | 將輸出推向攝影寫實風格。設為 0 則使用模型預設值。僅適用於 "Astra 2" 模型。預設值：0.0。 |
| `interpolation_model` | COMBO | 是 | `"Disabled"`<br>`"apo-8"` | 用於影格插值的 AI 模型。選擇 "Disabled" 表示不套用任何插值處理。 |
| `interpolation_model.interpolation_frame_rate` | INT | 條件式 | 15 至 240 | 輸出影格率。當插值模型為 "apo-8" 時為必填。預設值：60。 |
| `interpolation_model.interpolation_slowmo` | INT | 否 | 1 至 16 | 套用於輸入影片的慢動作倍數。例如，設為 2 會使輸出速度減半，時長加倍。預設值：1。 |
| `interpolation_model.interpolation_duplicate` | BOOLEAN | 否 | True/False | 分析輸入影片中的重複影格並將其移除。預設值：False。 |
| `interpolation_model.interpolation_duplicate_threshold` | FLOAT | 否 | 0.001 至 0.1（步進 0.001） | 重複影格的偵測敏感度。預設值：0.01。 |
| `dynamic_compression_level` | COMBO | 否 | `"Low"`<br>`"Mid"`<br>`"High"` | 影片壓縮的 CQP 等級。預設值："Low"。 |

**重要限制：**
- `upscaler_model` 或 `interpolation_model` 至少需啟用一個（非 "Disabled"），否則會引發錯誤。
- 輸入影片必須為 MP4 容器格式。
- 使用提示詞的 "Astra 2" 模型最多處理 500 個輸入影格（約 30fps 下的 15 秒）。未使用提示詞時則可處理更多影格。
- 當 `upscaler_model` 非 "Disabled" 時，`upscaler_resolution` 子參數為必填。
- 當 `interpolation_model` 非 "Disabled" 時，`interpolation_frame_rate` 子參數為必填。

## ## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `video` | VIDEO | 套用所選升頻及/或插值濾鏡後的增強影片輸出。 |