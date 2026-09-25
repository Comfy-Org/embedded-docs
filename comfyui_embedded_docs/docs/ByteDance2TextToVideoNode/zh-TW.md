# ByteDance Seedance 2.0 文字轉影片

此節點使用 ByteDance 的 Seedance 2.5 或 2.0 模型，根據文字提示生成影片。它會將提示傳送至所選模型，等待影片處理完成，並回傳生成的影片檔案。選擇 `Seedance 2.5 Draft` 模型時，會改為渲染快速的 480p 預覽；將生成的 `draft_task_id` 連接到 ByteDance Seedance 2.5 Draft to Final Video 節點，即可渲染 1080p 最終影片。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 用於影片生成的 Seedance 模型。Seedance 2.5 是最新模型，支援長達 30 秒的影片以及 mp4/mov 輸出；Seedance 2.5 Draft 會渲染快速的 480p 預覽，其 `draft_task_id` 輸出會在 ByteDance Seedance 2.5 Draft to Final Video 節點中渲染 1080p 最終影片；Seedance 2.0 適合最高品質與 4k；Seedance 2.0 Fast 適合速度最佳化；Seedance 2.0 Mini 適合最快速、最低成本的生成。選擇模型後會顯示額外輸入，用於提示、解析度、長寬比、時長與音訊生成。 | DYNAMIC_COMBO | 是 | `"Seedance 2.5"`<br>`"Seedance 2.5 Draft"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `種子` | 控制節點是否應重新執行；無論 `seed` 為何，結果都是非確定性的。（預設：0） | INT | 否 | 0 至 2147483647 |
| `浮水印` | 是否要在影片中加入浮水印。（預設：False）這是進階設定。 | BOOLEAN | 否 | True / False |

### Seedance 2.5 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。將台詞放在雙引號中，以引導生成的對話。 | STRING | 是 | — |
| `resolution` | 輸出影片的解析度。（預設：`"720p"`） | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `ratio` | 輸出影片的長寬比。（預設：`"16:9"`） | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的時長，以秒為單位。（預設：5） | INT | 是 | 4 至 30 |
| `generate_audio` | 為輸出影片啟用音訊生成。（預設：True） | BOOLEAN | 是 | True / False |
| `output_format` | 輸出影片的容器格式。（預設：`"mp4"`） | COMBO | 是 | `"mp4"` |

### Seedance 2.5 Draft 輸入

這些輸入會在選擇 `Seedance 2.5 Draft` 時顯示。參數集與上方 Seedance 2.5 相同，差別在於 `resolution` 僅提供 `"480p"`（預設 `"480p"`）。

### Seedance 2.0 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。 | STRING | 是 | — |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | 輸出影片的長寬比。（預設：`"16:9"`） | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的時長，以秒為單位。（預設：7） | INT | 是 | 4 至 15 |
| `generate_audio` | 為輸出影片啟用音訊生成。（預設：True） | BOOLEAN | 是 | True / False |

### Seedance 2.0 Fast 與 Seedance 2.0 Mini 輸入

由 Seedance 2.0 Fast 與 Seedance 2.0 Mini 共用；兩個模型皆提供相同的參數。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。 | STRING | 是 | — |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | `"480p"`<br>`"720p"` |
| `ratio` | 輸出影片的長寬比。（預設：`"16:9"`） | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的時長，以秒為單位。（預設：7） | INT | 是 | 4 至 15 |
| `generate_audio` | 為輸出影片啟用音訊生成。（預設：True） | BOOLEAN | 是 | True / False |

**注意：** `model` 選擇器是動態的；每個模型區段下方顯示的輸入，會在選取該模型時出現。移除空白後，提示的長度必須至少為 1 個字元。解析度與時長限制取決於所選模型：Seedance 2.5 支援 480p/720p/1080p 以及 4 到 30 秒，Seedance 2.0 支援 480p/720p/1080p/4k 以及 4 到 15 秒，而 Seedance 2.0 Fast 與 Seedance 2.0 Mini 僅支援 480p/720p 以及 4 到 15 秒；Seedance 2.5 Draft 僅支援 480p 以及 4 到 30 秒。`draft_task_id` 輸出僅由 Seedance 2.5 Draft 產生，因此使用任何其他模型時，必須使其保持未連接，否則執行會失敗。`seed` 值僅控制節點是否重新執行；它不會讓結果變成確定性。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 生成的影片檔案。 | VIDEO |
| `draft_task_id` | 草稿執行的任務 ID。僅 Seedance 2.5 Draft 模型會產生它；將其連接到 ByteDance Seedance 2.5 Draft to Final Video 節點，以渲染 1080p 最終影片。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2abad0c4eab5a1286c8da9237bcec52b275c40188b3b7dc9eede5d5f4cbb11d3`
