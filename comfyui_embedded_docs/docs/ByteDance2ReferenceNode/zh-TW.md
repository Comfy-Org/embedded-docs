# ByteDance Seedance 2.5 參考轉影片（舊版）

此節點使用 ByteDance 的 Seedance 2.5 或 Seedance 2.0 AI 模型來生成、編輯或延長影片。您可以在文字提示中描述影片，並附加參考圖片、影片和音訊來引導結果，支援多模態參考、影片編輯和影片延長。這是 Seedance 參考轉影片節點的舊版、已棄用版本。

## 輸入

選擇 `model` 會決定下方哪些參數可用。`video_editing` 和 `output_format` 僅在選取 Seedance 2.5 時顯示。可增長的參考槽位和參考影片自動調整大小選項為所有模型共享，並在「參考輸入」中說明。

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 用於生成影片的 AI 模型。Seedance 2.5 為最新模型，支援最長 30 秒的影片與 mp4/mov 輸出；Seedance 2.0 可提供最高畫質與 4k；Fast 針對速度進行最佳化；Mini 可實現最快、成本最低的生成。選取模型後會顯示下方列出的模型專屬輸入。 | DYNAMIC_COMBO | 是 | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `種子` | 種子控制節點是否應重新執行；無論種子為何，結果都是非確定性的（預設值：0）。 | INT | 是 | 0 到 2147483647<br>步長：1 |
| `浮水印` | 是否要在影片中加入浮水印（預設值：False）。進階設定。 | BOOLEAN | 是 | `True`<br>`False` |

### Seedance 2.5 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。將台詞放在雙引號中，以引導生成的對話。必須包含至少一個非空白字元（預設值：空）。 | STRING | 是 | 任意文字 |
| `resolution` | 輸出影片的解析度（預設值：`"720p"`）。 | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `ratio` | 輸出影片的長寬比（預設值：`"16:9"`）。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的持續時間（秒）（預設值：5）。 | INT | 是 | 4 到 30<br>步長：1 |
| `generate_audio` | 啟用輸出影片的音訊生成（預設值：True）。 | BOOLEAN | 是 | `True`<br>`False` |
| `video_editing` | 當提示要編輯已連接的參考影片時啟用，例如替換其中的物件。輸出會保留來源片段的自身長度和長寬比，且會忽略 `duration` 和 `ratio` 小工具。保持停用可生成新影片，或將影片延長至您設定的持續時間（預設值：False）。 | BOOLEAN | 是 | `True`<br>`False` |
| `output_format` | 輸出影片的容器格式（預設值：`"mp4"`）。 | COMBO | 是 | `"mp4"` |

### Seedance 2.0 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。必須包含至少一個非空白字元（預設值：空）。 | STRING | 是 | 任意文字 |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | 輸出影片的長寬比（預設值：`"adaptive"`）。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的持續時間（秒）（預設值：7）。 | INT | 是 | 4 到 15<br>步長：1 |
| `generate_audio` | 啟用輸出影片的音訊生成（預設值：True）。 | BOOLEAN | 是 | `True`<br>`False` |

### Seedance 2.0 Fast 與 Seedance 2.0 Mini 輸入

由 Seedance 2.0 Fast 和 Seedance 2.0 Mini 共享。這兩個模型公開與 Seedance 2.0 相同的輸入集，差別在於 `resolution` 僅限於 480p 和 720p。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。必須包含至少一個非空白字元（預設值：空）。 | STRING | 是 | 任意文字 |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | `"480p"`<br>`"720p"` |
| `ratio` | 輸出影片的長寬比（預設值：`"adaptive"`）。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的持續時間（秒）（預設值：7）。 | INT | 是 | 4 到 15<br>步長：1 |
| `generate_audio` | 啟用輸出影片的音訊生成（預設值：True）。 | BOOLEAN | 是 | `True`<br>`False` |

### 參考輸入

