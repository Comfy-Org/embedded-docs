# FishAudioInstantVoiceClone

此節點使用 Fish Audio API 從您的音訊錄音建立私人克隆語音。您提供一個或多個音訊樣本，節點會建立可立即用於文字轉語音的自訂語音。它接受 1 到 20 個錄音，每個錄音建議長度為 10 到 30 秒，總長度上限為 270 秒。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `檔案` | 用於語音克隆的音訊錄音。這是一個可增長輸入：連接一個或多個音訊項目（例如 `audio_1`、`audio_2`……）以提供語音樣本。 | AUDIO | 是 | 1 到 20 個錄音 |
| `enhance_audio_quality` | 在訓練前增強參考音訊品質（預設值：True）。 | BOOLEAN | 是 | True<br>False |

**注意：** 所有參考音訊合併後的總時長必須少於 270 秒。如果合併時長達到或超過 270 秒，節點將回傳錯誤。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `語音` | 新建立的克隆語音，由 Fish Audio API 回傳的唯一語音 ID 識別。此語音可用於文字轉語音。 | FISHAUDIO_VOICE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioInstantVoiceClone/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6c4f011a4611a076b2488152591efeb61c029d6dfae2b079ba74689891c84803`
