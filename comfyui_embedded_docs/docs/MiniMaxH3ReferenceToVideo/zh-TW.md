# MiniMax H3 參考轉影片

MiniMax H3 Reference to Video 節點會建立 MiniMax H3 參考轉影片生成所需的文字條件和空的音訊-影片潛在空間。您可以提供提示詞，以及選用的參考圖片、影片和音訊片段；節點會將這些參考內容編碼為模型生成時可使用的 token。提示詞使用 `<Picture i>`、`<Video k>` 和 `<Audio j>` 標籤來指稱參考內容。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `clip` | 用於將提示詞 token 化，以及將參考媒體編碼為條件 token 的 CLIP 模型。 | CLIP | 是 | |
| `vae` | 用於將參考圖片和參考影片影格編碼至潛在空間的 VAE。 | VAE | 是 | |
| `audio_vae` | 用於將參考音訊編碼至潛在空間的 VAE（音訊取樣率 32 kHz）。 | VAE | 是 | |
| `prompt` | 影片的文字提示詞。可使用 `<Picture i>`、`<Video k>` 和 `<Audio j>` 標籤（每種類型從 1 起算）來指稱參考媒體。支援多行和動態提示詞。 | STRING | 是 | |
| `width` | 生成影片的寬度（像素，預設：1344）。 | INT | 是 | 32 to 16384 (step 32) |
| `height` | 生成影片的高度（像素，預設：768）。 | INT | 是 | 32 to 16384 (step 32) |
| `length` | 24 fps 下的影格數；124 約等於 5 秒，訓練範圍約為 124-362（預設：124）。 | INT | 是 | 5 to 3600 (step 17) |
| `ref_image_size` | 參考圖片的縮放模式。`match` 只會將每張參考圖片按長寬比縮小至生成的像素面積；`max` 使用參考管線的 2048px 短邊來獲得最佳身分保真度。參考 token 會持續存在於每個取樣步驟中，因此 `max` 可能慢上好幾倍（預設：`match`）。 | COMBO | 是 | `"match"`<br>`"max"` |
| `ref_images` | 選用參考圖片。每張圖片若短邊大於 2048px，會縮小至短邊 2048px；且絕不放大。可提供多張圖片。 | IMAGE | 否 | 0 to 9 |
| `ref_videos` | 選用的參考影片影格，以 24 fps 擷取（2-15 秒）。可提供多部影片。 | IMAGE | 否 | 0 to 3 |
| `ref_video_audios` | 與參考影片依索引配對的選用音軌；`ref_video_audio_N` 是與其同編號 `ref_video_N` 對應的音軌。 | AUDIO | 否 | 0 to 3 |
| `ref_audios` | 選用的獨立參考音訊片段。 | AUDIO | 否 | 0 to 3 |

備註：
- 提示詞使用每種類型各自從 1 起算的標籤來指稱參考媒體：`<Picture i>` 代表圖片、`<Video k>` 代表影片、`<Audio j>` 代表音訊。參考內容會以固定順序呈現給模型：先圖片，再影片（每部影片的配樂 `<Audio j>` 標籤會緊接在其 `<Video k>` 標籤之前），最後是獨立音訊。
- 參考影片至少必須包含 5 個影格（24 fps 時約 0.2 秒），否則節點會拋出錯誤。影片影格會上限至所選的 `length`，並裁剪至受支援的影格數。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `positive` | 條件內容，包含編碼後的提示詞，以及 MiniMax H3 模型使用的已編碼參考圖片、影片和音訊 token。 | CONDITIONING |
| `latent` | 空的音訊-影片潛在空間，具有要求的 `width`、`height` 和 `length`（影格數）。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ReferenceToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d9a444e712cdc255d7c56a3ab38d0523659f198b3228b9283a7028cfd0e4f3f9`