所有模型皆可使用。最大槽位數量取決於所選模型：Seedance 2.5 支援的參考數量比 Seedance 2.0 模型更多。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | 可增長的槽位：連接一個或多個參考圖片（`image_1`、`image_2`、...），以引導影片生成。圖片會自動縮小至最大邊 6000 像素，且必須至少為 300x300 像素，長寬比介於 0.4 和 2.5 之間。 | IMAGE | 否 | 最多 30 個（Seedance 2.5）<br>最多 9 個（Seedance 2.0 模型） |
| `reference_videos` | 可增長的槽位：連接一個或多個參考影片（`video_1`、`video_2`、...），以引導影片生成；用於影片編輯和延長。 | VIDEO | 否 | 最多 10 個（Seedance 2.5）<br>最多 3 個（Seedance 2.0 模型） |
| `reference_audios` | 可增長的槽位：連接一個或多個參考音訊片段（`audio_1`、`audio_2`、...），以引導影片生成。 | AUDIO | 否 | 最多 10 個（Seedance 2.5）<br>最多 3 個（Seedance 2.0 模型） |
| `auto_downscale` | 自動縮小超過所選解析度下模型像素預算的參考影片。長寬比會保持不變；已在限制範圍內的影片不會被修改（預設值：True）。 | BOOLEAN | 否 | `True`<br>`False` |
| `auto_upscale` | 進階設定。自動放大低於所選解析度下模型最小像素數的參考影片。長寬比會保持不變；已達到最小值的影片不會被修改。注意：放大低解析度來源不會增加真實細節，且可能產生品質較低的生成結果（預設值：False）。 | BOOLEAN | 否 | `True`<br>`False` |
| `reference_assets` | 可增長的槽位：先前建立的 Seedance 虛擬庫素材（Image、Video 或 Audio）ID，用於作為參考（`asset_1`、`asset_2`、...）。每個素材都必須存在且狀態為 Active。在提示中，素材可表示為 `asset1`、`asset 1` 等；節點會將這些標記替換為諸如 "Image 2" 的標籤。 | STRING | 否 | 最多 30 個（Seedance 2.5）<br>最多 9 個（Seedance 2.0 模型） |

**重要限制：**

* 至少需要一個參考。對於 Seedance 2.0、2.0 Fast 和 2.0 Mini，您必須提供至少一個圖片或影片參考（透過 `reference_images`、`reference_videos`，或 `reference_assets` 中的圖片或影片項目）。Seedance 2.5 另外接受僅音訊參考（透過 `reference_audios` 或音訊 `reference_assets` 項目）。
* 參考數量取決於模型，並會合併直接輸入與素材參考進行驗證：Seedance 2.5 最多允許 30 個 `reference_images`、10 個 `reference_videos`、10 個 `reference_audios` 和 30 個 `reference_assets`；Seedance 2.0 模型最多允許 9 個圖片、3 個影片、3 個音訊片段和 9 個素材。
* 每個參考影片必須至少長 1.8 秒，且每個參考音訊片段必須至少長 1.8 秒。所有參考影片和所有參考音訊的總持續時間必須保持在所選模型的限制內（Seedance 2.0 模型為 15.1 秒）。
* 參考影片也必須符合所選解析度下模型的像素數限制。啟用 `auto_downscale`（預設）時，過大的影片會自動調整大小；啟用 `auto_upscale` 時，過小的影片會放大。如果停用任一自動調整，超出對應限制的影片會引發錯誤。
* 在 Seedance 2.5 上啟用 `video_editing` 時，會忽略 `duration` 和 `ratio` 輸入；輸出會符合參考影片本身的長度和長寬比。如果供應商將提示解讀為編輯參考影片，除非啟用 `video_editing` 或改寫提示以描述新影片，否則生成會失敗。
* 如果供應商拒絕為影片生成的音軌（例如可能與版權內容相符），任務會失敗；停用 `generate_audio` 會產生無聲影片。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4a1b62f65ff3515cdb749c9b3916e631e53523fe144e8cdf71ca020825196ae6`
