# ByteDance Seedance 2.5 參考轉影片

ByteDance Seedance 2.5 Reference to Video 會使用 ByteDance Seedance 模型（Seedance 2.5、2.5 Draft、2.0、2.0 Fast 與 2.0 Mini），在文字提示與可選的參考圖像、影片、音訊或先前上傳的素材庫素材引導下，產生、編輯或延長影片。它會上傳參考內容、提交生成任務、等待完成，並傳回完成的影片檔案。選擇 `Seedance 2.5 Draft` 時，會改為快速渲染 480p 預覽；將產生的 `draft_task_id` 連接到 ByteDance Seedance 2.5 Draft to Final Video 節點，即可渲染 1080p 最終影片。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 模型選擇器。Seedance 2.5 適用於最新模型，支援最長 30 秒的影片與 mp4 輸出；Seedance 2.5 Draft 適用於快速 480p 預覽，其 `draft_task_id` 輸出可在 ByteDance Seedance 2.5 Draft to Final Video 節點中渲染 1080p 最終影片；Seedance 2.0 適用於最高品質與 4k；Fast 適用於速度最佳化；Mini 適用於最快、成本最低的生成。選擇模型會變更下方顯示的輸入小工具。 | DYNAMIC_COMBO | 是 | "Seedance 2.5"<br>"Seedance 2.5 Draft"<br>"Seedance 2.0"<br>"Seedance 2.0 Fast"<br>"Seedance 2.0 Mini" |
| `種子` | 種子會控制節點是否應重新執行；無論種子為何，結果都是非確定性的。預設值：0。 | INT | 是 | 0 至 2147483647 |
| `浮水印` | 是否在影片中加入浮水印。預設值：False。進階設定。 | BOOLEAN | 是 | true<br>false |

### Seedance 2.5 輸入

當 `model` 設為 "Seedance 2.5" 時，會顯示這些輸入。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。將台詞放入雙引號中，可引導生成的對話。預設值：空字串。 | STRING | 是 | 多行文字 |
| `resolution` | 輸出影片的解析度。預設值：720p。 | COMBO | 是 | "480p"<br>"720p"<br>"1080p" |
| `ratio` | 輸出影片的長寬比。預設值：16:9。 | COMBO | 是 | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | 輸出影片的持續時間（秒）（4-30）。預設值：5。 | INT | 是 | 4 至 30 |
| `generate_audio` | 啟用輸出影片的音訊生成。預設值：True。 | BOOLEAN | 是 | true<br>false |
| `task_type` | 如何處理參考媒體。除了 auto 以外的每個值都會在提交任務時進行驗證，因此不相符的設定會在生成開始前失敗。<br>auto：模型會根據提示與輸入推斷任務，與其判讀衝突的設定只會在生成開始後失敗。<br>reference：在參考圖像、影片與音訊的引導下生成新影片。<br>edit：變更已連接的參考影片（新增、移除、取代）；輸出會保留來源片段的原始長度與長寬比，且會忽略 `duration` 與 `ratio` 小工具。<br>extend：向前或向後延續已連接的參考影片；提示應包含 "extend forward"、"extend backward" 或 "continue"，長寬比會跟隨來源片段，且輸出只包含你所設定持續時間內新生成的片段，不包含來源片段。預設值：auto。 | COMBO | 是 | "auto"<br>"reference"<br>"edit"<br>"extend" |
| `output_format` | 輸出影片的容器格式。預設值：mp4。 | COMBO | 是 | "mp4" |

### Seedance 2.5 Draft 輸入

當 `model` 設為 "Seedance 2.5 Draft" 時，會顯示這些輸入。參數集與上方的 Seedance 2.5 相同，差別在於 `resolution` 僅提供 `"480p"`（預設值 `"480p"`）。

### Seedance 2.0 輸入

當 `model` 設為 "Seedance 2.0" 時，會顯示這些輸入。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。預設值：空字串。 | STRING | 是 | 多行文字 |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | "480p"<br>"720p"<br>"1080p"<br>"4k" |
| `ratio` | 輸出影片的長寬比。預設值：adaptive。 | COMBO | 是 | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | 輸出影片的持續時間（秒）（4-15）。預設值：7。 | INT | 是 | 4 至 15 |
| `generate_audio` | 啟用輸出影片的音訊生成。預設值：True。 | BOOLEAN | 是 | true<br>false |

### Seedance 2.0 Fast 與 Seedance 2.0 Mini 輸入

