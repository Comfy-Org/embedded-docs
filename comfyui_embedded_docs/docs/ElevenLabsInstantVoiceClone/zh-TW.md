> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsInstantVoiceClone/zh-TW.md)

此節點透過分析 1 至 8 段人聲錄音，創建一個全新且獨特的語音模型。它會將這些樣本發送至 ElevenLabs API 進行處理，以生成可用於文字轉語音合成的語音複製品。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `audio_*` | AUDIO | 是 | 1 至 8 個檔案 | 用於語音複製的音訊錄音。您必須提供 1 到 8 個音訊檔案。 |
| `remove_background_noise` | BOOLEAN | 否 | True / False | 使用音訊隔離技術從語音樣本中移除背景噪音。(預設值: False) |

**注意：** 您必須提供至少一個音訊檔案，最多可提供八個。節點會根據您添加的音訊檔案自動創建輸入插槽。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `voice` | ELEVENLABS_VOICE | 新創建的複製語音模型的唯一識別碼。此輸出可連接至其他 ElevenLabs 文字轉語音節點。 |
