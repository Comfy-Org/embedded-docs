> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoNode/zh-TW.md)

此節點使用 Kling V3 模型生成影片。它支援兩種主要模式：文字轉影片（根據文字描述建立影片）和圖片轉影片（將現有圖片動畫化）。它還提供進階功能，例如為每個部分（分鏡腳本）使用不同提示詞建立多段影片，以及選擇性地生成伴隨音訊。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `多段生成` | COMBO | 是 | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` | 控制是生成單一影片，還是生成一系列具有各自提示詞和時長的片段。當設定為非 "disabled" 時，會出現每個分鏡腳本提示詞和時長的額外輸入。 |
| `生成音訊` | BOOLEAN | 是 | `True` / `False` | 啟用時，節點將為影片生成音訊。預設值為 `True`。 |
| `模型` | COMBO | 是 | `"kling-v3"` | 模型及其相關設定。選擇此選項會顯示 `resolution` 和 `aspect_ratio` 子參數。 |
| `model.resolution` | COMBO | 是 | `"4k"`<br>`"1080p"`<br>`"720p"` | 生成影片的解析度。此設定在 `模型` 設定為 "kling-v3" 時可用。 |
| `model.aspect_ratio` | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"` | 生成影片的長寬比。當為 `起始畫格` 提供圖片時（圖片轉影片模式），此設定將被忽略。在 `模型` 設定為 "kling-v3" 時可用。 |
| `seed` | INT | 是 | 0 到 2147483647 | 用於生成的種子值。更改此值將導致節點重新執行，但結果是非確定性的。預設值為 `0`。 |
| `起始畫格` | IMAGE | 否 | - | 可選的起始圖片。連接時，節點會從文字轉影片模式切換到圖片轉影片模式，將提供的圖片動畫化。 |

**`multi_shot` 模式的輸入：**

* 當 `multi_shot` 設定為 **"disabled"** 時，會出現以下輸入：
  * `prompt` (STRING)：影片的主要文字描述。必要。長度必須在 1 到 2500 個字元之間。
  * `negative_prompt` (STRING)：描述影片中不應出現內容的文字。可選。
  * `duration` (INT)：影片的長度（秒）。必須在 3 到 15 之間。預設值為 `5`。
* 當 `multi_shot` 設定為分鏡腳本選項（例如 `"3 storyboards"`）時，會出現每個分鏡腳本片段的輸入（例如 `storyboard_1_prompt`、`storyboard_1_duration`）。每個提示詞的長度必須在 1 到 512 個字元之間。**所有分鏡腳本時長的總和**必須在 3 到 15 秒之間。

**限制條件：**

* 當 `start_frame` 未連接時，節點以**文字轉影片**模式運作。在此模式下，它使用 `model.aspect_ratio` 設定。
* 當 `start_frame` 已連接時，節點以**圖片轉影片**模式運作。`model.aspect_ratio` 設定將被忽略。輸入圖片必須至少為 300x300 像素，且長寬比必須在 1:2.5 到 2.5:1 之間。
* 在分鏡腳本模式（`multi_shot` 不為 "disabled"）下，主要的 `prompt` 和 `negative_prompt` 輸入將被隱藏且不使用。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `video` | VIDEO | 生成的影片檔案。 |

---
**Source fingerprint (SHA-256):** `f7f827d657b1d057d273eba3215ce6848d3ea05c5f348e2f3fccccfdd030dfc3`
