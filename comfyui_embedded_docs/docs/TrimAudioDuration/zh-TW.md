> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimAudioDuration/zh-TW.md)

TrimAudioDuration 節點允許您從音訊檔案中剪裁特定時間區段。您可以指定開始剪裁的時間點以及剪裁後音訊片段的長度。此節點的工作原理是將時間值轉換為音訊幀位置，並提取音訊波形中對應的部分。

## 輸入參數

| 參數名稱 | 資料類型 | 是否必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | 是 | - | 要進行剪裁的音訊輸入 |
| `start_index` | FLOAT | 是 | -0xffffffffffffffff 至 0xffffffffffffffff | 開始時間（單位：秒），可為負值表示從音訊結尾開始計算（支援小於秒的單位）。預設值：0.0 |
| `duration` | FLOAT | 是 | 0.0 至 0xffffffffffffffff | 持續時間（單位：秒）。預設值：60.0 |

**注意：** 開始時間必須小於結束時間且在音訊長度範圍內。負的開始時間值表示從音訊結尾向前倒數計算。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `audio` | AUDIO | 經過剪裁的音訊片段，具有指定的開始時間和持續時長 |