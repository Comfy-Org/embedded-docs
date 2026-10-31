# MiniMax H3 Max Lip Sync

此節點會讓靜態圖片動起來，使嘴部動作配合所提供的音訊軌。圖片與音訊上傳後，會輪詢 Hailuo 03 Max 對嘴工作，並以您選擇的解析度回傳說話影片。輸出影片的長度與音訊相同。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影片生成的模型。 | DYNAMIC_COMBO | 是 | "MiniMax H3 Max" |

### MiniMax H3 Max 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `image` | 要製成動畫的圖片，至少 256x256 像素。長寬比必須介於 0.4 與 2.5 之間。 | IMAGE | 是 | 單張圖片 |
| `audio` | 要進行對嘴的音訊，長度為 5 到 899 秒。 | AUDIO | 是 | 5 到 899 秒 |
| `resolution` | 輸出解析度（預設值："768P"）。長寬比會採用最接近原圖的支援比例。 | COMBO | 是 | "480P"<br>"768P"<br>"1080P"<br>"2K" |
| `transcription` | 轉錄音訊以引導對嘴同步（預設值：false）。 | BOOLEAN | 否 | true<br>false |
| `seed` | 隨機種子。相同請求搭配相同種子會產生相似但不保證完全相同的結果（預設值：42）。 | INT | 是 | 0 到 2147483647 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `video` | 說話影片，長度與輸入音訊相同。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxLipSyncNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0af4166f9f3237cacc3506d6c6544c0374a330cf998f8bd2ef1f4f7162e2f9ab`
