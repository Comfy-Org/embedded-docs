> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoNode/zh-TW.md)

此節點使用 Kling V3 模型生成影片。它支援兩種主要模式：文字轉影片（根據文字描述建立影片）和圖片轉影片（將現有圖片動畫化）。它還提供進階功能，例如建立具有不同分段提示和時長的多段影片（故事板），並可選擇生成伴隨音訊。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `multi_shot` | COMBO | 是 | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` | 控制是生成單一影片，還是一系列具有獨立提示和時長的分段影片。當不為 "disabled" 時，會顯示每個故事板的提示和時長等額外輸入。 |
| `generate_audio` | BOOLEAN | 是 | `True` / `False` | 啟用時，節點將為影片生成音訊。預設為 `True`。 |
| `model` | COMBO | 是 | `"kling-v3"` | 模型及其相關設定。選擇此選項會顯示 `resolution` 和 `aspect_ratio` 子參數。 |
| `model.resolution` | COMBO | 是 | `"1080p"`<br>`"720p"` | 生成影片的解析度。此設定在 `model` 設為 "kling-v3" 時可用。 |
| `model.aspect_ratio` | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"` | 生成影片的長寬比。當為 `start_frame` 提供了圖片（圖片轉影片模式）時，此設定會被忽略。在 `model` 設為 "kling-v3" 時可用。 |
| `seed` | INT | 是 | 0 到 2147483647 | 用於生成的種子值。更改此值將導致節點重新執行，但結果是非確定性的。預設為 `0`。 |
| `start_frame` | IMAGE | 否 | - | 可選的起始圖片。當連接此輸入時，節點會從文字轉影片模式切換到圖片轉影片模式，對提供的圖片進行動畫處理。 |

**`multi_shot` 模式下的輸入：**
*   當 `multi_shot` 設為 **"disabled"** 時，會出現以下輸入：
    *   `prompt` (STRING): 影片的主要文字描述。必填。長度必須在 1 到 2500 個字元之間。
    *   `negative_prompt` (STRING): 描述影片中不應出現內容的文字。可選。
    *   `duration` (INT): 影片的長度（秒）。必須在 3 到 15 秒之間。預設為 `5`。
*   當 `multi_shot` 設為故事板選項（例如 `"3 storyboards"`）時，會出現每個故事板分段的輸入（例如 `storyboard_1_prompt`、`storyboard_1_duration`）。每個提示的長度必須在 1 到 512 個字元之間。**所有故事板時長的總和**必須在 3 到 15 秒之間。

**限制條件：**
*   當 `start_frame` 未連接時，節點在**文字轉影片**模式下運作。在此模式下，它使用 `model.aspect_ratio` 設定。
*   當 `start_frame` 連接時，節點在**圖片轉影片**模式下運作。`model.aspect_ratio` 設定會被忽略。輸入圖片必須至少為 300x300 像素，且長寬比在 1:2.5 到 2.5:1 之間。
*   在故事板模式（`multi_shot` 不為 "disabled"）下，主要的 `prompt` 和 `negative_prompt` 輸入會被隱藏且不被使用。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `video` | VIDEO | 生成的影片檔案。 |