# PixVerse V6 首尾影格轉影片

PixVerse V6 首幀到尾幀轉場影片生成使用 PixVerse 產生一段從首幀過渡到尾幀的影片，並可選擇搭配原生音訊。兩張提供的圖片會傳送至 PixVerse API，由其產生轉場影片並以影片檔案形式回傳。輸出的影片會保持首幀的長寬比。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `first_frame` | 影片的起始影像。 | IMAGE | 是 | — |
| `last_frame` | 影片的結束影像。 | IMAGE | 是 | — |
| `模型` | 模型與生成設定。選擇 PixVerse 模型並顯示其生成參數。 | DYNAMIC_COMBO | 是 | "PixVerse V6" |

### PixVerse V6 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述轉場效果的文字提示。 | STRING | 是 | 最多 5000 個字元 |
| `quality` | 輸出解析度。設定長邊：360p 為 640px，540p 為 1024px，720p 為 1280px，1080p 為 1920px。（預設：720p） | COMBO | 是 | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | 產生影片的長度（秒）。（預設：5） | INT | 是 | 1 至 15 |
| `generate_audio` | 與影片同時產生原生音訊軌。（預設：true） | BOOLEAN | 是 | true<br>false |
| `seed` | 影片生成的種子。PixVerse 會記錄該值，但不會據此重現生成結果。（預設：42） | INT | 是 | 0 至 2147483647 |
| `negative_prompt` | 對影片中不想要元素的選用文字描述。 | STRING | 否 | 最多 2048 個字元 |
| `style` | 套用於整個影片的選用視覺風格。（預設：none） | COMBO | 否 | 有多種選項可用（預設："none"） |

注意：提示文字在移除空白字元後不得為空，且長度限制為 5000 個字元。若提供了負面提示，則其長度限制為 2048 個字元。影片時長必須介於 1 至 15 秒之間。輸出影片會保持首幀的長寬比。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的影片，內容為從首幀過渡到尾幀；當啟用 `generate_audio` 時，會包含音訊軌。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6FirstLastFrameNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `cdb5e45e9de2b429b9d43bbff90b6529af246911ecae8c2809c8abd539101aaa`
