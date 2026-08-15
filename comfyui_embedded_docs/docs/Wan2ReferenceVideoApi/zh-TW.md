# Wan 2.7 參考生成影片

此節點根據提供的參考素材，生成包含人物或物體的影片。它使用 Wan 2.7 模型，根據文字提示建立影片，支援單一角色表演與多角色互動。您必須至少提供一個參考影片或參考圖像，才能進行生成。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影片生成的特定模型。 | DYNAMIC_COMBO | 是 | "wan2.7-r2v" |
| `seed` | 用於生成的種子，有助於控制輸出的隨機性（預設值：0）。 | INT | 否 | 0 to 2147483647 |
| `watermark` | 是否在結果中添加 AI 生成的水印（預設值：False）。這是進階設定。 | BOOLEAN | 否 | True<br>False |

### wan2.7-r2v 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model.prompt` | 描述影片的提示。使用諸如 'character1' 和 'character2' 的識別符來引用參考角色。至少必須包含一個角色。 | STRING | 是 | - |
| `model.negative_prompt` | 描述應避免之內容的負面提示（預設值：空）。 | STRING | 否 | - |
| `model.resolution` | 輸出影片的解析度。 | COMBO | 是 | "720P"<br>"1080P" |
| `model.ratio` | 輸出影片的長寬比。 | COMBO | 是 | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `model.duration` | 生成影片的長度（秒）（預設值：5）。 | INT | 是 | 2 to 10 |

### 參考輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model.reference_videos` | 可擴充插槽：最多連接 3 個參考影片（插槽 `video1` 至 `video3`）。整體至少需要一個參考影片或圖像。 | VIDEO | 否 | 0 to 3 items |
| `model.reference_images` | 可擴充插槽：最多連接 5 個參考圖像（插槽 `image1` 至 `image5`）。整體至少需要一個參考影片或圖像。 | IMAGE | 否 | 0 to 5 items |

**重要限制：**

* 您必須在 `model.reference_videos` 或 `model.reference_images` 輸入中至少提供一個參考影片或參考圖像。
* 參考影片與參考圖像的合計總數不得超過 5。
* `model.prompt` 輸入必須至少包含一個角色。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `output` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ReferenceVideoApi/zh-TW.md)

---
**Source fingerprint (SHA-256):** `52ac550522bf3fe8f57444ce8586fe83be470b893ff8c01292743553cfbd623d`
