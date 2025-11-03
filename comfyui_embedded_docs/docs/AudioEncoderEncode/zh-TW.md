> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderEncode/zh-TW.md)

AudioEncoderEncode 節點透過使用音訊編碼器模型對音訊資料進行編碼處理。它接收音訊輸入並將其轉換為編碼表示，可在條件處理流程中用於後續處理。此節點將原始音訊波形轉換為適合基於音訊的機器學習應用的格式。

## 輸入參數

| 參數名稱 | 資料類型 | 輸入類型 | 預設值 | 數值範圍 | 描述 |
|-----------|-----------|------------|---------|-------|-------------|
| `audio_encoder` | AUDIO_ENCODER | 必填 | - | - | 用於處理音訊輸入的音訊編碼器模型 |
| `audio` | AUDIO | 必填 | - | - | 包含波形和取樣率資訊的音訊資料 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | AUDIO_ENCODER_OUTPUT | 由音訊編碼器生成的編碼音訊表示 |