> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderLoader/zh-TW.md)

AudioEncoderLoader 節點會從您可用的音訊編碼器檔案中載入音訊編碼器模型。它接收音訊編碼器檔案名稱作為輸入，並返回已載入的音訊編碼器模型，可在您的工作流程中用於音訊處理任務。

## 輸入參數

| 參數名稱 | 資料類型 | 輸入類型 | 預設值 | 數值範圍 | 描述 |
|-----------|-----------|------------|---------|-------|-------------|
| `audio_encoder_name` | STRING | COMBO | - | 可用的音訊編碼器檔案 | 從您的 audio_encoders 資料夾中選擇要載入的音訊編碼器模型檔案 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `audio_encoder` | AUDIO_ENCODER | 返回已載入的音訊編碼器模型，供音訊處理工作流程使用 |