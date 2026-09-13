# ByteDance Seedance 2.5 參考轉影片

ByteDance Seedance 2.5 Reference to Video 會使用 ByteDance Seedance 模型（Seedance 2.5、2.0、2.0 Fast 和 2.0 Mini），在文字提示與可選參考圖像、影片、音訊或先前上傳的素材庫資產引導下，生成、編輯或延伸影片。它會上傳參考資料、提交生成任務、等待完成，並傳回完成的影片檔案。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 模型選擇器。Seedance 2.5 為最新模型，支援最長 30 秒的影片與 mp4/mov 輸出；Seedance 2.0 可達到最高品質與 4k；Fast 針對速度最佳化；Mini 則提供最快速、成本最低的生成。選擇模型會變更下方顯示的輸入小工具。 | DYNAMIC_COMBO | 是 | "Seedance 2.5"<br>"Seedance 2.0"<br>"Seedance 2.0 Fast"<br>"Seedance 2.0 Mini" |
| `種子` | `seed` 控制節點是否應重新執行；無論 `seed` 為何，結果都是非確定性的。預設：0。 | INT | 是 | 0 至 2147483647 |
| `浮水印` | 是否在影片中加入浮水印。預設：False。進階設定。 | BOOLEAN | 是 | true<br>false |

### Seedance 2.5 輸入

當 `model` 設為 "Seedance 2.5" 時，會顯示這些輸入。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。將台詞放在雙引號中，以引導生成的對話。預設：空字串。 | STRING | 是 | 多行文字 |
| `resolution` | 輸出影片的解析度。預設：720p。 | COMBO | 是 | "480p"<br>"720p"<br>"1080p" |
| `ratio` | 輸出影片的長寬比。預設：16:9。 | COMBO | 是 | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | 輸出影片的長度，以秒為單位（4-30）。預設：5。 | INT | 是 | 4 至 30 |
| `generate_audio` | 啟用輸出影片的音訊生成。預設：True。 | BOOLEAN | 是 | true<br>false |
| `task_type` | 要對參考媒體執行什麼操作。除了 auto 以外的每個值都會在提交任務時驗證，因此不相符的設定會在生成開始前失敗。<br>auto：模型會根據提示與輸入推斷任務，而與其解讀衝突的設定只會在生成開始後才失敗。<br>reference：在參考圖像、影片與音訊的引導下生成新影片。<br>edit：變更已連接的參考影片（新增、移除、取代）；輸出會保留來源片段本身的長度與長寬比，且會忽略 `duration` 與 `ratio` 小工具。<br>extend：將已連接的參考影片向前或向後延伸；提示應說明「extend forward」、「extend backward」或「continue」，長寬比會遵循來源片段，且輸出只包含你所設定長度的新生成片段，不包含來源片段。預設：auto。 | COMBO | 是 | "auto"<br>"reference"<br>"edit"<br>"extend" |
| `output_format` | 輸出影片的容器格式。預設：mp4。 | COMBO | 是 | "mp4" |

### Seedance 2.0 輸入

當 `model` 設為 "Seedance 2.0" 時，會顯示這些輸入。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。預設：空字串。 | STRING | 是 | 多行文字 |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | "480p"<br>"720p"<br>"1080p"<br>"4k" |
| `ratio` | 輸出影片的長寬比。預設：adaptive。 | COMBO | 是 | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | 輸出影片的長度，以秒為單位（4-15）。預設：7。 | INT | 是 | 4 至 15 |
| `generate_audio` | 啟用輸出影片的音訊生成。預設：True。 | BOOLEAN | 是 | true<br>false |

### Seedance 2.0 Fast 與 Seedance 2.0 Mini 輸入

