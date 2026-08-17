# ByteDance Seedance 2.0 參考轉影片

此節點使用 ByteDance 的 Seedance 2.5 或 2.0 AI 模型來生成、編輯或延伸影片。您可以在文字提示中描述影片，並可加入參考圖片、影片和音訊來引導結果。它支援多模態參考輸入、影片編輯和影片延伸。這是 ByteDance Seedance 2.5 Reference to Video 節點的舊版、已棄用版本。

## 輸入

選擇 `model` 會決定下列哪些參數可用。`video_editing` 和 `output_format` 僅在選取 Seedance 2.5 時顯示。可增長的參考插槽（growable reference slots）及參考影片自動調整大小選項為所有模型共用，並於「參考輸入」中說明。

### 通用輸入

| 參數 | 說明 | 資料類型 | 必要 | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於生成影片的 AI 模型。Seedance 2.5 為最新模型，支援最長 30 秒影片與 mp4/mov 輸出；Seedance 2.0 提供最高品質與 1080p/4k；Fast 為速度最佳化；Mini 為最快且成本最低的生成。選取模型後會顯示下方所列的該模型專用輸入。 | DYNAMIC_COMBO | 是 | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | `seed` 控制節點是否應重新執行；無論種子值為何，結果皆非確定性（預設值：0）。 | INT | 是 | 0 至 2147483647<br>Step: 1 |
| `watermark` | 是否在影片中加入浮水印（預設值：False）。 | BOOLEAN | 是 | `True`<br>`False` |

### Seedance 2.5 輸入

| 參數 | 說明 | 資料類型 | 必要 | Range |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 影片生成的文字提示。將口白台詞放在雙引號中，以引導生成對話。必須至少包含一個非空白字元（預設值：空白）。 | STRING | 是 | Any text |
| `resolution` | 輸出影片的解析度（預設值：`"720p"`）。 | COMBO | 是 | `"480p"`<br>`"720p"` |
| `ratio` | 輸出影片的長寬比（預設值：`"16:9"`）。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的持續時間（秒）（預設值：5）。 | INT | 是 | 4 至 30<br>Step: 1 |
| `generate_audio` | 為輸出影片啟用音訊生成（預設值：True）。 | BOOLEAN | 是 | `True`<br>`False` |
| `video_editing` | 當提示要編輯已連接的參考影片時啟用，例如替換其中的物件。啟用後，輸出將保留來源片段自身的長度與長寬比，並忽略 `duration` 和 `ratio` 控制項。保持停用以生成新影片，或將影片延伸到您設定的長度（預設值：False）。 | BOOLEAN | 是 | `True`<br>`False` |
| `output_format` | 輸出影片的容器格式（預設值：`"mp4"`）。 | COMBO | 是 | `"mp4"` |

### Seedance 2.0 輸入

| 參數 | 說明 | 資料類型 | 必要 | Range |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 影片生成的文字提示。必須至少包含一個非空白字元（預設值：空白）。 | STRING | 是 | Any text |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | 輸出影片的長寬比（預設值：`"adaptive"`）。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的持續時間（秒）（預設值：7）。 | INT | 是 | 4 至 15<br>Step: 1 |
| `generate_audio` | 為輸出影片啟用音訊生成（預設值：True）。 | BOOLEAN | 是 | `True`<br>`False` |

### Seedance 2.0 Fast 與 Seedance 2.0 Mini 輸入

由 Seedance 2.0 Fast 與 Seedance 2.0 Mini 共用。這兩個模型暴露與 Seedance 2.0 相同的輸入集合，但 `resolution` 僅限 480p 與 720p。

| 參數 | 說明 | 資料類型 | 必要 | Range |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 影片生成的文字提示。必須至少包含一個非空白字元（預設值：空白）。 | STRING | 是 | Any text |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | `"480p"`<br>`"720p"` |
| `ratio` | 輸出影片的長寬比（預設值：`"adaptive"`）。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的持續時間（秒）（預設值：7）。 | INT | 是 | 4 至 15<br>Step: 1 |
| `generate_audio` | 為輸出影片啟用音訊生成（預設值：True）。 | BOOLEAN | 是 | `True`<br>`False` |

