# ByteDance2ReferenceNodeV2

ByteDance Seedance 2.5 Reference to Video 使用 ByteDance Seedance 模型（Seedance 2.5、2.0、2.0 Fast 和 2.0 Mini），在文字提示詞以及可選的參考圖片、影片、音訊或先前上傳的素材庫資產引導下，生成、編輯或擴展影片。它會上傳參考素材、提交生成任務、等待完成，然後回傳完成的影片檔案。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 模型選擇器。Seedance 2.5 為最新模型，影片最長 30 秒，輸出格式為 mp4/mov；Seedance 2.0 提供最高品質及 4k；Fast 為速度最佳化；Mini 為最快且成本最低的生成。選擇模型會改變下方顯示的輸入控件。 | DYNAMIC_COMBO | 是 | "Seedance 2.5"<br>"Seedance 2.0"<br>"Seedance 2.0 Fast"<br>"Seedance 2.0 Mini" |
| `種子` | 種子控制節點是否應重新執行；無論種子為何，結果皆非確定性。預設值：0。 | INT | 是 | 0 至 2147483647 |
| `浮水印` | 是否在影片中加入浮水印。預設值：False。進階設定。 | BOOLEAN | 是 | true<br>false |

### Seedance 2.5 輸入

當 `model` 設定為 "Seedance 2.5" 時，會顯示這些輸入。

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 影片生成的文字提示詞。將口語對白放在雙引號中，以引導生成的對話。預設值：空字串。 | STRING | 是 | Multiline text |
| `resolution` | 輸出影片的解析度。預設值：720p。 | COMBO | 是 | "480p"<br>"720p"<br>"1080p" |
| `ratio` | 輸出影片的長寬比。預設值：16:9。 | COMBO | 是 | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | 輸出影片的持續時間（秒）（4-30）。預設值：5。 | INT | 是 | 4 至 30 |
| `generate_audio` | 為輸出影片啟用音訊生成。預設值：True。 | BOOLEAN | 是 | true<br>false |
| `task_type` | 對參考媒體進行什麼操作。除 auto 以外的每個值都會在任務提交時進行驗證，因此不相符的設定會在生成開始前失敗。<br>auto：模型從提示詞和輸入推斷任務，與其解讀衝突的設定會在生成開始後才失敗。<br>reference：以參考圖片、影片和音訊為引導，生成新影片。<br>edit：變更已連接的參考影片（新增、移除、替換）；輸出會保留來源片段自身的長度和長寬比，且 `duration` 和 `ratio` 控件會被忽略。<br>extend：向前或向後延續已連接的參考影片；提示詞應包含 "extend forward"、"extend backward" 或 "continue"，長寬比跟隨來源片段，且輸出僅包含您設定的持續時間內新生成的片段，而不包含來源片段。預設值：auto。 | COMBO | 是 | "auto"<br>"reference"<br>"edit"<br>"extend" |
| `output_format` | 輸出影片的容器格式。預設值：mp4。 | COMBO | 是 | "mp4" |

### Seedance 2.0 輸入

當 `model` 設定為 "Seedance 2.0" 時，會顯示這些輸入。

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 影片生成的文字提示詞。預設值：空字串。 | STRING | 是 | Multiline text |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | "480p"<br>"720p"<br>"1080p"<br>"4k" |
| `ratio` | 輸出影片的長寬比。預設值：adaptive。 | COMBO | 是 | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | 輸出影片的持續時間（秒）（4-15）。預設值：7。 | INT | 是 | 4 至 15 |
| `generate_audio` | 為輸出影片啟用音訊生成。預設值：True。 | BOOLEAN | 是 | true<br>false |

### Seedance 2.0 Fast 與 Seedance 2.0 Mini 輸入