當 `model` 設為 "Seedance 2.0 Fast" 或 "Seedance 2.0 Mini" 時，會顯示這些輸入。兩個模型共用相同的輸入集。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。預設：空字串。 | STRING | 是 | 多行文字 |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | "480p"<br>"720p" |
| `ratio` | 輸出影片的長寬比。預設：adaptive。 | COMBO | 是 | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | 輸出影片的長度，以秒為單位（4-15）。預設：7。 | INT | 是 | 4 至 15 |
| `generate_audio` | 啟用輸出影片的音訊生成。預設：True。 | BOOLEAN | 是 | true<br>false |

### 參考輸入

這些可擴充的參考插槽適用於所有模型。每個模型的最大插槽數不同：Seedance 2.5 支援最多 30 個圖像、10 個影片、10 個音訊與 30 個資產；Seedance 2.0、2.0 Fast 與 2.0 Mini 支援最多 9 個圖像、3 個影片、3 個音訊與 9 個資產。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | 可擴充插槽：連接 1..N 個可引導輸出的參考圖像。數量限制依模型而定（請參閱各模型章節）。圖像會驗證長寬比（0.4 至 2.5），並自動縮小至最大邊 6000 像素。 | IMAGE | 否 | 1..9 個插槽（Seedance 2.0 系列）<br>1..30 個插槽（Seedance 2.5） |
| `reference_videos` | 可擴充插槽：連接 1..N 個參考影片。數量限制依模型而定（請參閱各模型章節）。每段影片長度必須至少 1.8 秒，且必須符合所選模型與解析度的像素限制。 | VIDEO | 否 | 1..3 個插槽（Seedance 2.0 系列）<br>1..10 個插槽（Seedance 2.5） |
| `reference_audios` | 可擴充插槽：連接 1..N 個參考音軌。數量限制依模型而定（請參閱各模型章節）。每個音訊長度必須至少 1.8 秒。 | AUDIO | 否 | 1..3 個插槽（Seedance 2.0 系列）<br>1..10 個插槽（Seedance 2.5） |
| `reference_assets` | 可擴充插槽：連接 1..N 個資產 ID 字串，用於已上傳至 Seedance 虛擬素材庫的媒體。每個資產必須為 Active 狀態。你可以在提示中使用 `asset1` 或 `asset 1` 等符記來參照資產；節點會將它們取代為資產的位置標籤（例如 "Image 2" 或 "Video 1"）。 | STRING | 否 | 1..9 個插槽（Seedance 2.0 系列）<br>1..30 個插槽（Seedance 2.5） |
| `auto_downscale` | 自動縮小超過所選解析度之模型像素預算的參考影片。長寬比會保留；已在限制內的影片不會被變更。預設：True。 | BOOLEAN | 否 | true<br>false |
| `auto_upscale` | 自動放大低於所選解析度之模型最小像素數的參考影片。長寬比會保留；已達到最低要求的影片不會被變更。注意：放大低解析度來源不會增加真實細節，且可能產生品質較低的生成結果。預設：False。進階設定。 | BOOLEAN | 否 | true<br>false |

**注意：** 執行此節點至少需要一個參考圖像、影片或資產（Seedance 2.5 也接受僅有音訊的參考）。參考影片與音訊各自長度必須至少 1.8 秒，且所有參考影片的總時長（以及所有參考音訊的總時長，需分開計算）不得超過所選模型的最大總秒數。參考圖像的長寬比必須大約介於 2:5 與 5:2 之間（0.4 至 2.5），至少為 300x300 像素，並會自動縮小至最大邊 6000 像素。`task_type` 的 "edit" 與 "extend" 選項僅適用於 Seedance 2.5，且兩者都需要至少一個參考影片；使用 "edit" 時，輸出會保留來源片段本身的長度與長寬比，且會忽略 `duration` 與 `ratio` 小工具；使用 "extend" 時，輸出只包含你所設定長度的新生成片段。參照的資產必須處於 Active 狀態，否則任務會失敗。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 生成的影片，會在生成任務完成後從供應商下載。啟用音訊生成時會包含音訊。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNodeV2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3a6bba12e719204ba5dba9d7d5f2b4c5285ed68974ee015b6e4a7892a1cf0933`
