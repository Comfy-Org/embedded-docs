# AudioMerge 節點

AudioMerge 節點透過疊加波形來合併兩個音軌。它會自動匹配兩個音訊輸入的取樣率，並在合併前將它們的長度調整為相等。此節點提供了多種數學方法來組合音訊訊號，並確保輸出保持在可接受的音量範圍內。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `audio1` | 要合併的第一個音訊輸入 | AUDIO | 是 | - |
| `audio2` | 要合併的第二個音訊輸入 | AUDIO | 是 | - |
| `merge_method` | 用於組合音訊波形的方法。 | COMBO | 是 | `"add"`<br>`"mean"`<br>`"subtract"`<br>`"multiply"` |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `AUDIO` | 合併後的音訊輸出，包含組合後的波形和取樣率 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioMerge/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2a4a7da42835efd03cc67002e617a70c0514524a0ac0ed61d57e499c1283be95`
