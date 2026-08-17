# 音訊編碼器編碼

The AudioEncoderEncode 節點透過使用音訊編碼器模型對音訊資料進行編碼來處理該資料。它接收音訊輸入，並將其轉換為可用於後續條件處理管線的編碼表示。此節點將原始音訊波形轉換為適合音訊機器學習應用的格式。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `audio_encoder` | 用於處理音訊輸入的音訊編碼器模型 | AUDIO_ENCODER | 是 | - |
| `audio` | 包含波形和取樣率資訊的音訊資料 | AUDIO | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 由音訊編碼器產生的編碼音訊表示 | AUDIO_ENCODER_OUTPUT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderEncode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `85f77152ccc1e3f4687e2b655283e69e03d90b862d6a676dcb89ea973dd70a63`
