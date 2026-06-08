AudioEncoderLoader 節點會從音訊編碼器資料夾中的檔案載入音訊編碼器模型。它接收音訊編碼器模型的檔案名稱作為輸入，並傳回已載入的模型，該模型隨後可用於工作流程中的音訊處理任務。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `audio_encoder_name` | 選擇要載入的音訊編碼器模型檔案 | STRING | 是 | audio_encoders 資料夾中可用的音訊編碼器檔案列表 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `audio_encoder` | 已載入的音訊編碼器模型，可用於音訊處理工作流程 | AUDIO_ENCODER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `24cbd45198db7d950633358c29de57f56c999bc33534fabe80404528d194163c`
