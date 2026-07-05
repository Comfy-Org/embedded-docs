# Kling 文字口型同步影片

Kling 唇形同步文字轉影片節點可將影片檔案中的嘴部動作與文字提示同步。它接收輸入影片，並生成一個新影片，其中角色的唇部動作與提供的文字對齊。此節點使用語音合成來創造自然的語音同步效果。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `影片` | 用於唇形同步的輸入影片檔案 | VIDEO | 是 | - |
| `文字` | 唇形同步影片生成的文字內容。當模式為 text2video 時為必要。最大長度為 120 個字元。 | STRING | 是 | - |
| `語音` | 唇形同步音訊的語音選擇（預設值："Melody"） | COMBO | 否 | "Melody"<br>"Bella"<br>"Aria"<br>"Ethan"<br>"Ryan"<br>"Dorothy"<br>"Nathan"<br>"Lily"<br>"Aaron"<br>"Emma"<br>"Grace"<br>"Henry"<br>"Isabella"<br>"James"<br>"Katherine"<br>"Liam"<br>"Mia"<br>"Noah"<br>"Olivia"<br>"Sophia" |
| `語速` | 語速。有效範圍：0.8~2.0，精確至小數點後一位。（預設值：1） | FLOAT | 否 | 0.8-2.0 |

**影片要求：**

- 影片檔案不得大於 100MB
- 高度/寬度應在 720px 至 1920px 之間
- 時長應在 2 秒至 10 秒之間

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `影片 ID` | 生成的影片，包含唇形同步音訊 | VIDEO |
| `影片 ID` | 生成影片的唯一識別碼 | STRING |
| `時長` | 生成影片的時長資訊 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncTextToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f16200d52ba05acfedebc027dde91e2c91bdbb80086888d947c9f56a4e92856d`
