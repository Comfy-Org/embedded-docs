# PixVerse V6 文字轉影片

PixVerse V6 文字轉影片會使用 PixVerse 的 V6 模型，根據文字提示產生影片。此節點會將提示詞連同您選擇的解析度、時長、畫面比例及其他設定傳送至 PixVerse，等待生成完成，然後回傳產生的影片——若啟用音訊生成，也會包含原生音訊軌。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 模型與生成設定。選取模型並設定其生成選項。 | DYNAMIC_COMBO | 是 | "PixVerse V6" |

### PixVerse V6 輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 影片生成的提示詞。（預設值：""） | STRING | 是 | 1–5000 字元 |
| `aspect_ratio` | 輸出畫面比例。從 PixVerse V6 支援的畫面比例中選擇一個。 | COMBO | 是 | 多個可用選項 |
| `quality` | 輸出解析度。設定長邊：360p 為 640px，540p 為 1024px，720p 為 1280px，1080p 為 1920px。（預設值："720p"） | COMBO | 是 | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | 生成影片的長度（秒）。（預設值：5） | INT | 是 | 1–15 |
| `generate_audio` | 與影片一起生成原生音訊軌。（預設值：True） | BOOLEAN | 是 | True<br>False |
| `multi_clip` | 讓模型將影片剪輯成多個鏡頭，而非單一連續鏡頭。（預設值：False） | BOOLEAN | 是 | True<br>False |
| `seed` | 影片生成的隨機種子。PixVerse 會記錄它，但不會用於重現執行。支援生成後隨機化。（預設值：42） | INT | 是 | 0–2147483647 |
| `negative_prompt` | 影片中不希望出現元素的選用文字描述。（預設值：""） | STRING | 否 | 0–2048 字元 |
| `style` | 套用於整部影片的選用視覺風格。（預設值："none"） | COMBO | 否 | 多個可用選項 |

**注意：** `prompt` 為必填，且在去除前後空白後不得為空；最大長度為 5000 字元。`negative_prompt` 限制為 2048 字元。將 `style` 設為 "none"（預設值）即表示不套用任何視覺風格。`seed` 會被 PixVerse 記錄，但無法用來重現相同的執行。此節點會等待 PixVerse 完成影片生成後再下載；如果請求失敗——例如因為 PixVerse 已達到同時生成的上限、提供者帳戶額度不足，或內容審核拒絕了提示詞——節點會回傳錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
|-------------|-------------|-----------|
| `VIDEO` | 生成的影片。若已啟用 `generate_audio`，影片會包含原生音訊軌。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6TextToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4c268be9720a4606e77a9347570ac26b489625fc6b9528b9d3cceb4497d8683b`
