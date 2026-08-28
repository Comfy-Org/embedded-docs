# Wan 2.7 參考生成影片

此節點根據提供的參考素材生成包含人物或物體的影片。它使用 Wan 2.7 模型，根據文字提示建立影片，支援單一角色演出與多角色互動。您必須至少提供一個參考影片或參考圖片，才能進行生成。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影片生成的具體模型。 | DYNAMIC_COMBO | 是 | "wan2.7-r2v" |
| `seed` | 用於生成的種子，有助於控制輸出的隨機性（預設值：0）。 | INT | 是 | 0 至 2147483647 |
| `watermark` | 是否在結果中加入 AI 生成的水印（預設值：False）。這是一項進階設定。 | BOOLEAN | 是 | True<br>False |

### wan2.7-r2v 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `prompt` | 描述影片的提示詞。使用如 'character1' 和 'character2' 等識別碼來指稱參考角色。必須包含至少一個角色。 | STRING | 是 | - |
| `negative_prompt` | 描述應避免內容的負面提示詞（預設值：空白）。 | STRING | 否 | - |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | "720P"<br>"1080P" |
| `ratio` | 輸出影片的長寬比。 | COMBO | 是 | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `duration` | 生成的影片長度（以秒為單位，預設值：5）。 | INT | 是 | 2 至 10 |

### 參考輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `reference_videos` | 可擴充插槽：最多連接 3 個參考影片（插槽 `video1` 至 `video3`）。整體至少需要提供一個參考影片或參考圖片。 | VIDEO | 否 | 0 至 3 items |
| `reference_images` | 可擴充插槽：最多連接 5 個參考圖片（插槽 `image1` 至 `image5`）。整體至少需要提供一個參考影片或參考圖片。 | IMAGE | 否 | 0 至 5 items |

**重要約束：**

* 您必須在 `reference_videos` 或 `reference_images` 輸入中至少提供一個參考影片或參考圖片。
* 參考影片與參考圖片的總數不得超過 5。
* `prompt` 輸入必須包含至少一個字元。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `output` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ReferenceVideoApi/zh-TW.md)

---
**Source fingerprint (SHA-256):** `52ac550522bf3fe8f57444ce8586fe83be470b893ff8c01292743553cfbd623d`
