# ByteDance Seedance 2.0 文字轉影片

此節點使用 ByteDance 的 Seedance 2.5 或 2.0 模型，從文字描述生成影片。它會將您的提示詞傳送至所選模型，等待影片處理完成，然後回傳最終結果。

## 輸入

`model` 參數是動態下拉選單。當您選取模型時，會顯示數個該模型專屬的輸入欄位，包括文字提示詞、解析度、長寬比、持續時間與音訊生成設定。

### 通用輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|------|------|----------|------|------|
| `model` | 用於影片生成的模型。Seedance 2.5 是最新模型，可生成長達 30 秒的影片，輸出格式為 mp4/mov；Seedance 2.0 提供最高品質，支援 1080p/4k；Fast 為速度最佳化；Mini 則是最快且成本最低的生成選項。 | DYNAMIC_COMBO | 是 | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | 控制節點是否應重新執行；無論種子值為何，結果皆非確定性（預設：0）。 | INT | 否 | 0 至 2147483647 |
| `watermark` | 是否在影片中加入浮水印（預設：False）。此為進階設定。 | BOOLEAN | 否 | True / False |

### Seedance 2.5 輸入

當 `model` 設定為 `Seedance 2.5` 時，會顯示這些輸入。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|------|------|----------|------|------|
| `prompt` | 用於影片生成的文字提示詞。將口語台詞放在雙引號中，以引導生成的對話（預設：空）。 | STRING | 是 | 任意文字 |
| `resolution` | 輸出影片的解析度（預設："720p"）。 | COMBO | 是 | `"480p"`<br>`"720p"` |
| `ratio` | 輸出影片的長寬比（預設："16:9"）。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的持續時間（秒）（預設：5）。 | INT | 是 | 4 至 30 |
| `generate_audio` | 啟用輸出影片的音訊生成（預設：True）。 | BOOLEAN | 否 | True / False |
| `output_format` | 輸出影片的容器格式（預設："mp4"）。 | COMBO | 是 | `"mp4"` |

### Seedance 2.0 輸入

當 `model` 設定為 `Seedance 2.0` 時，會顯示這些輸入。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|------|------|----------|------|------|
| `prompt` | 用於影片生成的文字提示詞（預設：空）。 | STRING | 是 | 任意文字 |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | 輸出影片的長寬比（預設："16:9"）。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的持續時間（秒）（預設：7）。 | INT | 是 | 4 至 15 |
| `generate_audio` | 啟用輸出影片的音訊生成（預設：True）。 | BOOLEAN | 否 | True / False |

### Seedance 2.0 Fast 與 Seedance 2.0 Mini 輸入

當 `model` 設定為 `Seedance 2.0 Fast` 或 `Seedance 2.0 Mini` 時，會顯示這些輸入。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|------|------|----------|------|------|
| `prompt` | 用於影片生成的文字提示詞（預設：空）。 | STRING | 是 | 任意文字 |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | `"480p"`<br>`"720p"` |
| `ratio` | 輸出影片的長寬比（預設："16:9"）。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的持續時間（秒）（預設：7）。 | INT | 是 | 4 至 15 |
| `generate_audio` | 啟用輸出影片的音訊生成（預設：True）。 | BOOLEAN | 否 | True / False |

**注意：** `prompt` 在去除空白字元後必須至少包含 1 個字元，否則任務將無法通過驗證。持續時間限制取決於模型：Seedance 2.5 支援 4 至 30 秒，而 Seedance 2.0、Seedance 2.0 Fast 和 Seedance 2.0 Mini 支援 4 至 15 秒。解析度選項也因模型而異：Seedance 2.5 支援 480p 和 720p；Seedance 2.0 支援 480p、720p、1080p 和 4k；Seedance 2.0 Fast 和 Seedance 2.0 Mini 僅支援 480p 和 720p。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|--------|------|----------|
| `video` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `66d200f4ddf674b897def63604b0f29dcbf655e00b4e9b9c11e31b671ead94bc`
