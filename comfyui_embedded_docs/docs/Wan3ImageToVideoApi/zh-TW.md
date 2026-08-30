# Wan 3.0 圖像轉影片

此節點使用 Wan 3.0 模型從首幀圖片生成影片。您可以選擇性地提供末幀圖片來控制影片結尾；模型會建立一部從首幀過渡到末幀的影片。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 選擇要使用的 Wan 3.0 模型變體，並決定下方顯示哪些模型專屬設定。 | DYNAMIC_COMBO | 是 | "wan3.0-video"<br>"wan3.0-video-prime" |
| `首幀` | 首幀圖片。必須恰好一張圖片。 | IMAGE | 是 | 單張圖片 |
| `末幀` | 末幀圖片。模型會生成從首幀過渡到末幀的影片。可選；若提供，則必須恰好一張圖片。 | IMAGE | 否 | 單張圖片 |
| `種子` | 用於生成的種子（預設值：42）。 | INT | 是 | 0 - 2147483647 |
| `浮水印` | 是否在結果中加入 AI 生成的水印（預設值：false）。 | BOOLEAN | 是 | true<br>false |

### wan3.0-video 和 wan3.0-video-prime 輸入

這些模型專屬設定為兩種模型選項所共用，並在選取模型時顯示。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述元素與視覺特徵的提示詞。支援英文與中文。可留空（預設：空）。 | STRING | 是 | 最多 20000 個字元 |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | "1080P"<br>"720P"<br>"480P" |
| `ratio` | 輸出影片的長寬比。使用「adaptive」時，輸出尺寸將根據首幀推導。 | COMBO | 是 | "adaptive"<br>"16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `duration` | 輸出時長（秒）。使用「auto」時，模型會選擇符合提示詞的時長。 | COMBO | 是 | "auto"<br>"2" - "30" |
| `audio` | 輸出影片是否包含音軌（預設值：true）。 | BOOLEAN | 是 | true<br>false |
| `prompt_extend` | 是否使用 AI 輔助增強提示詞（預設值：true）。 | BOOLEAN | 是 | true<br>false |

注意：此節點接受恰好一張 `first_frame` 圖片，並可選接受一張 `last_frame` 圖片。若任一個輸入連接超過一張圖片，將引發錯誤。當提供 `last_frame` 時，生成的影片會從首幀過渡到末幀。`prompt` 限制為 20,000 個字元。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 生成的影片。當啟用 `audio` 選項時，包含音軌。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan3ImageToVideoApi/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ff9fce554fa7aa5fc8729b5f84b2f8bf89e8e7772ce1c32b1307d0dc4882200c`
