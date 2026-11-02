# MiniMax H3 Max Insert Video

此節點會以新生成的場景，取代影片中從開始時間到接續時間之間的部分，並由提示詞與可選的參考圖片和參考影片引導。來源影片會在 `start_time` 處切斷，並於 `resume_time` 處接續；被移除的片段會重新生成後再拼接回去。可用於修正鏡頭、替換動作，或銜接片段中的兩個部分。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影片生成的模型。 | DYNAMIC_COMBO | 是 | "MiniMax H3 Max" |

### MiniMax H3 Max 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `video` | 來源影片，長度最多 60 秒。長寬比必須介於 0.4 與 2.5 之間。 | VIDEO | 是 | 0 到 60 秒 |
| `reference_images` | 可擴充插槽：最多可連接 9 張可選的參考圖片（`image_1`...`image_9`）供新場景使用，每張至少 256x256 像素。在提示詞中會依連接順序以 `@Image1`..`@Image9` 引用。 | IMAGE | 否 | 0 到 9 張圖片 |
| `reference_videos` | 可擴充插槽：最多可連接 3 段可選的參考影片（`video_1`...`video_3`）供新場景使用，每段 2 到 15 秒，總長 15 秒。在提示詞中會依連接順序以 `@Video1`..`@Video3` 引用。 | VIDEO | 否 | 0 到 3 段影片 |
| `prompt` | 新場景。必須提供提示詞或至少一項參考；沒有提示詞的參考通常會被忽略。 | STRING | 是 | 0 到 50000 個字元 |
| `start_time` | 來源影片停止、新場景開始的秒數（預設：2.0）。 | FLOAT | 是 | 1.625 到 60.0 |
| `resume_time` | 新場景結束後，來源影片接續的秒數（預設：3.0）。必須晚於 `start_time`，且至少比影片結尾早 1.375 秒。`start_time` 與 `resume_time` 之間的來源內容會被移除。 | FLOAT | 是 | 1.625 到 60.0 |
| `duration` | 新場景的長度，以秒為單位（預設：5）。 | INT | 是 | 5 到 13 |
| `resolution` | 輸出影片的解析度（預設："768P"）。 | COMBO | 是 | "480P"<br>"768P" |
| `color_match` | 將新場景的顏色與來源影片進行匹配（預設：true）。 | BOOLEAN | 否 | true<br>false |
| `prompt_expansion` | 使用來源影片改寫提示詞。關閉此選項可在相同 `seed` 下獲得可重現的結果（預設：true）。 | BOOLEAN | 否 | true<br>false |
| `seed` | 隨機種子。相同 `seed` 的相同請求會得到相似但不保證完全相同的結果（預設：42）。 | INT | 是 | 0 到 2147483647 |

### 參數限制

- `resume_time` 必須大於 `start_time`，且至少比影片結尾早 1.375 秒，否則請求會被拒絕。
- 每段參考影片的長度必須介於 2 到 15 秒之間，且全部加總不得超過 15 秒。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `video` | 已將新場景拼接至開始時間與接續時間之間的來源影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxInsertVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `623ad0b37f51ce4640c0058676e008697e31563c2a77a3da79ba7936af2d3f99`
