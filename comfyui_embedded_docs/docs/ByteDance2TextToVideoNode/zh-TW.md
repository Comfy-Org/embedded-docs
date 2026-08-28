# ByteDance Seedance 2.0 文字轉影片

此節點使用 ByteDance 的 Seedance 2.5 或 2.0 模型，根據文字提示詞生成影片。它會將提示詞傳送至所選模型，等待影片處理完成，然後傳回產生的影片檔案。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 用於影片生成的 Seedance 模型。Seedance 2.5 是最新模型，支援長達 30 秒的影片以及 mp4/mov 輸出；Seedance 2.0 專為最高品質與 4k 而設；Seedance 2.0 Fast 專為速度最佳化而設；Seedance 2.0 Mini 專為最快、成本最低的生成而設。選取模型後，會顯示提示詞、解析度、長寬比、持續時間與音訊生成的額外輸入。 | DYNAMIC_COMBO | 是 | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `種子` | 控制節點是否應重新執行；無論 `seed` 為何，結果皆為非確定性。（預設值：0） | INT | 否 | 0 至 2147483647 |
| `浮水印` | 是否在影片中加入浮水印。（預設值：False）這是進階設定。 | BOOLEAN | 否 | True / False |

### Seedance 2.5 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示詞。將口說台詞放在雙引號中，以引導生成的對白。 | STRING | 是 | — |
| `resolution` | 輸出影片的解析度。（預設值：`"720p"`） | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `ratio` | 輸出影片的長寬比。（預設值：`"16:9"`） | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的持續時間（秒）。（預設值：5） | INT | 是 | 4 至 30 |
| `generate_audio` | 為輸出影片啟用音訊生成。（預設值：True） | BOOLEAN | 是 | True / False |
| `output_format` | 輸出影片的容器格式。（預設值：`"mp4"`） | COMBO | 是 | `"mp4"` |

### Seedance 2.0 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示詞。 | STRING | 是 | — |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | 輸出影片的長寬比。（預設值：`"16:9"`） | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的持續時間（秒）。（預設值：7） | INT | 是 | 4 至 15 |
| `generate_audio` | 為輸出影片啟用音訊生成。（預設值：True） | BOOLEAN | 是 | True / False |

### Seedance 2.0 Fast 和 Seedance 2.0 Mini 輸入

由 Seedance 2.0 Fast 與 Seedance 2.0 Mini 共用；這兩個模型暴露相同的參數。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示詞。 | STRING | 是 | — |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | `"480p"`<br>`"720p"` |
| `ratio` | 輸出影片的長寬比。（預設值：`"16:9"`） | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的持續時間（秒）。（預設值：7） | INT | 是 | 4 至 15 |
| `generate_audio` | 為輸出影片啟用音訊生成。（預設值：True） | BOOLEAN | 是 | True / False |

**注意：** `model` 選擇器是動態的；每個模型區段下顯示的輸入會在選取該模型時出現。提示詞在去除空白後必須至少包含 1 個字元。解析度和長度限制取決於所選模型：Seedance 2.5 支援 480p/720p/1080p 與 4 至 30 秒，Seedance 2.0 支援 480p/720p/1080p/4k 與 4 至 15 秒，而 Seedance 2.0 Fast 與 Seedance 2.0 Mini 僅支援 480p/720p 與 4 至 15 秒。`seed` 值僅控制節點是否重新執行；它不會讓結果具有確定性。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 產生的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e3b11f5a538d4b9b7e49f651d3939651edfe85000e02e66a8d7700c3389c4b9c`