當 `model` 設定為 "Seedance 2.0 Fast" 或 "Seedance 2.0 Mini" 時，會顯示這些輸入。兩個模型共享相同的輸入集合。

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 影片生成的文字提示詞。預設值：空字串。 | STRING | 是 | Multiline text |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | "480p"<br>"720p" |
| `ratio` | 輸出影片的長寬比。預設值：adaptive。 | COMBO | 是 | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9"<br>"adaptive" |
| `duration` | 輸出影片的持續時間（秒）（4-15）。預設值：7。 | INT | 是 | 4 至 15 |
| `generate_audio` | 為輸出影片啟用音訊生成。預設值：True。 | BOOLEAN | 是 | true<br>false |

### 參考輸入

這些可擴展的參考插槽適用於所有模型。每個模型的最大插槽數不同：Seedance 2.5 最多支援 30 張圖片、10 個影片、10 個音訊和 30 個資產；Seedance 2.0、2.0 Fast 和 2.0 Mini 最多支援 9 張圖片、3 個影片、3 個音訊和 9 個資產。

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | 可擴展插槽：連接 1..N 個參考圖片以引導輸出。數量限制依模型而定（參見各模型小節）。圖片會驗證長寬比（0.4 至 2.5），並自動縮小至最大邊長 6000 像素。 | IMAGE | No | 1..9 slots (Seedance 2.0 family)<br>1..30 slots (Seedance 2.5) |
| `reference_videos` | 可擴展插槽：連接 1..N 個參考影片。數量限制依模型而定（參見各模型小節）。每個影片長度至少必須為 1.8 秒，且必須符合所選模型和解析度的像素限制。 | VIDEO | No | 1..3 slots (Seedance 2.0 family)<br>1..10 slots (Seedance 2.5) |
| `reference_audios` | 可擴展插槽：連接 1..N 個參考音訊軌道。數量限制依模型而定（參見各模型小節）。每個音訊長度至少必須為 1.8 秒。 | AUDIO | No | 1..3 slots (Seedance 2.0 family)<br>1..10 slots (Seedance 2.5) |
| `reference_assets` | 可擴展插槽：連接 1..N 個已上傳至 Seedance 虛擬媒體庫之媒體的資產 ID 字串。每個資產必須處於 Active 狀態。您可以在提示詞中使用 `asset1` 或 `asset 1` 等語法來引用資產；節點會將其替換為資產的位置標籤（例如「Image 2」或「Video 1」）。 | STRING | No | 1..9 slots (Seedance 2.0 family)<br>1..30 slots (Seedance 2.5) |
| `auto_downscale` | 自動縮小超出所選解析度模型像素預算的參考影片。保留長寬比；已在限制內的影片不會被修改。預設值：True。 | BOOLEAN | No | true<br>false |
| `auto_upscale` | 自動放大低於所選解析度模型最小像素數的參考影片。保留長寬比；已達到最小值的影片不會被修改。注意：放大低解析度來源並不會增加真實細節，且可能產生較低品質的生成結果。預設值：False。進階設定。 | BOOLEAN | No | true<br>false |

**注意：** 執行此節點至少需要一個參考圖片、影片或資產（Seedance 2.5 也接受僅音訊的參考）。參考影片和音訊各自長度至少必須為 1.8 秒，且所有參考影片的總持續時間（以及所有參考音訊的總持續時間）不得超過所選模型的最大總秒數。參考圖片的長寬比必須介於約 2:5 至 5:2（0.4 至 2.5）之間，至少為 300x300 像素，並會自動縮小至最大邊長 6000 像素。`task_type` 的 "edit" 和 "extend" 選項僅適用於 Seedance 2.5，且兩者都至少需要一個參考影片；使用 "edit" 時，輸出會保留來源片段自身的長度和長寬比，且 `duration` 和 `ratio` 控件會被忽略；使用 "extend" 時，輸出僅包含您設定的持續時間內新生成的片段。引用的資產必須處於 Active 狀態，否則任務會失敗。

## 輸出

| 輸出名 | 說明 | 資料型別 |
|-------------|-------------|-----------|
| `video` | 生成的影片，在生成任務完成後從提供者下載。若啟用音訊生成，則包含音訊。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNodeV2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3a6bba12e719204ba5dba9d7d5f2b4c5285ed68974ee015b6e4a7892a1cf0933`
