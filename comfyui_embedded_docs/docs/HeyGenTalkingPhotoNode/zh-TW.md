# HeyGen 說話照片

使用 HeyGen 的 Avatar IV 技術，將一個人的靜態影像動畫化為唇形同步的說話影片。您可以使用 HeyGen 轉換為語音的文字腳本驅動動畫，或提供您自己的音訊讓虛擬化身進行唇形同步。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要動畫化的人物影像。若大於 2K 會自動縮小。 | IMAGE | 是 | - |
| `speech` | 以文字腳本（HeyGen 文字轉語音）或您自己的音訊驅動虛擬化身。 | DYNAMIC_COMBO | 是 | `"script"`<br>`"audio"` |
| `resolution` | 輸出影片解析度（預設：`"1080p"`）。 | COMBO | 否 | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | 輸出長寬比。`"auto"` 跟隨輸入影像（預設：`"auto"`）。 | COMBO | 否 | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `expressiveness` | 動畫臉部與手勢的生動程度（預設：`"low"`）。 | COMBO | 否 | `"low"`<br>`"medium"`<br>`"high"` |
| `seed` | 不會傳送至 HeyGen；變更它以強制重新執行（預設：42）。 | INT | 否 | 0 到 2147483647 |

### 腳本輸入

當 `speech` 為 `"script"` 時顯示。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `text` | 虛擬化身要說的文字（最多 5000 個字元）。產生的語音必須至少 1 秒長。（預設：空） | STRING | 是 | 1 到 5000 個字元 |
| `voice` | 腳本使用的語音（HeyGen 最受歡迎的語音）。 | COMBO | 是 | 有多個選項可用 |
| `custom_voice_id` | 選擇性的 HeyGen 語音 ID。設定時，會覆寫上方選擇的語音。可以使用 HeyGen 語音庫（2000+）中的任何語音。（預設：空） | STRING | 否 | - |
| `voice_speed` | 語音速度倍率（預設：1.0）。 | FLOAT | 否 | 0.5 到 1.5（步進 0.05） |

### 音訊輸入

當 `speech` 為 `"audio"` 時顯示。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `audio` | 供虛擬化身進行唇形同步的音訊，最長 10 分鐘。 | AUDIO | 是 | 最長 10 分鐘 |

注意：當 `speech` 為 `"script"` 時，必須指定 `text`，並透過 `voice` 選擇器（選擇虛擬化身預設語音以外的任何語音）或 `custom_voice_id` 指定語音。當 `speech` 為 `"audio"` 時，則需要 `audio`。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 生成的動態說話照片影片，包含唇形同步的語音。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenTalkingPhotoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2181066a8c6191cfcaa15ece4f89a16c37e76aa22763d6df4007baa20336f05a`
