# MinimaxHailuo03ContextIRNode

此節點使用 MiniMax H3 Context IR 來分析您的文字描述及任何附加的媒體內容，然後產生更強大、結構化的影片提示詞。傳回的提示詞設計用於連接到 MiniMax H3 影片節點的 prompt 輸入；如果您在該處附加媒體，請以相同順序附加相同的媒體，因為增強後的提示詞會依位置參照媒體。

## 輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於提示詞增強的模型。 | COMBO | 是 | `"MiniMax H3"` |
| `prompt` | 您打算生成之影片的描述。不能為空。 (預設值：`""`) | STRING | 是 | 任意文字 |
| `duration` | 您打算生成之影片的持續時間，以秒為單位（4-15）。 (預設值：5) | INT | 是 | 4 到 15 |
| `ratio` | 您打算生成之影片的長寬比。`"adaptive"` 需要至少一個圖片、影片或音訊輸入。 (預設值：`"adaptive"`) | COMBO | 是 | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `reference_images` | 主體或風格的參考圖片，在提示詞中依連接順序稱為「Image 1」至「Image 9」。最多 9 張圖片。 | IMAGE | 否 | 0 到 9 張圖片 |
| `reference_videos` | 動作或場景的參考影片，在提示詞中依連接順序稱為「Video 1」至「Video 3」。最多 3 個影片，每個 2-15 秒，總長 15 秒。 | VIDEO | 否 | 0 到 3 個影片 |
| `reference_audios` | 音訊參考，在提示詞中依連接順序稱為「Audio 1」至「Audio 3」。最多 3 個片段，每個 2-15 秒，總長 15 秒。若無參考圖片或影片則無法使用。 | AUDIO | 否 | 0 到 3 個片段 |
| `first_frame` | 您打算生成之影片的第一幀。不能與參考媒體組合使用。 | IMAGE | 否 | 單張圖片 |
| `last_frame` | 您打算生成之影片的最後一幀。不能與參考媒體組合使用。 | IMAGE | 否 | 單張圖片 |

### 參數限制

- `prompt`、`duration`、`ratio`、`reference_images`、`reference_videos` 和 `reference_audios` 輸入屬於 `model` 選項組的一部分。
- `first_frame` 和 `last_frame` 不能與任何參考媒體組合使用。
- 除非同時連接至少一個 `reference_image` 或 `reference_video`，否則無法使用 `reference_audios`。
- 當未連接任何幀且未連接參考媒體時，`ratio` 不能設定為 `"adaptive"`。
- 參考影片每個必須約 2-15 秒，總持續時間不超過 15 秒。其幀率必須介於 23.9 至 60.5 FPS 之間。
- 參考音訊每個必須約 2-15 秒，總持續時間不超過 15 秒。
- `first_frame`、`last_frame` 和每張參考圖片都必須至少為 256x256 像素，且長寬比介於 0.4 至 2.5 之間。

## 輸出

| 輸出名 | 說明 | 資料型別 |
|-------------|-------------|-----------|
| `STRING` | 由 MiniMax H3 Context IR 生成的增強結構化影片提示詞。可連接到 MiniMax H3 影片生成節點的 `prompt` 輸入。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ContextIRNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `73015517f9c0f55f0aceeef935508a372e0d95668e4733d1c8100b53e4afa7e2`
