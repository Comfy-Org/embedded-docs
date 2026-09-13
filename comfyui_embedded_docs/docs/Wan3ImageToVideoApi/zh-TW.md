# Wan 3.0 圖像轉影片

此節點使用 Wan 3.0 模型，從第一幀圖像生成影片。您可以選擇性地提供最後一幀圖像來控制影片的結尾方式；模型接著會建立一段從第一幀過渡到最後一幀的影片。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 選擇要使用的 Wan 3.0 模型變體，並決定下方顯示哪些模型特定設定。 | DYNAMIC_COMBO | 是 | "wan3.0-video"<br>"wan3.0-video-prime" |
| `首幀` | 第一幀圖像。必須正好提供一張圖像。 | IMAGE | 是 | 單張圖像 |
| `末幀` | 最後一幀圖像。模型會生成從第一幀過渡到最後一幀的影片。此為選填；若提供，必須正好提供一張圖像。 | IMAGE | 否 | 單張圖像 |
| `種子` | 生成時使用的種子（預設值：42）。 | INT | 是 | 0 - 2147483647 |
| `浮水印` | 是否在結果中加入 AI 生成的浮水印（預設值：false）。 | BOOLEAN | 是 | true<br>false |

### wan3.0-video 與 wan3.0-video-prime 輸入

這些模型特定設定為兩個模型選項共用，並會在選取模型後顯示。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述元素與視覺特徵的提示詞。支援英文與中文。可留空（預設值：空）。 | STRING | 是 | 最多 20000 個字元 |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | "1080P"<br>"720P"<br>"480P" |
| `ratio` | 輸出影片的長寬比。使用 "adaptive" 時，輸出尺寸會從第一幀推導。 | COMBO | 是 | "adaptive"<br>"16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `duration` | 輸出時長，以秒為單位。使用 "auto" 時，模型會選擇符合提示詞的時長。 | COMBO | 是 | "auto"<br>"2" - "30" |
| `audio` | 輸出影片是否包含音軌（預設值：true）。 | BOOLEAN | 是 | true<br>false |
| `prompt_extend` | 是否使用 AI 輔助增強提示詞（預設值：true）。 | BOOLEAN | 是 | true<br>false |

注意：此節點接受正好一張 `first_frame` 圖像，並可選填一張 `last_frame` 圖像。若任一個輸入連接超過一張圖像，會引發錯誤。提供 `last_frame` 時，生成的影片會從第一幀過渡到最後一幀。`prompt` 限制為 20,000 個字元。每次執行的價格取決於所選的 `model`、`resolution` 和 `duration`。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 生成的影片。當啟用 `audio` 選項時，會包含音軌。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan3ImageToVideoApi/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ff9fce554fa7aa5fc8729b5f84b2f8bf89e8e7772ce1c32b1307d0dc4882200c`
