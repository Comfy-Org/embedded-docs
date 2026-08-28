# Topaz 影片增強

**Topaz Video Enhance V2** 節點藉由強大的解析度提升與修復技術，為影片注入新生命。它可使用不同的 Topaz 放大模型來提高影片解析度、透過幀插值調整幀率，並套用創意或寫實的增強設定。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `影片` | 要處理的輸入影片。必須為 MP4 容器格式。 | VIDEO | 是 | - |
| `升頻模型` | 用於放大影片的 AI 模型。可用的子參數取決於所選模型。選取 `"Disabled"` 會停用放大。 | DYNAMIC_COMBO | 是 | `"Astra 2"`<br>`"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"`<br>`"Disabled"` |
| `插值模型` | 用於幀插值的 AI 模型。可用的子參數取決於所選模型。選取 `"Disabled"` 會停用插值。 | DYNAMIC_COMBO | 是 | `"Disabled"`<br>`"apo-8"` |
| `動態壓縮等級` | 用於影片壓縮的 CQP 等級（預設：`"Low"`）。 | COMBO | 否 | `"Low"`<br>`"Mid"`<br>`"High"` |

以下各節說明 `upscaler_model` 與 `interpolation_model` 選擇器各選項所顯示的子參數。`"Disabled"` 選項不會顯示任何額外參數。

### Astra 2 輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | 目標輸出解析度。 | COMBO | 是（選取「Astra 2」時） | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `upscaler_model.creativity` | 放大效果的創意強度（預設：0.5）。 | FLOAT | 否 | 0.0 至 1.0 (step 0.1) |
| `upscaler_model.prompt` | 選用的描述性（非指令性）場景提示。設定後輸入上限為 450 幀（約 15 秒 @ 30fps）（預設：空白）。 | STRING | 否 | - |
| `upscaler_model.sharp` | 增強前的銳利度：0.0=高斯模糊，0.5=原樣通過（預設），1.0=USM 銳化。 | FLOAT | 否 | 0.0 至 1.0 (step 0.01) |
| `upscaler_model.realism` | 將輸出推向照片寫實風格。保持為 0 以使用模型預設（預設：0.0）。 | FLOAT | 否 | 0.0 至 1.0 (step 0.01) |

### Starlight (Astra) Fast 輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | 目標輸出解析度。 | COMBO | 是（選取此模型時） | `"FullHD (1080p)"`<br>`"4K (2160p)"` |

### Starlight (Astra) Creative 輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | 目標輸出解析度。 | COMBO | 是（選取此模型時） | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `upscaler_model.creativity` | 放大效果的創意強度（預設：`"low"`）。 | COMBO | 否 | `"low"`<br>`"middle"`<br>`"high"` |

### Starlight Precise 2.5 輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | 目標輸出解析度。 | COMBO | 是（選取此模型時） | `"FullHD (1080p)"`<br>`"4K (2160p)"` |

### apo-8 輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `interpolation_model.interpolation_frame_rate` | 輸出幀率（預設：60）。 | INT | 是（選取「apo-8」時） | 15 至 240 |
| `interpolation_model.interpolation_slowmo` | 套用至輸入影片的慢動作倍率。例如，2 會使輸出速度變為原本的一半，且持續時間變為兩倍（預設：1）。 | INT | 否 | 1 至 16 |
| `interpolation_model.interpolation_duplicate` | 分析輸入中的重複幀並加以移除（預設：False）。 | BOOLEAN | 否 | True<br>False |
| `interpolation_model.interpolation_duplicate_threshold` | 重複幀的偵測敏感度（預設：0.01）。 | FLOAT | 否 | 0.001 至 0.1 (step 0.001) |

**重要限制：**

- `upscaler_model` 與 `interpolation_model` 至少必須啟用其中一個。如果兩者都設為 `"Disabled"`，節點會因為沒有可處理的內容而引發錯誤。
- 輸入的 `video` 必須為 MP4 容器格式。
- `"Astra 2"` 模型限制為 9000 個輸入幀。設定 `prompt` 時，限制為 450 個輸入幀（在 30 fps 下約 15 秒）。如果影片超過適用限制，節點會引發錯誤。
- 只要選取了 `"Disabled"` 以外的放大模型，就必須提供 `upscaler_model.upscaler_resolution`。`"FullHD (1080p)"` 以 1080p 結果為目標，`"4K (2160p)"` 以 2160p 結果為目標；實際輸出寬高會根據輸入長寬比計算，分別限制在最大長邊 1920 或 3840 像素，並四捨五入至偶數。
- 當 `interpolation_model` 為 `"apo-8"` 時，`interpolation_model.interpolation_frame_rate` 為必填。
- 目前不支援非常大的檔案；上傳僅限單一部分，否則節點會引發錯誤。
- 部分參數（`sharp`、`realism`、`interpolation_slowmo`、`interpolation_duplicate`、`interpolation_duplicate_threshold`）在 UI 中標記為進階，且預設可能隱藏。

## 輸出

| 輸出名 | 說明 | 資料型別 |
| --- | --- | --- |
| `video` | 套用所選放大及/或幀插值濾鏡後的增強影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhanceV2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `14627dc772a6a46a645517bd34b545e0986a84561e24bdfe810b67f791ee47e3`
