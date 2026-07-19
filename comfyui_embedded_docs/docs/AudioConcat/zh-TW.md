# 音訊串接

## 概述

AudioConcat 節點透過將兩個音訊輸入連接在一起來合併它們。它接收兩個音訊輸入，並依照您指定的順序進行連接，可將第二個音訊放置在第一個音訊之前或之後。此節點會自動處理不同的音訊格式，將單聲道音訊轉換為立體聲，並匹配兩個輸入之間的取樣率。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `audio1` | 要連接的第一個音訊輸入 | AUDIO | 是 | - |
| `audio2` | 要連接的第二個音訊輸入 | AUDIO | 是 | - |
| `direction` | 決定將 audio2 附加在 audio1 之後或之前（預設值："after"） | COMBO | 是 | `"after"`<br>`"before"` |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `AUDIO` | 包含兩個輸入音訊檔案連接後的合併音訊 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioConcat/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b54046e29761cf27bc5b1c065dac87846613afc0b5cbb296632628bf7d4527b7`
