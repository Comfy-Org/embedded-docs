# Wan 2.7 影片編輯

Wan 2.7 Video Edit 節點使用文字指令、參考圖片或風格轉換來編輯影片。它會將輸入影片（以及任何參考圖片）傳送至 Wan 2.7 video-edit 服務，並根據所選的解析度、長寬比和持續時間設定，傳回新產生的影片。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於影片編輯的模型。每個選項都會公開自己的一組子參數。 | DYNAMIC_COMBO | 是 | `"wan2.7-videoedit"` |
| `video` | 要編輯的影片。 | VIDEO | 是 | - |
| `seed` | 用於生成的種子。（預設值：0） | INT | 是 | 0 至 2147483647 |
| `audio_setting` | 'auto'：模型根據提示決定是否重新生成音訊。'origin'：保留輸入影片的原始音訊。（預設值："auto"） | COMBO | 是 | `"auto"`<br>`"origin"` |
| `watermark` | 是否在結果中加入 AI 生成浮水印。（預設值：False） | BOOLEAN | 是 | - |

### wan2.7-videoedit 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 編輯指令或風格轉換需求。（預設值：空字串） | STRING | 是 | - |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | `"720P"`<br>`"1080P"` |
| `ratio` | 長寬比。如果未變更，則會近似輸入影片的長寬比。 | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | 輸出持續時間（秒）。'auto' 會符合輸入影片的持續時間。特定值會從影片開頭截斷。（預設值："auto"） | COMBO | 是 | `"auto"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |

### 參考輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | 可增長的插槽：連接 0 至 4 張圖片（`image1`...`image4`）以引導編輯。wan2.7-videoedit 模型的數量上限為 4。 | IMAGE | 否 | 0 至 4 items |

**限制：**
*   `audio_setting` 和 `watermark` 是進階選項。
*   `prompt` 必須包含至少 1 個字元。
*   輸入 `video` 的持續時間必須介於 2 到 10 秒之間。
*   `reference_images` 可增長插槽最多接受 4 張圖片。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 模型產生的已編輯影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoEditApi/zh-TW.md)

---
**Source fingerprint (SHA-256):** `27283273ee56c90903db103a3e9bc17dc4df0914676c9aedd2a115b07937dc10`
