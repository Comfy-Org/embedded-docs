# HeyGenAvatarVideoNode

此節點使用 HeyGen 的渲染引擎，建立一個 AI 虛擬角色朗讀您提供的文字，或與您自己的音訊進行嘴型同步的影片。

## 輸入
| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `engine` | 渲染引擎；每個選項僅列出支援該引擎的虛擬角色。'auto' 提供所有虛擬角色並選取最佳引擎（優先使用 Avatar IV）。Avatar V 為最高保真度，Avatar III 為最經濟實惠的選項。 | COMBO | 是 | `"auto"`<br>`"avatar_iv"`<br>`"avatar_iii"`<br>`"avatar_v"` |
| `custom_avatar_id` | 可選的 HeyGen 虛擬角色外觀 ID。設定後將覆蓋上方選取的虛擬角色。可使用 HeyGen 超過 3000 個公開外觀（或您的私人虛擬角色）中的任何一個。 | STRING | 否 |  |
| `speech` | 使用文字腳本（HeyGen 文字轉語音）或您自己的音訊來驅動虛擬角色。 | COMBO | 是 | `"script"`<br>`"audio"` |
| `resolution` | 輸出影片解析度（預設："1080p"）。 | COMBO | 否 | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | 輸出影片長寬比。'auto' 跟隨虛擬角色的原始素材（預設："auto"）。 | COMBO | 否 | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `background_color` | 可選的純色背景，以十六進位色碼表示（例如 '#00ff00'）。留空則使用虛擬角色自身的背景。 | STRING | 否 |  |
| `seed` | 不會發送至 HeyGen；變更此值可強制重新執行（預設：42）。 | INT | 否 | 最小值：0<br>最大值：2147483647 |

當 `speech` 設定為 `"script"` 時，可使用以下子參數：

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `text` | 虛擬角色要朗讀的文字（最多 5000 個字元）。生成的語音長度必須至少 1 秒。 | STRING | 是 |  |
| `voice` | 腳本使用的語音。預設選項使用 HeyGen 分配給虛擬角色的語音。 | COMBO | 是 | 多個選項可用 |
| `custom_voice_id` | 可選的 HeyGen 語音 ID。設定後將覆蓋上方選取的語音。可使用 HeyGen 語音庫（超過 2000 種）中的任何一種語音。 | STRING | 否 |  |
| `voice_speed` | 語音速度倍率（預設：1.0）。 | FLOAT | 否 | 最小值：0.5<br>最大值：1.5<br>步進：0.05 |

當 `speech` 設定為 `"audio"` 時，可使用以下子參數：

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `audio` | 虛擬角色進行嘴型同步的音訊，最長 10 分鐘。 | AUDIO | 是 |  |

## 輸出
| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `VIDEO` | 生成的虛擬角色主持人影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatarVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `009bc72b841ca273af83fe6f80fb24d4b11c2efd96c011795b1ff1cf8e66ee61`
