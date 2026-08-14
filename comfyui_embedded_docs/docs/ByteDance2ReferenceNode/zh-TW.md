# ByteDance Seedance 2.0 參考轉影片

此節點使用 ByteDance 的 Seedance 2.5 或 2.0 AI 模型來生成、編輯或延伸影片。您可以透過文字提示來描述影片，並可新增參考圖片、影片和音訊以引導結果。它支援多模態參考輸入、影片編輯和影片延伸。

## 輸入

選擇 `model` 會決定下列哪些參數可用。`video_editing` 和 `output_format` 僅在選取 Seedance 2.5 時出現。可擴充的參考輸入槽位與參考影片自動調整大小選項由所有模型共用，並在「參考輸入」中說明。

### 通用輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於生成影片的 AI 模型。Seedance 2.5 為最新模型，影片可達 30 秒，並支援 mp4/mov 輸出；Seedance 2.0 提供最高品質與 1080p/4k；Fast 為速度最佳化；Mini 為最快且成本最低的生成。選取模型後，會顯示下列該模型專屬的輸入。 | COMBO | 是 | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | 種子值控制節點是否應重新執行；無論種子為何，結果都是非確定性的（預設：0）。 | INT | 是 | 0 至 2147483647 |
| `watermark` | 是否在影片中加入浮水印（預設：False）。 | BOOLEAN | 是 | `True`<br>`False` |

### Seedance 2.5 輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。將口說台詞放在雙引號中，以引導生成的對話。必須包含至少一個非空白字元（預設：空字串）。 | STRING | 是 | 任意文字 |
| `resolution` | 輸出影片的解析度（預設：`"720p"`）。 | COMBO | 是 | `"480p"`<br>`"720p"` |
| `ratio` | 輸出影片的長寬比（預設：`"16:9"`）。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的持續時間（秒）（預設：5）。 | INT | 是 | 4 至 30<br>步長：1 |
| `generate_audio` | 為輸出影片啟用音訊生成（預設：True）。 | BOOLEAN | 是 | `True`<br>`False` |
| `video_editing` | 當提示詞要編輯已連接的參考影片時啟用，例如替換其中的物件。啟用後，輸出會保留來源片段本身的長度與長寬比，`duration` 和 `ratio` 控制項會被忽略。保持停用則可生成新影片，或將影片延伸至您設定的持續時間（預設：False）。 | BOOLEAN | 是 | `True`<br>`False` |
| `output_format` | 輸出影片的容器格式（預設：`"mp4"`）。 | COMBO | 是 | `"mp4"` |

### Seedance 2.0 輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。必須包含至少一個非空白字元（預設：空字串）。 | STRING | 是 | 任意文字 |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | 輸出影片的長寬比（預設：`"adaptive"`）。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的持續時間（秒）（預設：7）。 | INT | 是 | 4 至 15<br>步長：1 |
| `generate_audio` | 為輸出影片啟用音訊生成（預設：True）。 | BOOLEAN | 是 | `True`<br>`False` |

### Seedance 2.0 Fast 與 Seedance 2.0 Mini 輸入

由 Seedance 2.0 Fast 與 Seedance 2.0 Mini 共用。這兩個模型提供與 Seedance 2.0 相同的輸入集合，但 `resolution` 僅限於 480p 和 720p。

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。必須包含至少一個非空白字元（預設：空字串）。 | STRING | 是 | 任意文字 |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | `"480p"`<br>`"720p"` |
| `ratio` | 輸出影片的長寬比（預設：`"adaptive"`）。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的持續時間（秒）（預設：7）。 | INT | 是 | 4 至 15<br>步長：1 |
| `generate_audio` | 為輸出影片啟用音訊生成（預設：True）。 | BOOLEAN | 是 | `True`<br>`False` |

### 參考輸入

