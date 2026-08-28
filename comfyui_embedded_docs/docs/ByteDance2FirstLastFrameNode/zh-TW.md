# ByteDance Seedance 2.0 首末幀轉影片

此節點使用 ByteDance Seedance 模型，從必填的首幀圖像和可選的末幀圖像生成影片。您透過文字提示來描述影片；首幀引導影片的開頭，末幀引導影片的結尾。它支援 Seedance 2.5 以及 Seedance 2.0 系列（Seedance 2.0、Seedance 2.0 Fast 和 Seedance 2.0 Mini）。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | Seedance 2.5 為最新模型，影片可達 30 秒並輸出 mp4/mov 格式；Seedance 2.0 提供最高品質和 4k；Fast 優化速度；Mini 提供最快、成本最低的生成。選擇模型會在下文顯示該模型的專屬輸入。 | DYNAMIC_COMBO | 是 | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `首幀圖像` | 影片的首幀圖像。 | IMAGE | 否 | - |
| `末幀圖像` | 影片的末幀圖像。 | IMAGE | 否 | - |
| `first_frame_asset_id` | 用作首幀的 Seedance asset_id。與 `first_frame` 圖像輸入互相排斥。預設為空字串。 | STRING | 否 | - |
| `last_frame_asset_id` | 用作末幀的 Seedance asset_id。與 `last_frame` 圖像輸入互相排斥。預設為空字串。 | STRING | 否 | - |
| `種子` | 種子控制節點是否應重新執行；無論種子為何，結果都是非確定性的。預設為 0。 | INT | 是 | 0 到 2147483647 |
| `浮水印` | 是否在影片中加入浮水印。預設為 False。 | BOOLEAN | 是 | False<br>True |

### Seedance 2.5 輸入

選擇 `Seedance 2.5` 時會顯示這些輸入。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 影片生成的文字提示。將台詞放在雙引號中以引導生成的對話。 | STRING | 是 | - |
| `resolution` | 輸出影片的解析度。預設為 720p。 | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `duration` | 輸出影片的持續時間（秒）（4-30）。預設為 5。 | INT | 是 | 4 到 30 |
| `generate_audio` | 為輸出影片啟用音訊生成。預設為 True。 | BOOLEAN | 是 | False<br>True |
| `output_format` | 輸出影片的容器格式。預設為 mp4。 | COMBO | 是 | `"mp4"` |

### Seedance 2.0 輸入

選擇 `Seedance 2.0` 時會顯示這些輸入。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 影片生成的文字提示。 | STRING | 是 | - |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | 輸出影片的長寬比。預設為 `adaptive`，即使用與輸入幀長寬比最接近的支援比例。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的持續時間（秒）（4-15）。預設為 7。 | INT | 是 | 4 到 15 |
| `generate_audio` | 為輸出影片啟用音訊生成。預設為 True。 | BOOLEAN | 是 | False<br>True |

### Seedance 2.0 Fast 和 Seedance 2.0 Mini 輸入

由 `Seedance 2.0 Fast` 和 `Seedance 2.0 Mini` 共用。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 影片生成的文字提示。 | STRING | 是 | - |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | `"480p"`<br>`"720p"` |
| `ratio` | 輸出影片的長寬比。預設為 `adaptive`，即使用與輸入幀長寬比最接近的支援比例。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的持續時間（秒）（4-15）。預設為 7。 | INT | 是 | 4 到 15 |
| `generate_audio` | 為輸出影片啟用音訊生成。預設為 True。 | BOOLEAN | 是 | False<br>True |

**參數約束**

- 您必須以 `first_frame` 圖像或 `first_frame_asset_id` 的形式提供首幀。同時提供兩者會引發錯誤；兩者都不提供也會引發錯誤。
- `last_frame` 和 `last_frame_asset_id` 輸入為選用，但您不能同時為同一幀提供兩者。
- Asset ID 必須引用現有且有效的 Seedance Image 資產。
- `prompt` 輸入為必填，且不能為空。
- 使用 `Seedance 2.5` 時，輸出長寬比始終為 adaptive，並遵循首幀自身的長寬比，因此不會顯示 `ratio` 輸入。
- 使用 Seedance 2.0 系列模型和本機幀圖像時，圖像在生成前會進行中心裁切並調整為目標輸出解析度和比例。當 `ratio` 為 `adaptive` 時，使用與輸入圖像最接近的支援比例。
- 本機幀圖像會驗證支援的長寬比和尺寸；過大的圖像會縮小。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `bc2eb5f43c935986ad870703cfbc92dd99a53d6f0ac91cf0cad46bee33ff2cc0`
