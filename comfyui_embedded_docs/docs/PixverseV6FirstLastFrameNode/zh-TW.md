# PixVerse V6 首尾影格轉影片

PixVerse V6 First-Last-Frame to Video 會使用 PixVerse 產生從第一影格過渡到最後影格的影片，並可選擇搭配原生音訊。兩張提供的影像會傳送到 PixVerse API，由 API 產生過渡影片並以影片檔案形式回傳。輸出會保持第一影格的長寬比。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `first_frame` | 影片的起始影像。 | IMAGE | 是 | — |
| `last_frame` | 影片的結束影像。 | IMAGE | 是 | — |
| `模型` | 模型與生成設定。選擇 PixVerse 模型並顯示其生成參數。 | DYNAMIC_COMBO | 是 | "PixVerse V6" |

### PixVerse V6 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述過渡效果的提示詞。 | STRING | 是 | 最多 5000 個字元 |
| `quality` | 輸出解析度。設定長邊：360p 為 640px，540p 為 1024px，720p 為 1280px，1080p 為 1920px。（預設：720p） | COMBO | 是 | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | 生成影片的長度，以秒為單位。（預設：5） | INT | 是 | 1 到 15 |
| `generate_audio` | 與影片一併生成原生音軌。（預設：true） | BOOLEAN | 是 | true<br>false |
| `seed` | 影片生成的種子。PixVerse 會記錄此值，但不會用它重現執行結果。（預設：42） | INT | 是 | 0 到 2147483647 |
| `negative_prompt` | 描述影片中不希望出現元素的選填文字。 | STRING | 否 | 最多 2048 個字元 |
| `style` | 套用到整部影片的選填視覺風格。（預設：none） | COMBO | 否 | 提供多個選項（預設："none"） |

注意：移除空白後，`prompt` 不得為空，且限制為 5000 個字元。提供 `negative_prompt` 時，其限制為 2048 個字元。`duration_seconds` 必須介於 1 到 15 秒之間。輸出影片會保持第一影格的長寬比。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 生成的影片，會從第一影格過渡到最後影格；啟用 `generate_audio` 時會包含音軌。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6FirstLastFrameNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `cdb5e45e9de2b429b9d43bbff90b6529af246911ecae8c2809c8abd539101aaa`
