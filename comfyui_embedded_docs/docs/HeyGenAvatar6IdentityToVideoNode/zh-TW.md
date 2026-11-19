# HeyGen Avatar 6 Identity to Video

使用 Avatar 6 生成 HeyGen 虛擬人偶的說話影片。選擇支援 Avatar 6 的其中一個內建外觀，或貼上你自己的 HeyGen 虛擬人偶 ID，然後用文字腳本或自己的音訊來驅動它。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 模型選擇器。`"heygen-avatar-6-turbo"` 是更便宜、更快速的等級；兩個模型接受相同的輸入與解析度。 | COMBO | 是 | `"heygen-avatar-6"`<br>`"heygen-avatar-6-turbo"` |
| `avatar` | 要呈現的虛擬人偶外觀。支援 Avatar 6 的 19 種內建外觀會直接列出；`custom avatar` 會顯示 `custom_avatar_id`，供你選用在 HeyGen 中建立的外觀。 | DYNAMIC_COMBO | 是 | 19 種內建外觀<br>`custom avatar` |
| `speech` | 使用文字腳本（HeyGen 文字轉語音）或自己的音訊來驅動虛擬人偶。顯示名稱：語音來源。 | DYNAMIC_COMBO | 是 | `"script"`<br>`"audio"` |
| `resolution` | 輸出影片的解析度。預設：`"1080p"`。 | COMBO | 是 | `"1080p"`<br>`"2k"` |
| `aspect_ratio` | 輸出影片的長寬比。`"auto"` 會沿用該虛擬人偶外觀本身的影片素材。預設：`"auto"`。 | COMBO | 是 | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `motion_prompt` | 手勢、表情、姿勢與鏡頭運動的選用指示。預設：空字串。 | STRING | 是 | 多行文字 |
| `motion_expressiveness` | `"less"` 會產生更少、更小的手勢。當兩者重疊時，`motion_prompt` 優先。預設：`"default"`。 | COMBO | 是 | `"less"`<br>`"default"` |
| `seed` | `seed` 控制節點是否應重新執行；無論 `seed` 為何，結果都不具決定性。預設：42。 | INT | 是 | 0 至 2147483647 |

### `custom avatar` 輸入

當 `avatar` 設為 `custom avatar` 時，會顯示這些輸入。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `custom_avatar_id` | 支援 Avatar 6 的 HeyGen 虛擬人偶外觀 ID，例如使用 HeyGen Create Avatar 建立的外觀。預設：空字串。 | STRING | 是 | - |

### `script` 語音輸入

當 `speech` 設為 `"script"` 時，會顯示這些輸入。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `text` | 要讓虛擬人偶說出的文字。預設：空字串。 | STRING | 是 | 最多 5000 個字元 |
| `voice` | 腳本使用的語音。預設選項會使用 HeyGen 指派給該虛擬人偶的語音；使用 HeyGen Create Avatar 建立的虛擬人偶沒有預設語音，因此請為它們選擇語音。 | COMBO | 是 | `"(avatar's default voice)"` 加上 HeyGen 的一般語音清單 |
| `custom_voice_id` | 選用的 HeyGen 語音 ID。設定後，會覆寫上方選取的語音。預設：空字串。 | STRING | 否 | - |
| `voice_speed` | 語速倍率。預設：1.0。 | FLOAT | 否 | 0.5 至 1.5（步進值：0.05） |

### `audio` 語音輸入

當 `speech` 設為 `"audio"` 時，會顯示這些輸入。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `audio` | 供虛擬人偶使用的語音。影片長度會依音訊長度而定。 | AUDIO | 是 | 0.5 秒至 10 分鐘 |

**限制與行為：**

* `custom avatar` 需要非空的虛擬人偶 ID，否則節點會引發錯誤。
* 腳本限制為 5000 個字元，音訊限制為 10 分鐘。
* 定價依輸出影片的秒數計算，並取決於模型與解析度。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 生成的說話影片，會在渲染完成後從 HeyGen 下載。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatar6IdentityToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `952146c3790333883ad08b7031853eb7021c8d18c59e58389b5d57b548820944`
