# PixVerse V6 圖像轉影片

此節點使用 PixVerse V6 模型將輸入影像製作成動畫，並回傳一段影片，可選擇同時包含原生音軌。輸出影片會保持輸入影像的長寬比。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `圖像` | 要製作成動畫的輸入影像。 | IMAGE | 是 | 單一影像 |
| `模型` | 模型與生成設定。 | DYNAMIC_COMBO | 是 | "PixVerse V6" |

### PixVerse V6 輸入

當選取「PixVerse V6」模型時，會顯示這些設定。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的提示詞（預設：空白）。 | STRING | 是 | 1 至 5000 個字元 |
| `quality` | 輸出解析度。設定長邊：360p 為 640px，540p 為 1024px，720p 為 1280px，1080p 為 1920px（預設："720p"）。 | COMBO | 是 | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | 生成影片的長度，以秒為單位（預設：5）。 | INT | 是 | 1 至 15 |
| `generate_audio` | 生成影片時一併生成原生音軌（預設：true）。 | BOOLEAN | 是 | true or false |
| `multi_clip` | 讓模型將影片切成多個鏡頭，而不是單一連續鏡頭（預設：false）。 | BOOLEAN | 是 | true or false |
| `seed` | 影片生成的種子。PixVerse 會記錄此值，但不會據此重現執行結果（預設：42，已啟用生成後控制）。 | INT | 是 | 0 至 2147483647 |
| `negative_prompt` | 選填的文字描述，用於描述影片中不希望出現的元素（預設：空白）。 | STRING | 否 | 最多 2048 個字元 |
| `style` | 選填的視覺風格，套用於整段影片（預設：無）。 | COMBO | 否 | 有多個選項可用（PixVerse V6 風格預設集） |

注意：`prompt` 必須至少包含一個非空白字元，且最多 5000 個字元；`negative_prompt` 若有提供，最多 2048 個字元。輸出影片一律符合輸入影像的長寬比，因此不需要設定長寬比。僅接受單一輸入影像。當內容審核未通過、供應商帳戶額度不足，或同時生成數量已達上限時，PixVerse 可能會拒絕請求。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 生成的影片；當啟用 `generate_audio` 時，會包含原生音軌。長寬比與輸入影像相符。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6ImageToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6ecf958e510e7afc43f5f0e4e5dfd2b789aea02bec882d928326732501cee7b3`
