# Fish Audio 語音選擇器

Fish Audio Voice Selector 節點會從 Fish Audio 音色庫中選擇一個語音，用於文字轉語音生成。你可以選擇其中一個內建預設語音，或選擇 "custom" 來輸入任何來自 fish.audio 的語音模型 ID。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `voice` | 選擇一個語音，或選擇 "custom" 以輸入任何 fish.audio 語音模型 ID。 | DYNAMIC_COMBO | 是 | "Energetic Male (en)"<br>"Friendly Women (en)"<br>"Sarah (en)"<br>"Verity (en)"<br>"Polo (en)"<br>"Adrian (en)"<br>"E-girl (en)"<br>"Narrator (en)"<br>"Warm Conversational Voice (en)"<br>"Warm Storyteller (en)"<br>"Dramatic Character Male (en)"<br>"News Narrator (zh)"<br>"Lively Female (zh)"<br>"Gentle Female (zh)"<br>"Energetic Female (ja)"<br>"Calm Female (ja)"<br>"Calm Male (ja)"<br>"custom" |

預設語音選項涵蓋英文 (en)、中文 (zh) 和日文 (ja) 語音，且不需要任何額外輸入。

### 自訂輸入

當 `voice` 設為 "custom" 時，這些輸入會出現。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `voice_id` | 來自 fish.audio 的語音模型 ID，例如 https://fish.audio/m/<id>/ 中的 ID。預設值：空字串。 | STRING | 是 | Any valid Fish Audio voice model ID |

注意：當 `voice` 設為 "custom" 時，`voice_id` 在去除空白後不得為空；否則節點會引發 "Custom voice ID is empty." 錯誤。若傳入無法辨識的語音選項，節點會引發 "Unknown voice" 錯誤。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `voice` | 所選的 Fish Audio 語音模型 ID。若為預設語音，則會傳回 Fish Audio 音色庫中對應的語音 ID；若為 "custom"，則會傳回輸入的 `voice_id` 值。 | FISHAUDIO_VOICE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioVoiceSelector/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4f99a58aa7e6054f58fe84e61e4e1008b17828bd97d71ef0a4009c4de4052bbd`