當 `model` 設為 "Seedance 2.0 Fast" 或 "Seedance 2.0 Mini" 時，會顯示這些輸入。兩個模型共用相同的輸入集。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。預設值：空字串。 | STRING | 是 | 多行文字 |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | "480p"<br>"720p" |
| `ratio` | 輸出影片的長寬比。預設值：adaptive。 | COMBO | 是 | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | 輸出影片的持續時間（秒）（4-15）。預設值：7。 | INT | 是 | 4 至 15 |
| `generate_audio` | 啟用輸出影片的音訊生成。預設值：True。 | BOOLEAN | 是 | true<br>false |

### 參考輸入

這些可增長的參考插槽適用於所有模型。每個模型的最大插槽數量不同：Seedance 2.5 最多支援 30 張圖像、10 部影片、10 個音訊與 30 個素材；Seedance 2.0、2.0 Fast 與 2.0 Mini 最多支援 9 張圖像、3 部影片、3 個音訊與 9 個素材。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | 可增長的插槽：連接 1..N 張可引導輸出的參考圖像。數量限制依模型而異（請參閱各模型章節）。圖像會驗證長寬比（0.4 到 2.5），並自動縮小至最大邊 6000 像素。 | IMAGE | 否 | 1..9 個插槽（Seedance 2.0 系列）<br>1..30 個插槽（Seedance 2.5） |
| `reference_videos` | 可增長的插槽：連接 1..N 部參考影片。數量限制依模型而異（請參閱各模型章節）。每部影片長度必須至少 1.8 秒，且必須符合所選模型與解析度的像素限制。 | VIDEO | 否 | 1..3 個插槽（Seedance 2.0 系列）<br>1..10 個插槽（Seedance 2.5） |
| `reference_audios` | 可增長的插槽：連接 1..N 個參考音訊軌。數量限制依模型而異（請參閱各模型章節）。每個音訊長度必須至少 1.8 秒。 | AUDIO | 否 | 1..3 個插槽（Seedance 2.0 系列）<br>1..10 個插槽（Seedance 2.5） |
| `reference_assets` | 可增長的插槽：連接 1..N 個素材 ID 字串，用於已上傳至 Seedance 虛擬素材庫的媒體。每個素材必須為 Active。你可以在提示中使用 `asset1` 或 `asset 1` 等標記來引用素材；節點會將它們替換為素材的位置標籤（例如 "Image 2" 或 "Video 1"）。 | STRING | 否 | 1..9 個插槽（Seedance 2.0 系列）<br>1..30 個插槽（Seedance 2.5） |
| `auto_downscale` | 自動縮小超出所選解析度之模型像素預算的參考影片。會保留長寬比；已在限制內的影片不會被變更。預設值：True。 | BOOLEAN | 否 | true<br>false |
| `auto_upscale` | 自動放大低於所選解析度下模型最低像素數的參考影片。會保留長寬比；已達最低標準的影片不會被變更。注意：放大低解析度來源不會增加真實細節，且可能產生較低品質的生成結果。預設值：False。進階設定。 | BOOLEAN | 否 | true<br>false |

**注意：** 執行節點時至少需要一張參考圖像、一部影片或一個素材（Seedance 2.5 也接受僅有音訊的參考）。參考影片與音訊各自長度必須至少 1.8 秒，且所有參考影片的總持續時間（以及所有參考音訊的總持續時間，分開計算）不得超過所選模型的最大總秒數。參考圖像的長寬比必須約介於 2:5 到 5:2（0.4 到 2.5）之間，至少為 300x300 像素，並會自動縮小至最大邊 6000 像素。`task_type` 的 "edit" 與 "extend" 選項僅適用於 Seedance 2.5，且兩者都需要至少一部參考影片；使用 "edit" 時，輸出會保留來源片段的原始長度與長寬比，並忽略 `duration` 與 `ratio` 小工具；使用 "extend" 時，輸出只包含你所設定持續時間內新生成的片段。引用的素材必須處於 Active 狀態，否則任務會失敗。每次執行都會傳回其任務 ID 作為 `draft_task_id`，但只有 `Seedance 2.5 Draft` 執行的 ID 可由 ByteDance Seedance 2.5 Draft to Final Video 節點渲染，因此使用任何其他模型時，該輸出必須保持未連接，否則執行會失敗。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 生成的影片，會在生成任務完成後從供應商下載。啟用音訊生成時會包含音訊。 | VIDEO |
| `draft_task_id` | 執行時傳回的任務 ID。只有 `Seedance 2.5 Draft` 執行會產生可由 ByteDance Seedance 2.5 Draft to Final Video 節點渲染的草稿；使用任何其他模型時，該輸出必須保持未連接，否則執行會失敗。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNodeV2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `12fee29b280ff71e29f268f52131d1c15cf3066e0804356b735b61d97c80a6a9`
