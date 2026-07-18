# HeyGenTalkingPhotoNode

使用 HeyGen 的 Avatar IV 技術，將靜態人物照片動畫化為唇形同步的說話影片。您可以透過 HeyGen 轉換為語音的文字腳本驅動動畫，或提供自訂音訊讓虛擬人物進行唇形同步。

## 輸入
| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要動畫化的人物圖片。若大於 2K 會自動縮小。 | IMAGE | 是 | - |
| `speech` | 使用文字腳本（HeyGen 文字轉語音）或自訂音訊驅動虛擬人物。 | COMBO | 是 | `"script"`<br>`"audio"` |
| `text` | 虛擬人物要說的文字（最多 5000 個字元）。生成的語音長度至少需 1 秒。 | STRING | 是（當 speech 為 "script" 時） | - |
| `voice` | 腳本使用的語音（HeyGen 最受歡迎的語音選項）。 | COMBO | 是（當 speech 為 "script" 時） | 提供多種選項 |
| `custom_voice_id` | 可選的 HeyGen 語音 ID。設定後會覆蓋上方選擇的語音。可使用 HeyGen 資料庫中超過 2000 種語音。 | STRING | 否 | - |
| `voice_speed` | 語速倍率（預設值：1.0）。 | FLOAT | 否 | 0.5 至 1.5 |
| `audio` | 供虛擬人物唇形同步的音訊，最長 10 分鐘。 | AUDIO | 是（當 speech 為 "audio" 時） | - |
| `resolution` | 輸出影片解析度（預設值："1080p"）。 | COMBO | 否 | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | 輸出畫面比例。'auto' 會跟隨輸入圖片（預設值："auto"）。 | COMBO | 否 | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `expressiveness` | 動畫臉部與手勢的表達程度（預設值："low"）。 | COMBO | 否 | `"low"`<br>`"medium"`<br>`"high"` |
| `seed` | 不會發送至 HeyGen；變更此值可強制重新執行（預設值：42）。 | INT | 否 | 0 至 2147483647 |

## 輸出
| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 生成的動畫說話照片影片，包含唇形同步的語音。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenTalkingPhotoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2181066a8c6191cfcaa15ece4f89a16c37e76aa22763d6df4007baa20336f05a`
