# YuE2 生成音樂

從風格、歌詞和 ABC 記譜生成音樂 token 與聲學條件。它會傳回條件以及生成的持續時間（以秒為單位），這些應提供給 Empty YuE2 Latent Audio 節點。如果 ABC 輸入留空，則忽略所選模式，並自動使用 off 模式。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `clip` | 用於將音樂輸入 token 化並編碼的 CLIP 模型。 | CLIP | 是 | - |
| `style` | 描述音樂風格的文字。支援多行輸入和動態提示詞。 | STRING | 是 | Multiline text |
| `lyrics` | 生成音樂的歌詞。支援多行輸入和動態提示詞。 | STRING | 是 | Multiline text |
| `abc` | 連接 ABC 生成器，或提供已編輯的樂譜。留空以自動使用 off 模式。預設值："" | STRING | 是 | Multiline text |
| `seed` | 生成用的隨機種子。預設值：0 | INT | 是 | 0 至 18446744073709551615 |
| `mode` | full：生成旋律與和弦；melody：僅生成旋律，建議用於翻唱。預設值："full" | COMBO | 是 | "full"<br>"melody" |
| `max_duration` | 最大持續時間（秒）。對於長提示詞會自動縮短；生成可能會提前停止。預設值：360.0 | FLOAT | 是 | 0.04 至 900.0 |
| `temperature` | 生成用的取樣溫度。預設值：1.0（進階） | FLOAT | 是 | 0.0 至 5.0 |
| `top_p` | 核心取樣機率閾值。預設值：0.95（進階） | FLOAT | 是 | 0.01 至 1.0 |
| `top_k` | Top-k 取樣限制。預設值：100（進階） | INT | 是 | 1 至 32768 |
| `repetition_penalty` | 對重複 token 施加的懲罰。預設值：1.2（進階） | FLOAT | 是 | 0.01 至 10.0 |

注意：如果 `abc` 為空或僅包含空白字元，則會忽略 `mode` 選擇，並自動使用 off 模式。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `CONDITIONING` | 由音樂 token 生成的聲學條件。 | CONDITIONING |
| `seconds` | 生成的音訊持續時間（秒）。請將此值提供給 Empty YuE2 Latent Audio 節點。 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/YuE2GenerateMusic/zh-TW.md)

---
**Source fingerprint (SHA-256):** `54f5d46cf083726bdf97c86e5683b2727840f75bb553bddf9525cfbf5affa44c`
