# ByteDance2ReferenceNodeV2

ByteDance Seedance 2.5 Reference to Video 使用 ByteDance Seedance 模型（Seedance 2.5、2.0、2.0 Fast 與 2.0 Mini），根據文字提示以及可選的參考圖片、影片、音訊或先前上傳的素材庫資產，來生成、編輯或延伸影片。此節點會上傳參考內容、提交生成任務、等待完成，然後回傳最終的影片檔案。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 模型選擇器。Seedance 2.5 為最新模型，影片最長 30 秒，輸出 mp4/mov；Seedance 2.0 提供最高品質與 4k；Fast 為速度最佳化；Mini 為最快且成本最低的生成。選擇模型會改變下方顯示的輸入元件。 | DYNAMIC_COMBO | 是 | "Seedance 2.5"<br>"Seedance 2.0"<br>"Seedance 2.0 Fast"<br>"Seedance 2.0 Mini" |
| `seed` | 種子控制節點是否應重新執行；無論種子為何，結果皆非確定性。預設值：0。 | INT | 是 | 0 至 2147483647 |
| `watermark` | 是否在影片中加入浮水印。預設值：False。進階設定。 | BOOLEAN | 是 | true<br>false |

### Seedance 2.5 輸入

當 `model` 設定為「Seedance 2.5」時，會顯示這些輸入。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。若要引導生成的對話，請將口語台詞放在雙引號中。預設值：空字串。 | STRING | 是 | 多行文字 |
| `resolution` | 輸出影片的解析度。預設值：720p。 | COMBO | 是 | "480p"<br>"720p"<br>"1080p" |
| `ratio` | 輸出影片的畫面比例。預設值：16:9。 | COMBO | 是 | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | 輸出影片的持續時間（秒）（4-30）。預設值：5。 | INT | 是 | 4 至 30 |
| `generate_audio` | 是否為輸出影片啟用音訊生成。預設值：True。 | BOOLEAN | 是 | true<br>false |
| `task_type` | 對參考媒體進行什麼操作。除了 auto 以外的每個值都會在提交任務時驗證，因此不匹配的設定會在生成開始前失敗。<br>auto：模型會從提示與輸入推斷任務，與其解讀衝突的設定只會在生成開始後才失敗。<br>reference：依據參考圖片、影片與音訊生成新的影片。<br>edit：變更已連接的參考影片（新增、移除、替換）；輸出會保留來源剪輯本身的長度與畫面比例，且 duration 與 ratio 元件會被忽略。<br>extend：向前或向後延伸已連接的參考影片；提示中應包含「extend forward」、「extend backward」或「continue」，畫面比例會跟隨來源剪輯，而輸出僅包含你設定的持續時間內新生成的片段，不包含來源剪輯。預設值：auto。 | COMBO | 是 | "auto"<br>"reference"<br>"edit"<br>"extend" |
| `output_format` | 輸出影片的容器格式。預設值：mp4。 | COMBO | 是 | "mp4" |

### Seedance 2.0 輸入

當 `model` 設定為「Seedance 2.0」時，會顯示這些輸入。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。預設值：空字串。 | STRING | 是 | 多行文字 |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | "480p"<br>"720p"<br>"1080p"<br>"4k" |
| `ratio` | 輸出影片的畫面比例。預設值：adaptive。 | COMBO | 是 | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | 輸出影片的持續時間（秒）（4-15）。預設值：7。 | INT | 是 | 4 至 15 |
| `generate_audio` | 是否為輸出影片啟用音訊生成。預設值：True。 | BOOLEAN | 是 | true<br>false |

### Seedance 2.0 Fast 與 Seedance 2.0 Mini 輸入

