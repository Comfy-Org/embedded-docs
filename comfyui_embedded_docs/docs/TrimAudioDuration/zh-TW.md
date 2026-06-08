## 概述

TrimAudioDuration 節點可讓您從音訊檔案中裁剪出特定的時間區段。您可以指定裁剪的起始時間以及結果音訊片段的長度。此節點透過將時間值轉換為音訊幀位置，並提取音訊波形中的對應部分來運作。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `音訊` | 要進行裁剪的音訊輸入 | AUDIO | 是 | - |
| `起始索引` | 起始時間（秒），可為負數以從結尾倒數（支援小數秒）。預設值：0.0 | FLOAT | 是 | -0xffffffffffffffff 至 0xffffffffffffffff |
| `持續時間` | 持續時間（秒）。預設值：60.0 | FLOAT | 是 | 0.0 至 0xffffffffffffffff |

**注意：** 起始時間必須小於結束時間，且須在音訊長度範圍內。負數的起始值會從音訊結尾向前倒數計算。若起始時間為負數，則會轉換為從音訊結尾倒數的幀位置。起始與結束幀會被限制在音訊邊界內。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `音訊` | 已裁剪的音訊片段，具有指定的起始時間與持續時間 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimAudioDuration/zh-TW.md)

---
**Source fingerprint (SHA-256):** `695a9fe11fa086a317f94823e066688705e9f911cd6cfc5857596ff31dd539ed`
