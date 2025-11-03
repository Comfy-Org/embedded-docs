> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio/zh-TW.md)

TextEncodeAceStepAudio 節點透過將標籤和歌詞合併為 token，並以可調節的歌詞強度進行編碼，來處理用於音訊條件化的文字輸入。該節點接收 CLIP 模型以及文字描述和歌詞，將它們一起進行 token 化，並生成適合音訊生成任務的條件化資料。此節點允許透過控制歌詞對最終輸出影響程度的強度參數，來微調歌詞的影響力。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | 是 | - | 用於 token 化與編碼的 CLIP 模型 |
| `tags` | STRING | 是 | - | 用於音訊條件化的文字標籤或描述（支援多行輸入與動態提示） |
| `lyrics` | STRING | 是 | - | 用於音訊條件化的歌詞文字（支援多行輸入與動態提示） |
| `lyrics_strength` | FLOAT | 否 | 0.0 - 10.0 | 控制歌詞對條件化輸出影響的強度（預設值：1.0，步長：0.01） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | 包含已處理文字 token 並套用了歌詞強度的編碼條件化資料 |