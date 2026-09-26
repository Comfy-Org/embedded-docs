# ByteDance Seedance 2.0 首末幀轉影片

此節點使用 ByteDance Seedance 模型，從必填的第一幀圖像與選填的最後一幀圖像生成影片。您可以使用文字提示詞描述影片；第一幀會引導影片開頭，最後一幀則引導影片結尾。它支援 Seedance 2.5 與 Seedance 2.0 系列（Seedance 2.0、Seedance 2.0 Fast 和 Seedance 2.0 Mini）。選取 `Seedance 2.5 Draft` 模型時，會改為渲染快速的 480p 預覽；將產生的 `draft_task_id` 連接到 ByteDance Seedance 2.5 Draft to Final Video 節點，即可渲染 1080p 最終影片。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | Seedance 2.5 為最新模型，支援最長 30 秒的影片與 mp4 輸出；Seedance 2.5 Draft 可快速產生 480p 預覽，其 `draft_task_id` 輸出可在 ByteDance Seedance 2.5 Draft to Final Video 節點中渲染成 1080p 最終影片；Seedance 2.0 可提供最高品質與 4k；Fast 可最佳化速度；Mini 可產生最快、成本最低的結果。選取模型後，下方會顯示該模型專屬的輸入。 | DYNAMIC_COMBO | 是 | `"Seedance 2.5"`<br>`"Seedance 2.5 Draft"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `首幀圖像` | 影片的第一幀圖像。 | IMAGE | 否 | - |
| `末幀圖像` | 影片的最後一幀圖像。 | IMAGE | 否 | - |
| `first_frame_asset_id` | 要用作第一幀的 Seedance asset_id。與 `first_frame` 圖像輸入互斥。預設為空字串。 | STRING | 否 | - |
| `last_frame_asset_id` | 要用作最後一幀的 Seedance asset_id。與 `last_frame` 圖像輸入互斥。預設為空字串。 | STRING | 否 | - |
| `種子` | Seed 控制節點是否應重新執行；無論 seed 為何，結果都是非確定性的。預設為 0。 | INT | 是 | 0 到 2147483647 |
| `浮水印` | 是否在影片中加入浮水印。預設為 False。 | BOOLEAN | 是 | False<br>True |

### Seedance 2.5 輸入

選取 `Seedance 2.5` 時會顯示這些輸入。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示詞。將台詞放在雙引號中，以引導生成的對話。 | STRING | 是 | - |
| `resolution` | 輸出影片的解析度。預設為 720p。 | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `duration` | 輸出影片的長度（秒，4-30）。預設為 5。 | INT | 是 | 4 到 30 |
| `generate_audio` | 啟用輸出影片的音訊生成。預設為 True。 | BOOLEAN | 是 | False<br>True |
| `output_format` | 輸出影片的容器格式。預設為 mp4。 | COMBO | 是 | `"mp4"` |

### Seedance 2.5 Draft 輸入

選取 `Seedance 2.5 Draft` 時會顯示這些輸入。參數集與上方的 Seedance 2.5 相同，但 `resolution` 只提供 `"480p"`（預設 `"480p"`）。

### Seedance 2.0 輸入

選取 `Seedance 2.0` 時會顯示這些輸入。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示詞。 | STRING | 是 | - |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | 輸出影片的長寬比。預設為 `adaptive`，其使用最接近輸入幀長寬比的支援比例。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的長度（秒，4-15）。預設為 7。 | INT | 是 | 4 到 15 |
| `generate_audio` | 啟用輸出影片的音訊生成。預設為 True。 | BOOLEAN | 是 | False<br>True |

### Seedance 2.0 Fast 和 Seedance 2.0 Mini 輸入

`Seedance 2.0 Fast` 與 `Seedance 2.0 Mini` 共用。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示詞。 | STRING | 是 | - |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | `"480p"`<br>`"720p"` |
| `ratio` | 輸出影片的長寬比。預設為 `adaptive`，其使用最接近輸入幀長寬比的支援比例。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | 輸出影片的長度（秒，4-15）。預設為 7。 | INT | 是 | 4 到 15 |
| `generate_audio` | 啟用輸出影片的音訊生成。預設為 True。 | BOOLEAN | 是 | False<br>True |

**參數限制**

- 您必須以 `first_frame` 圖像或 `first_frame_asset_id` 提供第一幀。同時提供兩者會引發錯誤；兩者皆未提供也會引發錯誤。
- `last_frame` 和 `last_frame_asset_id` 輸入為選填，但同一幀不能同時提供兩者。
- Asset ID 必須參照現有且有效的 Seedance Image 素材。
- `prompt` 輸入為必填，且不能為空。
- 每次執行都會將其任務 ID 以 `draft_task_id` 形式傳回，但只有 `Seedance 2.5 Draft` 執行的 ID 可由 ByteDance Seedance 2.5 Draft to Final Video 節點渲染。使用任何其他模型時，必須將該輸出保持未連接，否則執行會失敗。
- 使用 `Seedance 2.5` 時，輸出長寬比一律為 adaptive，並遵循第一幀本身的長寬比，因此不會顯示 `ratio` 輸入。
- 使用 Seedance 2.0 系列模型與本機幀圖像時，圖像會先置中裁切並調整大小至目標輸出解析度與比例，再進行生成。當 `ratio` 為 `adaptive` 時，會使用最接近輸入圖像的支援比例。
- 本機幀圖像會驗證支援的長寬比與尺寸；過大的圖像會縮小。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的影片。 | VIDEO |
| `draft_task_id` | 執行所傳回的任務 ID。只有 `Seedance 2.5 Draft` 執行會產生可供 ByteDance Seedance 2.5 Draft to Final Video 節點渲染的草稿；使用任何其他模型時，必須將該輸出保持未連接，否則執行會失敗。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `363f1baac1685c2dada0e64a0b339f6ab2671161dccb002eb81f6b4f0d0aa243`
