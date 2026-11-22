# ByteDance Seedance 2.5 參考轉影片（舊版）

此節點使用 ByteDance 的 Seedance 2.5 或 Seedance 2.0 AI 模型來生成、編輯或延長影片。您可透過文字提示描述影片，並附加參考圖片、影片和音訊來引導結果，支援多模態參考、影片編輯與影片延長。此為 Seedance 參考轉影片節點的舊版、已棄用版本。

## 輸入

選擇 `model` 會決定下方哪些參數可用。`video_editing` 與 `output_format` 僅在選取 Seedance 2.5 時出現。可擴充的參考槽位與參考影片自動調整大小選項為所有模型共用，並於參考輸入一節說明。

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 用於生成影片的 AI 模型。Seedance 2.5 為最新模型，支援最長 30 秒的影片、4k 與 mp4/mov 輸出；Seedance 2.0 提供最高品質與 4k；Fast 用於速度最佳化；Mini 用於最快、成本最低的生成。選擇模型後會顯示下方列出的模型專屬輸入。 | DYNAMIC_COMBO | 是 | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `種子` | `seed` 控制節點是否應重新執行；無論 `seed` 為何，結果都是非確定性的（預設：0）。 | INT | 是 | 0 至 2147483647<br>步進值：1 |
| `浮水印` | 是否在影片中加入浮水印（預設：False）。進階設定。 | BOOLEAN | 是 | `True`<br>`False` |

### Seedance 2.5 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。將台詞放在雙引號內，以引導生成的對話。必須包含至少一個非空白字元（預設：空）。 | STRING | 是 | 任意文字 |
| `resolution` | 輸出影片的解析度（預設：`"720p"`）。 | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | 輸出影片的長寬比（預設：`"16:9"`）。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的時長，以秒為單位（預設：5）。 | INT | 是 | 4 至 30<br>步進值：1 |
| `generate_audio` | 啟用輸出影片的音訊生成（預設：True）。 | BOOLEAN | 是 | `True`<br>`False` |
| `video_editing` | 當提示要編輯已連接的參考影片時啟用，例如替換其中的物件。此時輸出會保留來源片段本身的長度與長寬比，且會忽略 `duration` 與 `ratio` 元件。保持停用以生成新影片，或將影片延長至您設定的時長（預設：False）。 | BOOLEAN | 是 | `True`<br>`False` |
| `output_format` | 輸出影片的容器格式（預設：`"mp4"`）。 | COMBO | 是 | `"mp4"` |

### Seedance 2.0 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。必須包含至少一個非空白字元（預設：空）。 | STRING | 是 | 任意文字 |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | 輸出影片的長寬比（預設：`"adaptive"`）。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的時長，以秒為單位（預設：7）。 | INT | 是 | 4 至 15<br>步進值：1 |
| `generate_audio` | 啟用輸出影片的音訊生成（預設：True）。 | BOOLEAN | 是 | `True`<br>`False` |

### Seedance 2.0 Fast 與 Seedance 2.0 Mini 輸入

由 Seedance 2.0 Fast 與 Seedance 2.0 Mini 共用。這兩個模型公開的輸入集與 Seedance 2.0 相同，差別在於 `resolution` 僅限於 480p 與 720p。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。必須包含至少一個非空白字元（預設：空）。 | STRING | 是 | 任意文字 |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | `"480p"`<br>`"720p"` |
| `ratio` | 輸出影片的長寬比（預設：`"adaptive"`）。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的時長，以秒為單位（預設：7）。 | INT | 是 | 4 至 15<br>步進值：1 |
| `generate_audio` | 啟用輸出影片的音訊生成（預設：True）。 | BOOLEAN | 是 | `True`<br>`False` |

### 參考輸入

適用於所有模型。最大槽位數量取決於所選模型：Seedance 2.5 支援的參考數量比 Seedance 2.0 模型更多。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | 可擴充槽位：連接一或多張參考圖片（`image_1`、`image_2`、...），用以引導影片生成。圖片會自動縮小至最大邊長 6000 像素，且必須至少為 300x300 像素，長寬比介於 0.4 與 2.5 之間。 | IMAGE | 否 | 最多 30 個（Seedance 2.5）<br>最多 9 個（Seedance 2.0 模型） |
| `reference_videos` | 可擴充槽位：連接一或多部參考影片（`video_1`、`video_2`、...），用以引導影片生成；用於影片編輯與延長。 | VIDEO | 否 | 最多 10 個（Seedance 2.5）<br>最多 3 個（Seedance 2.0 模型） |
| `reference_audios` | 可擴充槽位：連接一或多個參考音訊片段（`audio_1`、`audio_2`、...），用以引導影片生成。 | AUDIO | 否 | 最多 10 個（Seedance 2.5）<br>最多 3 個（Seedance 2.0 模型） |
| `auto_downscale` | 自動縮小超過模型在所選解析度下像素預算的參考影片。會保留長寬比；已在限制內的影片不會被變更（預設：True）。 | BOOLEAN | 否 | `True`<br>`False` |
| `auto_upscale` | 進階設定。自動放大低於模型在所選解析度下最低像素數量的參考影片。會保留長寬比；已達到最低要求的影片不會被變更。注意：放大低解析度來源不會增加真實細節，且可能產生品質較低的生成結果（預設：False）。 | BOOLEAN | 否 | `True`<br>`False` |
| `reference_assets` | 可擴充槽位：先前建立的 Seedance 虛擬庫資產（圖片、影片或音訊）ID，用作參考（`asset_1`、`asset_2`、...）。每個資產都必須存在且狀態為 Active。在提示中，資產可以 `asset1`、`asset 1` 等方式參照；節點會將這些標記替換為例如「Image 2」的標籤。 | STRING | 否 | 最多 30 個（Seedance 2.5）<br>最多 9 個（Seedance 2.0 模型） |

**重要限制：**

* 至少需要一個參考。對於 Seedance 2.0、2.0 Fast 與 2.0 Mini，您必須提供至少一個圖片或影片參考（透過 `reference_images`、`reference_videos`，或 `reference_assets` 中的圖片或影片項目）。Seedance 2.5 另外接受純音訊參考（透過 `reference_audios` 或音訊的 `reference_assets` 項目）。
* 參考數量取決於模型，並會針對直接輸入與資產參考合併後進行驗證：Seedance 2.5 最多允許 30 個 `reference_images`、10 個 `reference_videos`、10 個 `reference_audios` 與 30 個 `reference_assets`；Seedance 2.0 模型最多允許 9 張圖片、3 部影片、3 個音訊片段與 9 個資產。
* 每個參考影片必須至少長 1.8 秒，且每個參考音訊片段必須至少長 1.8 秒。所有參考影片與所有參考音訊的總時長必須維持在所選模型的限制內（Seedance 2.0 模型為 15.1 秒）。
* 參考影片也必須符合模型在所選解析度下的像素數量限制。啟用 `auto_downscale`（預設）時，過大的影片會自動調整大小；啟用 `auto_upscale` 時，過小的影片會放大。若停用任一自動調整，超出對應限制的影片將會引發錯誤。
* 在 Seedance 2.5 上啟用 `video_editing` 時，會忽略 `duration` 與 `ratio` 輸入；輸出會符合參考影片本身的長度與長寬比。若供應商將提示解讀為編輯參考影片，除非啟用 `video_editing` 或改寫提示以描述新影片，否則生成會失敗。
* 若供應商拒絕為影片生成的音軌（例如可能與版權相符），工作會失敗；停用 `generate_audio` 會產生無聲影片。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2c8ff29bb772b9ef005e264dd5c07b36f83b5b7068eebefa83ed567029187184`
