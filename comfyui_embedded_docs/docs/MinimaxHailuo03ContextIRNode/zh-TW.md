# MiniMax H3 Context IR（提示詞增強器）

## 概述

此節點使用 MiniMax H3 Context IR 分析您的文字描述和任何附加媒體，然後產生更強且結構化的影片提示詞。傳回的提示詞旨在連接到 MiniMax H3 影片節點的提示詞輸入；如果您在該處附加媒體，請以相同順序附加相同媒體，因為增強後的提示詞會依位置參照媒體。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於提示詞增強的模型。 | DYNAMIC_COMBO | 是 | `"MiniMax H3"` |
| `first_frame` | 您打算生成影片的第一幀。無法與參考媒體搭配使用。 | IMAGE | 否 | 單張圖片 |
| `last_frame` | 您打算生成影片的最後一幀。無法與參考媒體搭配使用。 | IMAGE | 否 | 單張圖片 |

### MiniMax H3 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 您打算生成影片的描述。不能為空。（預設：`""`） | STRING | 是 | 任何文字（不能為空） |
| `duration` | 您打算生成影片的長度，以秒為單位（4-15）。（預設：5） | INT | 是 | 4 到 15 |
| `ratio` | 您打算生成影片的長寬比。`"adaptive"` 需要至少一個圖片、影片或音訊輸入。（預設：`"adaptive"`） | COMBO | 是 | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |

### 參考輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | 主體或風格參考圖片，在提示詞中依連接順序以 "Image 1".."Image 9" 表示。最多 9 張圖片。可擴充插槽：連接 `image_1`...`image_9`。 | IMAGE | 否 | 0 到 9 張圖片 |
| `reference_videos` | 動作或場景參考影片，在提示詞中依連接順序以 "Video 1".."Video 3" 表示。最多 3 段影片，每段 2-15 秒，總長度最多 15 秒。可擴充插槽：連接 `video_1`...`video_3`。 | VIDEO | 否 | 0 到 3 段影片 |
| `reference_audios` | 音訊參考，在提示詞中依連接順序以 "Audio 1".."Audio 3" 表示。最多 3 段音訊片段，每段 2-15 秒，總長度最多 15 秒。若沒有參考圖片或影片，則無法使用。可擴充插槽：連接 `audio_1`...`audio_3`。 | AUDIO | 否 | 0 到 3 段音訊 |

### 參數限制

- `prompt`、`duration`、`ratio`、`reference_images`、`reference_videos` 和 `reference_audios` 輸入屬於 `model` 選項群組的一部分，並在選取 "MiniMax H3" 時顯示。
- `first_frame` 和 `last_frame` 不能與任何參考媒體搭配使用。
- `reference_audios` 除非至少同時連接一個 `reference_image` 或 `reference_video`，否則無法使用。
- 當未連接任何幀和參考媒體時，`ratio` 不能設為 `"adaptive"`。
- 參考影片每段長度必須約為 2-15 秒，總時長不得超過 15 秒。其影格率必須介於 23.9 到 60.5 FPS 之間。
- 參考音訊每段長度必須約為 2-15 秒，總時長不得超過 15 秒。
- `first_frame`、`last_frame` 以及每張參考圖片都必須至少為 256x256 像素，且長寬比必須介於 0.4 到 2.5 之間。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `STRING` | MiniMax H3 Context IR 生成的增強結構化影片提示詞。可連接到 MiniMax H3 影片生成節點的提示詞輸入。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ContextIRNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `73015517f9c0f55f0aceeef935508a372e0d95668e4733d1c8100b53e4afa7e2`
