# 音訊編碼器編碼

AudioEncoderEncode 節點會使用音訊編碼器模型，將音訊轉換為編碼後的表示形式。它接收一個音訊編碼器和一個音訊輸入，接著從音訊中擷取波形與取樣率，並將它們傳遞給編碼器以產生編碼輸出。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `audio_encoder` | 用於處理音訊輸入的音訊編碼器模型 | AUDIO_ENCODER | 是 | - |
| `音訊` | 包含波形與取樣率資訊的音訊資料 | AUDIO | 是 | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `output` | 由音訊編碼器產生的編碼音訊表示 | AUDIO_ENCODER_OUTPUT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderEncode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `85f77152ccc1e3f4687e2b655283e69e03d90b862d6a676dcb89ea973dd70a63`
