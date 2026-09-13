# PixVerse V6 文字轉影片

PixVerse V6 文字轉影片會使用 PixVerse 的 V6 模型，根據文字提示詞生成影片。此節點會將提示詞以及您選擇的長寬比、解析度、時長和其他設定傳送給 PixVerse，等待生成完成，然後傳回生成的影片——啟用音訊生成時，還會包含原生音軌。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 模型與生成設定。選擇模型並設定其生成選項。 | DYNAMIC_COMBO | 是 | "PixVerse V6" |

### PixVerse V6 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的提示詞。（預設：""） | STRING | 是 | 1–5000 個字元 |
| `aspect_ratio` | 輸出長寬比。選擇 PixVerse V6 支援的其中一種長寬比。 | COMBO | 是 | 提供多個選項 |
| `quality` | 輸出解析度。設定長邊：360p 為 640px，540p 為 1024px，720p 為 1280px，1080p 為 1920px。（預設："720p"） | COMBO | 是 | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | 生成影片的長度，以秒為單位。（預設：5） | INT | 是 | 1–15 |
| `generate_audio` | 與影片一起生成原生音軌。（預設：True） | BOOLEAN | 是 | True<br>False |
| `multi_clip` | 讓模型將影片切成多個鏡頭，而不是一個連續鏡頭。（預設：False） | BOOLEAN | 是 | True<br>False |
| `seed` | 影片生成的種子。PixVerse 會記錄它，但不會用它重現執行結果。支援生成後隨機化。（預設：42） | INT | 是 | 0–2147483647 |
| `negative_prompt` | 選填的文字描述，用於說明影片中不希望出現的元素。（預設：""） | STRING | 否 | 0–2048 個字元 |
| `style` | 選填的視覺風格，套用於整段影片。（預設："none"） | COMBO | 否 | 提供多個選項 |

**注意：** `prompt` 為必填，且去除空白後不得為空；其最大長度為 5000 個字元。`negative_prompt` 限制為 2048 個字元。將 `style` 設為 "none"（預設值）表示不套用任何視覺風格。PixVerse 會記錄 `seed`，但無法用它重現相同的執行結果。此節點會等待 PixVerse 完成影片生成後再下載；如果請求失敗——例如 PixVerse 已達到同時生成數上限、供應商帳戶額度不足，或內容審核拒絕該提示詞——節點會傳回錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `VIDEO` | 生成的影片。如果啟用 `generate_audio`，影片會包含原生音軌。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6TextToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4c268be9720a4606e77a9347570ac26b489625fc6b9528b9d3cceb4497d8683b`
