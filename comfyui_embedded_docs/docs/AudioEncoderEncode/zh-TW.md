> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderEncode/zh-TW.md)

## 概述

AudioEncoderEncode 節點透過使用音訊編碼器模型對音訊資料進行編碼處理。它接收音訊輸入，並將其轉換為編碼後的表示形式，可用於條件處理管線中的後續操作。此節點將原始音訊波形轉換為適合基於音訊的機器學習應用程式的格式。

## 輸入

| 參數 | 資料類型 | 輸入類型 | 預設值 | 範圍 | 說明 |
|-----------|-----------|------------|---------|-------|-------------|
| `audio_encoder` | AUDIO_ENCODER | 必要 | - | - | 用於處理音訊輸入的音訊編碼器模型 |
| `audio` | AUDIO | 必要 | - | - | 包含波形和取樣率資訊的音訊資料 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | AUDIO_ENCODER_OUTPUT | 由音訊編碼器產生的編碼後音訊表示形式 |

---
**Source fingerprint (SHA-256):** `8de45c157937ee95fbaef06aaefe478db7be8b16088d92720d977fe3d14eee39`
