# Grok 參考生成影片

Grok Reference-to-Video 節點會根據文字提示生成影片，並使用最多七張參考影像來引導輸出的風格與內容。使用 `grok-imagine-video-1.5` 模型時，您還可以附加最多三個預設語音參考，並在提示詞中直接以 `@ImageN` 和 `@AudioN` 標籤來引用影像與語音。此節點會將請求傳送至外部 API，等待生成完成後下載產生的影片。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於影片生成的模型。 | DYNAMIC_COMBO | 是 | `"grok-imagine-video-1.5"`<br>`"grok-imagine-video"` |
| `prompt` | 期望影片的文字描述。必須是非空字串。 | STRING | 是 | N/A |
| `seed` | 用於決定節點是否應重新執行的種子；無論種子為何，實際結果皆為非確定性（預設值：0）。 | INT | 否 | 0 至 2147483647 |

### Grok Imagine Video 1.5 輸入

當 `model` 設為 `grok-imagine-video-1.5` 時可用。

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `voice_1` | 可選的預設語音參考；可在提示詞中以 @Audio1 引用。API 僅支援這些預設語音，不支援自訂音訊（預設值：none）。 | COMBO | 否 | 預設語音選項，包含 `"none"` |
| `voice_2` | 可選的第二個語音參考；在提示詞中以 @Audio2 引用（預設值：none）。 | COMBO | 否 | 預設語音選項，包含 `"none"` |
| `voice_3` | 可選的第三個語音參考；在提示詞中以 @Audio3 引用（預設值：none）。 | COMBO | 否 | 預設語音選項，包含 `"none"` |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | `"480p"`<br>`"720p"` |
| `aspect_ratio` | 輸出影片的長寬比。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | 輸出影片的秒數長度（預設值：6）。 | INT | 是 | 1 至 15 |

### Grok Imagine Video 輸入

當 `model` 設為 `grok-imagine-video` 時可用。

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | `"480p"`<br>`"720p"` |
| `aspect_ratio` | 輸出影片的長寬比。 | COMBO | 是 | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | 輸出影片的秒數長度（預設值：6）。 | INT | 是 | 2 至 10 |

### 參考輸入

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | 可擴充插槽：連接 1 至 7 張參考影像以引導影片生成。使用 `grok-imagine-video-1.5` 時，可在提示詞中以 @Image1 ... @Image7 引用，並依照輸入順序編號；批次輸入的每一張影像均個別計算。 | IMAGE | 是 | 1 至 7 張影像 |

**注意：** 顯示的子參數取決於所選的 `model`；`grok-imagine-video-1.5` 會新增 `voice_1`、`voice_2` 和 `voice_3` 輸入。至少需要一張參考影像，總數上限為 7 張（批次輸入的每一張影像均個別計算）。使用 `grok-imagine-video-1.5` 時，提示詞可將已連接的影像引用為 `@Image1` ... `@Image7`，並將語音插槽引用為 `@Audio1`、`@Audio2`、`@Audio3`；未編號的 `@image` 或 `@audio` 指的是第一個項目。`@AudioN` 指的是 `voice_N` 小工具，而非已啟用語音的順序。引用未連接的影像或設為 `none` 的語音插槽會導致錯誤。API 僅支援預設語音，不支援自訂音訊。

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
|-------------|-------------|-----------|
| `video` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoReferenceNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ac068b34ad7efe786d29f51052a623eaf324041a99b124f6b5f81fadea661a83`
