> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningStableAudio/zh-TW.md)

ConditioningStableAudio 節點為音訊生成的正向與負向條件輸入添加時間資訊。它設定開始時間和總持續時間參數，有助於控制音訊內容的生成時機與長度。此節點透過附加音訊專用的時間元數據來修改現有的條件資料。

## 輸入參數

| 參數名稱 | 資料類型 | 是否必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 需添加音訊時間資訊的正向條件輸入 |
| `negative` | CONDITIONING | 是 | - | 需添加音訊時間資訊的負向條件輸入 |
| `seconds_start` | FLOAT | 是 | 0.0 至 1000.0 | 音訊生成的起始時間（單位：秒，預設值：0.0） |
| `seconds_total` | FLOAT | 是 | 0.0 至 1000.0 | 音訊生成的總持續時間（單位：秒，預設值：47.0） |

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 已應用音訊時間資訊的修改後正向條件 |
| `negative` | CONDITIONING | 已應用音訊時間資訊的修改後負向條件 |