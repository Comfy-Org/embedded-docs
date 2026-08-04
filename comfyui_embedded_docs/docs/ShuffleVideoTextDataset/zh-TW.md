# 隨機排序影片-文字配對

此節點會隨機打亂影片-文本對的順序，確保每個影片仍與其對應的文本配對。它接收兩個長度相同的列表，並對兩者施加相同的隨機排列，從而保證原始配對在打亂後得以保留。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|------|------|----------|------|------|
| `影片` | 要打亂的影片列表。 | VIDEO | 是 | List of video items |
| `文字` | 要打亂的文本列表。 | STRING | 是 | List of text strings |
| `隨機種子` | 控制打亂順序的隨機種子（預設值：0）。 | INT | 是 | 0 to 18446744073709551615 |
注意：`videos` 和 `texts` 的長度必須相同，因為節點會將每個影片與同一位置的文字配對，並在洗牌時保持這些配對。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|----------|------|----------|
| `影片` | 以新的隨機順序打亂後的影片。 | VIDEO |
| `文字` | 與影片相同新順序的打亂後文本。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleVideoTextDataset/zh-TW.md)

---
**Source fingerprint (SHA-256):** `33b763a6d48ca1036d5267139f90eadb3b2080a02fa57ce5bcae6087a077efa1`