適用於所有模型。可用的槽位數量上限取決於所選模型：Seedance 2.5 支援的參考數量多於 Seedance 2.0 系列模型。

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | 可擴充的輸入槽位：連接一個或多個參考圖片（`image_1`、`image_2`、...）來引導影片生成。圖片會自動縮小至最大邊長 6000 像素，且必須至少為 300x300 像素，長寬比介於 0.4 至 2.5 之間。 | IMAGE | 否 | Up 至 30 (Seedance 2.5)<br>Up 至 9 (Seedance 2.0 models) |
| `reference_videos` | 可擴充的輸入槽位：連接一個或多個參考影片（`video_1`、`video_2`、...）來引導影片生成；用於影片編輯與延伸。 | VIDEO | 否 | Up 至 10 (Seedance 2.5)<br>Up 至 3 (Seedance 2.0 models) |
| `reference_audios` | 可擴充的輸入槽位：連接一個或多個參考音訊片段（`audio_1`、`audio_2`、...）來引導影片生成。 | AUDIO | 否 | Up 至 10 (Seedance 2.5)<br>Up 至 3 (Seedance 2.0 models) |
| `auto_downscale` | 自動縮小超出所選解析度之模型像素預算的參考影片。會保留長寬比；已在限制內的影片不會被變更（預設：True）。 | BOOLEAN | 否 | `True`<br>`False` |
| `auto_upscale` | 自動放大低於所選解析度之模型最低像素數量的參考影片。會保留長寬比；已達到最低要求的影片不會被變更。注意：放大低解析度來源並不會增加真實細節，且可能產生品質較低的生成結果（預設：False）。 | BOOLEAN | 否 | `True`<br>`False` |
| `reference_assets` | 可擴充的輸入槽位：先前建立的 Seedance 虛擬資源庫資產（Image、Video 或 Audio）ID，作為參考使用（`asset_1`、`asset_2`、...）。每個資產都必須存在且狀態為 Active。在提示中，資產可被參照為 `asset1`、`asset 1` 等；節點會將這些標記替換為「Image 2」等標籤。 | STRING | 否 | Up 至 30 (Seedance 2.5)<br>Up 至 9 (Seedance 2.0 models) |

**重要限制：**

* 至少需要一個參考。對於 Seedance 2.0、2.0 Fast 和 2.0 Mini，您必須提供至少一個圖片或影片參考（透過 `reference_images`、`reference_videos`，或 `reference_assets` 中的圖片或影片項目）。Seedance 2.5 額外接受僅含音訊的參考（透過 `reference_audios`，或 `reference_assets` 中的音訊項目）。
* 參考數量依模型而定，並會將直接輸入與資產參考合併驗證：Seedance 2.5 允許最多 30 個 `reference_images`、10 個 `reference_videos`、10 個 `reference_audios` 和 30 個 `reference_assets`；Seedance 2.0 系列模型最多允許 9 個圖片、3 個影片、3 個音訊片段和 9 個資產。
* 每個參考影片長度至少需 1.8 秒，每個參考音訊片段也至少需 1.8 秒。所有參考影片與所有參考音訊的總持續時間必須維持在所選模型的限制內（Seedance 2.0 系列模型為 15.1 秒）。
* 參考影片也必須符合所選解析度下模型的像素數量限制。啟用 `auto_downscale`（預設）時，過大的影片會自動調整大小；啟用 `auto_upscale` 時，過小的影片會被放大。若停用任一自動調整功能，超出對應限制的影片會產生錯誤。
* 在 Seedance 2.5 上啟用 `video_editing` 時，`duration` 和 `ratio` 輸入會被忽略；輸出會符合參考影片自身的長度與長寬比。若提供者將提示詞解讀為編輯參考影片，除非啟用 `video_editing`，或重新措辭提示詞以描述新影片，否則生成會失敗。
* 若提供者拒絕為影片生成的音軌（例如可能的版權相符），任務將失敗；停用 `generate_audio` 會產生無聲影片。

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
|-------------|-------------|-----------|
| `video` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4429306ac40b0f04ce7176cd805b34164de5e4e2b7204b008ea076b57663c200`
