# MiniMax H3 Max Reframe Video

此節點透過將影片放置到新畫布上並生成周圍區域，將影片調整為新的長寬比。來源影片的時間節奏與聲音會保持不變。可用於將橫向影片轉為直向，或反向操作，且不會因裁切而使主體移出畫面。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影片生成的模型。 | DYNAMIC_COMBO | 是 | "MiniMax H3 Max" |

### MiniMax H3 Max 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `video` | 要重新取景的來源影片，長度為 0.5 至 300 秒。 | VIDEO | 是 | 0.5 至 300 秒 |
| `aspect_ratio` | 輸出畫布的長寬比（預設："9:16"）。 | COMBO | 是 | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4"<br>"21:9"<br>"9:21" |
| `resolution` | 輸出影片的解析度（預設："768P"）。 | COMBO | 是 | "480P"<br>"768P"<br>"1080P" |
| `prompt` | 針對所生成周圍區域的選用引導提示。 | STRING | 是 | 0 至 50000 個字元 |
| `seed` | 隨機種子。相同種子的相同請求會產生相似但不保證完全相同的結果（預設：42）。 | INT | 是 | 0 至 4294967295 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `video` | 依所選長寬比重新取景後的影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxReframeVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `83d780c2fe8c42475d4ad25ad5b318f2a4c135edef9c0ca1ff0d1fd07d90c1c6`
