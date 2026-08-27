# 音訊編碼器載入器

AudioEncoderLoader 節點會從您的 audio_encoders 資料夾中的檔案載入音訊編碼器模型。它接受音訊編碼器模型的檔案名稱作為輸入，並傳回已載入的模型，該模型隨後可用於工作流程中的音訊處理任務。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `audio_encoder_name` | 選擇要載入的音訊編碼器模型檔案 | COMBO | 是 | audio_encoders 資料夾中可用的音訊編碼器檔案清單 |

注意：如果選取的檔案不包含有效的音訊編碼器模型，節點將引發錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `audio_encoder` | 已載入的音訊編碼器模型，可用於音訊處理工作流程 | AUDIO_ENCODER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `780d0c7fcf571e5ef02d273791e5d2e894baa6d5900d845ed65e9ce669769f7e`