當 `model` 設定為「Seedance 2.0 Fast」或「Seedance 2.0 Mini」時，會顯示這些輸入。兩個模型共用相同的輸入集合。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。預設值：空字串。 | STRING | 是 | 多行文字 |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | "480p"<br>"720p" |
| `ratio` | 輸出影片的畫面比例。預設值：adaptive。 | COMBO | 是 | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | 輸出影片的持續時間（秒）（4-15）。預設值：7。 | INT | 是 | 4 至 15 |
| `generate_audio` | 是否為輸出影片啟用音訊生成。預設值：True。 | BOOLEAN | 是 | true<br>false |

### 參考輸入

這些可擴充的參考插槽適用於所有模型。插槽數量上限依模型而異：Seedance 2.5 支援最多 30 張圖片、10 部影片、10 段音訊與 30 個資產；Seedance 2.0、2.0 Fast 與 2.0 Mini 則支援最多 9 張圖片、3 部影片、3 段音訊與 9 個資產。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | 可擴充插槽：連接 1..N 個參考圖片以引導輸出。數量限制依模型而定（參見各模型小節）。圖片會驗證畫面比例（0.4 至 2.5），並自動縮小至最長邊 6000 像素。 | IMAGE | 否 | 1..9 個插槽（Seedance 2.0 系列）<br>1..30 個插槽（Seedance 2.5） |
| `reference_videos` | 可擴充插槽：連接 1..N 個參考影片。數量限制依模型而定（參見各模型小節）。每部影片長度至少須為 1.8 秒，且必須符合所選模型與解析度的像素限制。 | VIDEO | 否 | 1..3 個插槽（Seedance 2.0 系列）<br>1..10 個插槽（Seedance 2.5） |
| `reference_audios` | 可擴充插槽：連接 1..N 條參考音訊。數量限制依模型而定（參見各模型小節）。每段音訊長度至少須為 1.8 秒。 | AUDIO | 否 | 1..3 個插槽（Seedance 2.0 系列）<br>1..10 個插槽（Seedance 2.5） |
| `reference_assets` | 可擴充插槽：連接 1..N 個資產 ID 字串，對應已上傳至 Seedance 虛擬素材庫的媒體。每個資產必須為 Active 狀態。你可以在提示中以 `asset1` 或 `asset 1` 這類代號引用資產；節點會將這些代號替換為資產的位置標籤（例如「Image 2」或「Video 1」）。 | STRING | 否 | 1..9 個插槽（Seedance 2.0 系列）<br>1..30 個插槽（Seedance 2.5） |
| `auto_downscale` | 自動縮小超出所選解析度像素預算的參考影片。會保留畫面比例；已在限制內的影片則不受影響。預設值：True。 | BOOLEAN | 否 | true<br>false |
| `auto_upscale` | 自動放大低於所選解析度最小像素數的參考影片。會保留畫面比例；已符合最小像素數的影片則不受影響。注意：放大低解析度來源不會增加真實細節，且可能產生較低品質的生成結果。預設值：False。進階設定。 | BOOLEAN | 否 | true<br>false |

**注意：** 至少需要一個參考圖片、影片或資產才能執行此節點（Seedance 2.5 也接受僅含音訊的參考）。參考影片與音訊的長度都必須至少為 1.8 秒，且所有參考影片（以及所有參考音訊，分別計算）的總持續時間不得超過所選模型的最大總秒數。參考圖片的畫面比例必須約在 2:5 至 5:2（0.4 至 2.5）之間，至少為 300x300 像素，並會自動縮小至最長邊 6000 像素。`task_type` 的「edit」與「extend」選項僅適用於 Seedance 2.5，且兩者都至少需要一部參考影片；使用「edit」時，輸出會保留來源剪輯本身的長度與畫面比例，且 `duration` 與 `ratio` 元件會被忽略；使用「extend」時，輸出僅包含你設定的持續時間內新生成的片段。引用的資產必須處於 Active 狀態，否則任務會失敗。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 生成的影片，會在生成任務完成後從提供者下載。若已啟用音訊生成，則包含音訊。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNodeV2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3a6bba12e719204ba5dba9d7d5f2b4c5285ed68974ee015b6e4a7892a1cf0933`
