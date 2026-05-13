> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsInstantVoiceClone/zh-TW.md)

# ElevenLabs 即時語音克隆節點

ElevenLabs 即時語音克隆節點透過分析 1 到 8 段個人語音的音訊錄音，建立一個全新的、獨特的語音模型。它將這些樣本發送到 ElevenLabs API，由 API 處理後產生一個可用於文字轉語音合成的語音克隆。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `audio_*` | AUDIO | 是 | 1 到 8 個檔案 | 用於語音克隆的音訊錄音。您必須提供 1 到 8 個音訊檔案。 |
| `remove_background_noise` | BOOLEAN | 否 | True / False | 使用音訊隔離技術從語音樣本中移除背景噪音。（預設值：False） |

**注意：** 您必須至少提供一個音訊檔案，最多可提供八個。節點會自動為您新增的音訊檔案建立輸入插槽。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `voice` | ELEVENLABS_VOICE | 新建立的克隆語音模型的唯一識別碼。此輸出可連接到其他 ElevenLabs 文字轉語音節點。 |

---
**Source fingerprint (SHA-256):** `297598e183df3ccddabc75d6903c5c69f10648adeea430e546f9c5f6df49bdb2`
