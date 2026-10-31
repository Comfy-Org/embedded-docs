# MiniMax H3 Max Recast

Recast 會將影片中的人物替換為參考照片中的人物，同時保留來源片段的動作、鏡頭、剪接與聲音。上傳影片後，系統會輪詢 Hailuo 03 Max 任務，並以您選擇的解析度回傳替換人物後的影片。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影片生成的模型。 | DYNAMIC_COMBO | 是 | "MiniMax H3 Max" |

### MiniMax H3 Max 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `video` | 來源影片，長度 5 到 30 秒；每個鏡頭必須為 15 秒或更短。長寬比必須介於 0.4 和 2.5 之間。 | VIDEO | 是 | 5 至 30 秒 |
| `reference_images` | 可擴充插槽：連接 1 到 4 張照片（`image_1`...`image_4`），每張對應一個新人物，至少 256x256 像素。預設會從左到右替換影片中的主要人物。 | IMAGE | 是 | 1 至 4 張圖片 |
| `prompt` | 選填。誰變成誰，或要保留或變更的其他內容。請以 `@Image1`..`@Image4` 指稱照片，例如「該男子變成 @Image2」。 | STRING | 是 | 0 至 2000 個字元 |
| `resolution` | 輸出影片的解析度（預設："768P"）。 | COMBO | 是 | "768P"<br>"1080P" |
| `enhance_realism` | 更自然的皮膚紋理，並讓新人物更好地融入場景（預設：false）。 | BOOLEAN | 否 | true<br>false |
| `seed` | 隨機種子。相同請求搭配相同種子會產生相似但不保證完全相同的結果（預設：42）。 | INT | 是 | 0 至 4294967295 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `video` | 已替換為新人物後的影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxRecastNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a9e6f9edf12653f9f361992a097d1d57e7ba14b3e7dd20008b0e022cabc14c1b`
