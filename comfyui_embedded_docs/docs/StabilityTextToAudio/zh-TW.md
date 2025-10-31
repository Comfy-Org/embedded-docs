> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityTextToAudio/zh-TW.md)

此節點使用 Stability AI 的音訊生成技術，根據您的文字提示來建立音訊內容。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `"stable-audio-2.5"` | 要使用的音訊生成模型（預設值："stable-audio-2.5"） |
| `prompt` | STRING | 是 | - | 用於生成音訊內容的文字描述（預設值：空字串） |
| `duration` | INT | 否 | 1-190 | 控制生成音訊的持續時間（單位：秒）（預設值：190） |
| `seed` | INT | 否 | 0-4294967294 | 用於生成的隨機種子（預設值：0） |
| `steps` | INT | 否 | 4-8 | 控制取樣步驟的數量（預設值：8） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `audio` | AUDIO | 基於文字提示生成的音訊檔案 |