### 參考輸入

適用於所有模型。插槽的最大數量取決於所選模型：Seedance 2.5 支援比 Seedance 2.0 系列更多的參考。

| 參數 | 說明 | 資料類型 | 必要 | Range |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | 可增長插槽：連接一張或多張參考圖片（`image_1`、`image_2`、...）以引導影片生成。數量限制依模型而定（參見模型章節）。圖片會自動縮小至最長邊不超過 6000 像素，且必須至少為 300x300 像素，長寬比介於 0.4 至 2.5 之間。 | IMAGE | 否 | 最多 30（Seedance 2.5）<br>最多 9（Seedance 2.0 系列） |
| `reference_videos` | 可增長插槽：連接一部或多部參考影片（`video_1`、`video_2`、...）以引導影片生成；用於影片編輯與延伸。 | VIDEO | 否 | 最多 10（Seedance 2.5）<br>最多 3（Seedance 2.0 系列） |
| `reference_audios` | 可增長插槽：連接一個或多個參考音訊片段（`audio_1`、`audio_2`、...）以引導影片生成。 | AUDIO | 否 | 最多 10（Seedance 2.5）<br>最多 3（Seedance 2.0 系列） |
| `auto_downscale` | 自動縮小超出所選解析度之模型像素上限的參考影片。保留長寬比；已在限制內的影片不會被變動（預設值：True）。 | BOOLEAN | 否 | `True`<br>`False` |
| `auto_upscale` | 自動放大低於所選解析度之模型像素下限的參考影片。保留長寬比；已符合下限的影片不會被變動。注意：放大低解析度來源不會增加真實細節，且可能產生較低品質的生成結果（預設值：False）。 | BOOLEAN | 否 | `True`<br>`False` |
| `reference_assets` | 可增長插槽：先前建立的 Seedance 虛擬庫資產（Image、Video 或 Audio）ID，作為參考使用（`asset_1`、`asset_2`、...）。每個資產必須存在且狀態為 Active。在提示中，資產可寫為 `asset1`、`asset 1` 等；節點會將這些標記替換為如「Image 2」的標籤。 | STRING | 否 | 最多 30（Seedance 2.5）<br>最多 9（Seedance 2.0 系列） |

**重要限制：**

* 至少需要一個參考。對於 Seedance 2.0、2.0 Fast 和 2.0 Mini，您必須提供至少一個圖片或影片參考（透過 `reference_images`、`reference_videos`，或 `reference_assets` 中的圖片或影片條目）。Seedance 2.5 另外接受僅音訊參考（透過 `reference_audios` 或音訊 `reference_assets` 條目）。
* 參考數量依模型而定，並會合併驗證直接輸入與資產參考：Seedance 2.5 最多允許 30 個 `reference_images`、10 個 `reference_videos`、10 個 `reference_audios` 和 30 個 `reference_assets`；Seedance 2.0 系列最多允許 9 個圖片、3 個影片、3 個音訊片段和 9 個資產。
* 每個參考影片必須至少 1.8 秒長，每個參考音訊片段也必須至少 1.8 秒長。所有參考影片與所有參考音訊的總持續時間必須保持在所選模型的限制內（Seedance 2.0 系列為 15.1 秒）。
* 參考影片也必須符合所選解析度下的模型像素數量限制。啟用 `auto_downscale`（預設）時，過大的影片會自動調整大小；啟用 `auto_upscale` 時，過小的影片會被放大。若停用任一自動調整，超出對應限制的影片將引發錯誤。
* 當 Seedance 2.5 啟用 `video_editing` 時，`duration` 和 `ratio` 輸入會被忽略；輸出將符合參考影片自身的長度與長寬比。若提供者將提示解讀為編輯參考影片，除非啟用 `video_editing`，或改寫提示以描述新影片，否則生成將失敗。
* 若提供者拒絕為影片生成的音軌（例如可能的版權相符），任務將失敗；停用 `generate_audio` 會產生無聲影片。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4a1b62f65ff3515cdb749c9b3916e631e53523fe144e8cdf71ca020825196ae6`
