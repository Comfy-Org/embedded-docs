# TextEncodeAceStepAudio

TextEncodeAceStepAudio 節點通過將標籤和歌詞合併為 token，然後以可調整的歌詞強度進行編碼，來處理用於音訊條件化的文字輸入。它接收一個 CLIP 模型以及文字描述和歌詞，將它們一起 token 化，並生成適合音訊生成任務的條件化資料。該節點允許透過一個強度參數來微調歌詞的影響，該參數控制其對最終輸出的作用。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 用於分詞和編碼的 CLIP 模型 | CLIP | 是 | - |
| `標籤` | 用於音訊條件化的文字標籤或描述（支援多行輸入和動態提示） | STRING | 是 | - |
| `歌詞` | 用於音訊條件化的歌詞文字（支援多行輸入和動態提示） | STRING | 是 | - |
| `歌詞強度` | 控制歌詞對條件化輸出影響的強度（預設值：1.0，步長：0.01） | FLOAT | 是 | 0.0 - 10.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `conditioning` | 包含已處理的文字 token 以及應用的歌詞強度的編碼條件化資料 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2226c9f25dd26bf454bcce2e298d6d261dace5a9bbed164a2fcf0e1204d7c3f4`
